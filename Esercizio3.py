rubrica = {
	'Paolino Paperino': {'giorno': 9, 'mese': 'giugno', 'anno': 1934, 'età': 89, 'sesso': 'M', 'mail': 'paolino.paperin0@disney.org'},
	'Ron Weasley': {'giorno': 1, 'mese': 'marzo', 'anno': 1980, 'età': 43, 'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'},
	'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 19, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
	'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 54, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

def punto_1 ( ):
    print ( "----- Ecco tutta la rubrica: \n" )
    for nome in rubrica:
        print ( f"{nome}: ", end = '')
        for data in rubrica[nome]:
            print ( f"'{data}' {rubrica[nome][data]},", end = ' ' )
    print ('\n')

sorted_rubrica = sorted ( rubrica, key = lambda nome : rubrica[nome]['età'] )

def punto_2 ( ):
    print ( "----- Ecco i nomi in ordine di erà:\n" )
    for data in sorted_rubrica:
        print ( data )

def punto_3 ( ):
    print ( "----- Ecco i nomi in contrordine di età:\n" )
    for data in sorted_rubrica[::-1]:
        print ( data )

def punto_4 ( ):
    print ( "----- Messaggi peronalizzati: \n" )
    for nome in rubrica:
        r = rubrica[nome]
        print ( f'''Car{'a' if r['sesso'] == 'F' else 'o'} {nome},
sei nat{'a' if r['sesso'] == 'F' else 'o'} il {r['giorno']} di {r['mese']} del {r['anno']} e quindi a breve compirai {r['età']+1} anni.
Ti manderemo gli auguri a {r['mail']}\n''' )

import sys
if len ( sys.argv ) > 1:
    if sys.argv[1] in ['giorno', 'mese', 'anno', 'età', 'sesso', 'mail']:
        print ( f"----- args {sys.argv[1]}\n" )
        for nome in rubrica:
            print ( rubrica[nome][sys.argv[1]] )

        exit () # prevent argparse from printing error

import argparse

parser =  argparse.ArgumentParser()
parser.add_argument ( '-n', '--nome', default='', help='il nome della pesona da salutare?' )
parser.add_argument ( '-p', '--punto', default=0, help='il numero del punto da eseguire')
args = parser.parse_args ( )

if ( args.nome != '' ):
    r = rubrica[args.nome]
    print ( f'''Car{'a' if r['sesso'] == 'F' else 'o'} {args.nome},
sei nat{'a' if r['sesso'] == 'F' else 'o'} il {r['giorno']} di {r['mese']} del {r['anno']} e quindi a breve compirai {r['età']+1} anni.
Ti manderemo gli auguri a {r['mail']}''' )

match args.punto:
    case '1': punto_1()
    case '2': punto_2()
    case '3': punto_3()
    case '4': punto_4()

