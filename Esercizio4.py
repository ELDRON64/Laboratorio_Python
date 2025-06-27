#
# Esercizio4.py
#
# Elia Castellarin
#
# 30 Aprile 2025
# 
# versione 1.0
# 
# Stampa in un file la rubrica 
#

rubrica = {
	'Paolino Paperino': {'giorno': 9, 'mese': 'giugno', 'anno': 1934, 'età': 89, 'sesso': 'M', 'mail': 'paolino.paperin0@disney.org'},
	'Ron Weasley': {'giorno': 1, 'mese': 'marzo', 'anno': 1980, 'età': 43, 'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'},
	'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 19, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
	'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 54, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

with open( 'rubrica.txt', 'w' ) as file:
    print ( '----- printing rubrica to text file' )
    for nome in rubrica:
        file.write ( nome )
        for att in rubrica[nome]:
            file.write ( f', {rubrica[nome][att]}' )
        file.write ( '\n' )

import json

with open( 'rubrica.json', 'w' ) as file:
    print ( '\n----- printing rubrica to json file' )
    json.dump ( rubrica, file, indent = 4 )

with open( 'rubrica.json', 'r' ) as file:
    data = json.load ( file )
    print ( f'\n----- reading rubrica from json file\n\n{json.dumps ( data, indent = 4 ) }\n' )

