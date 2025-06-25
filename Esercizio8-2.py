import os
import json
import random
from colorama import Fore, Style

def error ( message:str ):
	print ( message )

if not os.path.isfile ( "words" ):
	error ( "no words?" )

with open ( "words", 'r' ) as f:
	# hope that it parse
	# the only whay to chek for a non json input is to parse it
	words = json.load ( f )

if words == {}:
	error ( "empty words list" )

## this is safe since words is a dictorary from the json load
letter = random.choice ( list ( words.keys ( ) ) )

if words[letter] == []:
	error ( "empty words list" )

word = random.choice ( words [ letter ] )

guess = ''

while ( guess != word ):
	# ask
	guess = input ( "Inserire una parola di 5 lettere: " )
	guess = guess.upper ( )

	print ( f'hai provato {guess}' )

	# check size
	if len ( guess ) != 5:
		print ( "the inserted word is not valid" )
		continue 

	right = []
	quasi = []
	for index, char in enumerate ( word ):
		if ( char == guess[index] ):
			right.append ( index )
		for c in range (0,5):
			if ( char == guess [c] and c != index ):
				quasi.append ( c )
	
	for i in range (0,5):
		if i in right:
			print ( Fore.GREEN + guess[i], end='' )
		elif i in quasi:
			print ( Fore.YELLOW + guess[i], end='' )
		else:
			print ( Fore.WHITE + guess[i], end='' ) 
	
	print ( Style.RESET_ALL)

print ( "Complimenti hai indovinato" )
