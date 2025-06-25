from threading import Thread
from threading import Lock
import random
import time
import numpy

from colorama import Fore, Style

gen = random.Random()
rng = numpy.random.default_rng()

def print_sc ( sol:set ) -> None:
    for y in sol:
        for x in range ( len(sol) ):
            print ( (Fore.GREEN + 'o ' if ( x == y ) else 'x ' ), end='' )
            print ( Style.RESET_ALL,end='' )
        print ( )

def stessa_diagonale(x0, y0, x1, y1):
    '''Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale"
    '''
    dy = abs(y1 - y0)
    dx = abs(x1 - x0) 

    return dx == dy     


def incrocia_colonne(posizioni, col):
    '''Ritorna Vero se la colonna 'col', che indica la posizione della regina
      (col, posizioni[col]) incrocia la diagonale di qualcuna 
      delle posizioni delle regine precedenti 
    '''
    for c in range(col):     
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            return True  
    return False   

def soluzione_ok ( soluzione_posizioni:list ) -> int:
    '''Controlla tutte le posizioni della possibile soluzione
       'soluzione_posizioni' per verificare se ognuna delle posizioni 
       (colonne dela permatazione) ogni colonna incrocia la diagonale
       di qualche altra posizione
    '''
    for col in range(1, len(soluzione_posizioni)):
        if incrocia_colonne(soluzione_posizioni, col):
            return 0 

    return 1

def genera_soluzione ( size:int ) -> list:
    sol = [i for i in range(size)]
    gen.shuffle ( sol )
    return sol

start_time = time.time( )
soluzioni = 0
while soluzioni < 10:
    soluzioni += soluzione_ok ( genera_soluzione ( 8 ) )

print ( f'----- Tempo medio per trovare una delle 10 soluzioni: { ( time.time ( ) - start_time ) / 10 }')

# Suppongo che in 8x8 ci siano 92 soluzioni distinte. Continuo fino a che le soluzioni uniche non siano 92
# Non intraprendo un approccio sequenziale per mantere la randomicità dei singoli casi.
soluzioni = set()
count_sol = dict()
tentativi = 0

while ( len( soluzioni) != 92 ):
    tentativi += 1
    sol = genera_soluzione (8)
    if ( soluzione_ok ( sol ) ):
        sol = ''.join( [str(i)for i in sol] ) ## used for hasable property
        if ( sol not in count_sol.keys ( ) ):
            count_sol[sol] = 0
        count_sol[sol] += 1
        soluzioni.add ( sol )
    ## print ( f'-- attuali tentativi {tentativi}, {len(count_sol)} {count_sol}')

print ( f'\n----- Trovate tutte le 92 soluzioni in {tentativi} tentativi' )

sorted_sols = sorted ( count_sol, key = lambda x : count_sol[x] )
# print ( sorted_sols )
print ( '\n------ Soluzioni ripetute\n')
for sol in sorted_sols:
    if count_sol[sol] > 1:
        print_sc ( [ int(i) for i in sol ] )
        print ( f'^^^^^^^^^^^^^^^ questa soluzione è stata ripetuta {count_sol[sol]} volte\n' )

## spawn a thread that after 30 seconds is killed
## if the hread result is non detrimined a solution is not found
## this is for preventing to wait for an hour so plz don't kill me

lokker = Lock( )
def trova_soluzione ( size:int, result:list, index:int, max_time:float ) -> None :
    # print ( f'--- dispatching thread for {size}x{size}' ) 
    start = time.time ( )
    tentativi = 0
    sol = genera_soluzione (size)
    while not soluzione_ok ( sol ):
        if start + max_time < time.time():
            break
        sol = genera_soluzione (size)
        tentativi += 1
    t = time.time ( ) - start
    lokker.acquire ( )
    result[index][1] += ( t if t < max_time else 0 )
    result[index][0] += ( 1 if t < max_time else 0 )

    # print ( f'--- finished thread for {size}x{size} with {tentativi}' ) 

    lokker.release ( )
    return

## starting threads
threads_list = []
start_co = 14
counting = 5 
samples = 5
threads_sols = [ [0,0] for i in range (counting) ] ## records, time

max_time = 30

for i in range ( samples ):
    for i in range ( counting ):
        tester = Thread ( target = trova_soluzione, args=(i+start_co,threads_sols,i,max_time))
        tester.start ( )
        threads_list.append ( tester )

## waiting
print ( "----- stiamo aspettando che le soluzioni arrivino per favore attendere")
for i in threads_list:
   i.join() 

## counting
for i in range ( counting ):
    if ( threads_sols[i][0] > 0 ):
        print ( f'------ found {threads_sols[i][0]} for {start_co+i}x{start_co+i} in {threads_sols[i][1]/threads_sols[i][0]} seconds' )
    else:
        print ( f"------ {i+start_co} non ce l'ha fatta")





def simmetrize ( sol:list ):
    soluzioni = []
    soluzioni.append ( ''.join( [str(i)for i in sol] ) )
    for i in range ( 3 ):
        ## ruota lista di 90 gradi
        ## x = -y
        ## y = x
        new_sol = [0]*len(sol)
        
        for x,y in enumerate ( sol ):
            new_sol[len(sol)-1-y] = x

        sol = new_sol
        soluzioni.append ( ''.join( [str(i)for i in sol] ) )

    return soluzioni

soluzioni_uniche = []
while ( len(soluzioni_uniche) != 40 ):
    sol = genera_soluzione ( 8 )
    if ( soluzione_ok ( sol ) and sol not in soluzioni_uniche ):
        soluzioni_uniche.extend ( simmetrize ( sol ) )

print ( '\n----- ecco le 40 soluzioni uniche\n' )
for solll in soluzioni_uniche:
    list_solll = [ int(i) for i in solll ]
    print ( f'soluzione {solll}' )
    print_sc ( list_solll )
    print ( )



