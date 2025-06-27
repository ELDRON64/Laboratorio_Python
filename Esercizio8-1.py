#
# Esercizio8-1.py
#
# Elia Castellarin
#
# 25 Giugno 2025
# 
# versione 1.1
# 
# wordle
#

import json
import random
from colorama import Fore, Style

def error ( message:str ):
	print ( message )

words = dict ( )
try:
	with open ( "Additional/words", 'r' ) as f:
		try:
			words = json.load ( f )
		except json.decoder.JSONDecodeError:
			error ( "Json load error" )
except FileNotFoundError:
	error ( "no words?" )

## choose a word
try:
	letter = random.choice ( list ( words.keys ( ) ) )
	word = random.choice ( words [ letter ] )
except IndexError:
	error ( 'no words in list' )

guess = ''
tentativi = 0
while ( guess != word ):
	tentativi += 1
	if tentativi > 5:
		print ( "enniente" )
		exit ( )
	# ask
	try: 
		guess = input ( "Inserire una parola di 5 lettere: " )
	except KeyboardInterrupt:
		print ( "\nperché? PERCHE\' NON VUOI ESSERE MIO AMICO?" )
		continue

	
	guess = guess.upper ( )

	print ( f'hai provato {guess}' )

	try:
		guess [5]
		print ( "the word is to long, nice try")
		continue
	except IndexError:
		pass
	
	right = []
	quasi = []
	for index, char in enumerate ( word ):
		try: 
			if ( char == guess[index] ):
				right.append ( index )
		except IndexError:
			# error ( "Parola inserita è troppo corta" )
			# il messaggio diventa noioso dopo un po
			pass
		for c in range (0,5):
			try:
				if ( char == guess [c] and c != index ):
					quasi.append ( c )
			except IndexError:
				# error ( "Parola inserita è troppo corta" )
				pass
	
	for i in range (0,5):
		try:
			if i in right:
				print ( Fore.GREEN + guess[i], end='' )
			elif i in quasi:
				print ( Fore.YELLOW + guess[i], end='' )
			else:
				print ( Fore.WHITE + guess[i], end='' )
		except IndexError:
			break
	
	print ( Style.RESET_ALL)

print ( "Complimenti hai indovinato" )
