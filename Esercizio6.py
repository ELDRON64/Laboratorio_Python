import Additional.Rubrica as R

def is_int ( s ):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def Parse\
	( comm : str, parameters : list[list] ) -> list:
		r"""parsed a command in the form: \<name> -a \<type> -b \<null> -c \<type> ...
		
		The passed dictz specifies the type of the parameter after the argument
		
		The returned lis is like this:
		\{
			"comm" : \<name>
			"-a" : \<value\>,
			"-b" : \<value\>,
			...
			"arg1" : \<value>
			...
			"argn" : \<value>
		}
		the values are checed for type ad not added if not present

		If there are no arguments
		[
			"comm" : \<name>
			"-a" : \<default\>,
			"-b" : \<default\>,
			...
			"arg1" : \<value>
			...
			"argn" : \<value>
		]
		the inputed parameters list must be like
		pars = [
			["-a",..."-x"] ## aviable parameters listed in order
			["-a","int",/<default>] ## single parameter with it's type and the dault value 
			...
			["-x","str",/<default>]
		]
		!! The list is not ckecked for errors !!

		if the command has some arguments ( not specidied by -X )
		they will be putted at the end named as "arg1", ... "argn"
		"""

		arguments = { 
			"comm" : ""
		}
		
		## inizilize with defualt values
		for argu in parameters [1:]:
			##		    name		default
			arguments [ argu[0] ] = argu[2]
        
		splitted_commad = [] 
		## string literals delimited by ' or " ( sorry but mixed is allowed )
		s_litteral = False
		temp = ''

		for char in comm:
			if char == ' ' and not s_litteral:
				splitted_commad.append(temp)
				temp = ''
				continue
			if char in [ "'","'" ]:
				s_litteral = not s_litteral
				continue
			temp += char
		splitted_commad.append ( temp )

		checking_parameter = False
		arguments_count = 1

		for index in range ( 0, len ( splitted_commad ) ):
			if checking_parameter: ## skips the token after -X because it is verified the the -X token is found
				checking_parameter = False
				continue

			token = splitted_commad [ index ]

			if arguments ["comm"] == "":
				arguments ["comm"] = token
				continue

			if token in parameters[0]:
				## this is a parameter now it's apropriate to chek the type
				parameter_type_index = parameters[0].index ( token )
				## get the type
				parameter_type = parameters [ parameter_type_index + 1 ]

				if parameter_type[1] == "NIL":
					arguments[token] = "YES"
					continue

				if index + 1 == len ( splitted_commad ):
					raise "the " + parameter_type + "misses it's parameter"
				
				value = splitted_commad [ index + 1 ] ## by defaul it's string
				
				match parameter_type [1]:
					case "int":
						if is_int ( value ):
							value = (int) ( value )
						else:
							raise "argument type error"
						pass
					case "bool":
						if not value in ['true','True','False','false']:
							raise "argument type error"               
						value = value in ['True','true']

				arguments[token] = value
				checking_parameter = True

			else:
				arg_name = "arg" + (str)(arguments_count)
				arguments[ arg_name ] = token
				arguments_count += 1

		return arguments


rub = R.Rubrica( )
com = ""
while com != "EXIT":
	com = input ( 'cicciogamer@localhost % ' )
	com = Parse ( com, [['-j'],['-j','bool',True]] )
	try: 
		match com['comm'].upper():
			case 'APRI':
				rub.APRI ( com['arg1'], com['-j'] )

			case 'AGGIUNGI':
				rub.AGGIUNGI ( [ com['arg'+str(i)] for i in range (1,8) ] )

			case 'RIMUOVI':
				rub.RIMUOVI ( com['arg1'] )

			case 'SALVA':
				rub.SALVA ( com['arg1'], com['-j'] )

			case 'STAMPA':
				rub.STAMPA ( com['arg1'] )
			
			case 'HELP':
				print ( """I Comandi disponibili sono:
\tAPRI <file> <-j> apre il file e ne carica il contnuto se -j è specificato lo spre come json
\tAGGIUNGI <giorno>, <mese>, <anno>, <età>, <sesso>, <mail> aggiunge il contatto descritto
\tRIMUOVI <nome> rimove il contatto
\tSALVA <file> <-j> salva la rubrica nel file ( che è conideator json se -j è presente )
\tSTAMPA <nome> stampa il contatto
\tEXIT provalo
		""")

			case 'EXIT':
				print ( "hello i'm under the water plis help me\n" )
				exit ( )
	except IndexError:
		print ( "sono stati forniti troppo pochi argomenti" )
	except KeyError:
		print ( "la persona cercata non esite" )
	except TypeError:
		print ( "missing parameters" )
	except R.RubricaError:
		pass # already printed
