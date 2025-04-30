import re

testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

testo_righe = len ( [ elem for elem in testo.split ('\n') if elem != '' ] )
testo_parole = len ( [ elem for elem in re.split ( r' |\n', testo ) if elem != '' ] )
testo_caratteri = len ( list ( testo ) )
testo_PYTHON = re.sub( r'day|about|water',"PYTHON", testo, flags=re.IGNORECASE )  
testo_dispari = ' '.join ( [ elem if not index % 2 else elem.upper() for index, elem in enumerate ( testo.replace('\n\n',' 0\0').replace('\n',' \0').split ( ' ' ) ) ] ).replace ( ' \0','\n' ).replace ( ' 0\0', '\n\n' )
testo_specchio = '\n'.join ( [ elem[::-1] if index % 5 == 2 else elem for index, elem in enumerate ( testo.split ('\n') ) ] ) 

print ( f"------ Metedata: ------------\n\nnumero righe: {testo_righe};\nnumero parole: {testo_parole};\nnumero caratteri: {testo_caratteri};\n" )
print ( f"------ testo PYTHON: --------\n{testo_PYTHON}" )
print ( f"------ testo dispari: -------\n{testo_dispari}" )
print ( f"------ testo a specchio: ----\n{testo_specchio}") 

parole_strofa = [ { re.sub ( r'(?![a-z]|[a-z]).*', '', token ).capitalize() for token in re.split( ' |\n', elem ) } for elem in testo.split ( '\n\n' ) ]
joined_parole = parole_strofa [0]
joined_parole.remove ( '' )

for parole in parole_strofa:
    joined_parole &= parole

if joined_parole == set():
    print ( "------ non ci sono ripetizioni " )
else:
    print ( f"------ parole ripetute -----\n{joined_parole}")

parole = set( )
for token in re.split ( ' |\n', testo ):
    # pulisco il token
    token = re.sub ( r'(?![a-z]|[a-z]).*', '', token )
    parole.add(token)

parole_ordinate = sorted ( parole, key = lambda token : len ( token ) )
parole_ordinate.remove ( '' )
print ( f"\n------ parole ordinate ------\n\n{parole_ordinate}" )

frequenze = {}
for c in list ( testo ):
    if c in frequenze:
        frequenze[c] += 1
    else:
        frequenze[c] = 1

frequenze_caratteri = { chr(i) : 0 for i in range (65,90) }
for c in list ( testo ):
    if ( 64 < ord (c) and ord (c) < 91 ) or ( 96 < ord(c) and ord(c) < 123 ):
        c = c.upper()
        frequenze_caratteri[c] += 1

print ( f'\n------- tutti i caratteri: ---\n\n{frequenze};\n\n------- tutti i caratteri ( ma diverso ): \n\n{(frequenze_caratteri)}')   

