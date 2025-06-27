#
# Esercizio7.py
#
# Elia Castellarin
#
# 30 Aprile 2025
# 
# versione 1.0
# 
# Calcola e stampa l'integrale di 3 funzioni
#

import matplotlib.pyplot as plt
import numpy as np

class Integral:
    def __init__ ( self, Interval, function, name = '?' ):
        self.I = Interval
        self.f = function
        self.fig, self.axes = plt.subplots ( nrows=2, ncols=1 )
        self.name = name
    
    @staticmethod
    def R_sum ( I, N, f ):
        step = ( I[1] - I[0] ) / N
        
        somma = -f(I[0])
        for x in np.linspace ( I[0], I[1], N, endpoint = False ):
            somma += f(x) ## considero la somma delle basi del trapezio
    
        somma *= 2 
        somma += f(I[0]) + f(I[1]) ## for including the center ones 2 times and the edge one only 1 time
        somma /= 2
        somma *= step ## moltiplico per l'altezza del trapezio

        return somma

    def Compute ( self, N_iniziale:int, N_max:int, epsilon:float ):
        result = self.R_sum ( self.I, N_iniziale, self.f )
        while ( N_iniziale < N_max-1 ):
            N_iniziale+=1
            temp = self.R_sum ( self.I, N_iniziale, self.f )
    
            if abs ( ( result - temp ) ) < epsilon:
                result = temp
                break

            result = temp
            N_iniziale+=1
        
        return ( result, N_iniziale )

    def Print ( self, N_iniziale, N_finale, valore ) -> None:

        ## initial step
        x = np.linspace ( self.I[0], self.I[1], N_iniziale )
        y = [ self.f(x_1) for x_1 in x ]
        self.axes[0].plot (x,y)

        xv = [ i for i,j in zip(x,y) if j > valore ]
        yv = [ j for i,j in zip(x,y) if j > valore ]
        self.axes[1].plot (xv,yv)

        ## initial step
        x = np.linspace ( self.I[0], self.I[1], int( ( N_finale + N_iniziale ) / 2 ) )
        y = [ self.f(x_1) for x_1 in x ]
        self.axes[0].plot (x,y)

        xv = [ i for i,j in zip(x,y) if j > valore ]
        yv = [ j for i,j in zip(x,y) if j > valore ]
        self.axes[1].plot (xv,yv)

        ## initial step
        x = np.linspace ( self.I[0], self.I[1], N_finale )
        y = [ self.f(x_1) for x_1 in x ]
        self.axes[0].plot (x,y)

        xv = [ i for i,j in zip(x,y) if j > valore ]
        yv = [ j for i,j in zip(x,y) if j > valore ]
        self.axes[1].plot (xv,yv)
 
        self.fig.savefig(f'{self.name}.png')



f = lambda x : (1/(np.sqrt(2*np.pi))) * np.exp (-0.5*pow(x,2)) 
g = lambda x : np.sin ( 10 / pow ( x, 2 ) ) if x != 0 else 0
h = lambda x : x*x

Interval = [-4,4]
N_default = 9
epsilon = 0.001
valore = 0.10

if __file__ == "__main__" or True:
    N_max = int ( input ( "Quando vuoi essere sicuro ( N > 42 ) " ) )
    
    ## create objekts
    F = Integral ( Interval, f, 'f' )
    G = Integral ( Interval, g, 'g' )
    H = Integral ( Interval, h, 'h' )

    F_i, F_n = F.Compute ( N_default, N_max, epsilon )
    G_i, G_n = G.Compute ( N_default, N_max, epsilon )
    H_i, H_n = H.Compute ( N_default, N_max, epsilon )

    print ( f"L'integrale della funzione F è quasi {F_i} con N: {F_n}" )
    print ( f"L'integrale della funzione G è quasi {G_i} con N: {G_n}" )
    print ( f"L'integrale della funzione H è quasi {H_i} con N: {H_n}" )

    F.Print ( N_default, F_n, valore )
    G.Print ( N_default, G_n, valore )
    H.Print ( N_default, H_n, valore )

