import Additional.Tartaruga as Tartaruga
import Additional.Command as Command

def Punto3 ():
	pippo = Command.Controller ( )

	pippo.Command ( "start && turtle g" )
	comm = input ( "inserisci comando " )
	while ( comm not in [ "exit", "end" ] ):
		try:
			pippo.Command ( comm )
		except:
			print ( "command not found, use help" )
		comm = input ( "inserisci comando " )
	try:
		pippo.Command ( "end" )
	except Tartaruga._tkinter.TclError:
		pass

	exit ( )

	pass

def Punto4 ():
	pippo = Command.Controller ( )

	pippo.Command ( "start && turtle g -p 5" )

	for i in range ( 1, 6 ):
		pippo.Command ( f"squa -s {i*20}" )

	pippo.Command ( "loop" )
	exit ( )
	pass

def Punto5 ():
	pippo = Command.Controller ( )
	pippo.Command ( "start && turtle g -p 5" )

	for i in range ( -1,2 ):
		color = input ( f"colore del {i+2}° triangolo " )
		pippo.Command ( f" move {69*2*i} 0 -a && tria -s 42 -c { color }" )

	print ( "done" )
	pippo.Command ( "loop" )

	exit ( )
	pass

def Punto6 ():
	dimenzione = input ( "inserire la dimensione di partenza: " )
	if ( not Command.is_int (dimenzione) ):
		Punto6 ( )
	dimenzione = int(dimenzione)

	lati = input ( "inserire il numero dei lati: " )
	if ( not Command.is_int ( lati ) ):
		Punto6 ( )
	lati = int(lati)

	pippo = Command.Controller ( )
	pippo.Command ( "start && turtle g -p 2" )

	next_dir = [-dimenzione*2,0]
	scale_mult = 1.6
	for lato in range ( lati ):
		pippo.Command ( f"""tria -s {int(dimenzione/2.8)} -c green && move {next_dir[0]} {next_dir[1]} && squa -s {int(dimenzione)} -c pink && move {next_dir[0]} {next_dir[1]} && cross -s {int(dimenzione/3)} -c blue """ )
		next_dir = [-next_dir[1],next_dir[0]]
		pippo.Command ( f'move {next_dir[0]} {next_dir[1]}' )

		dimenzione *= scale_mult
		next_dir [0] = int( next_dir[0] * scale_mult)
		next_dir [1] = int( next_dir[1] * scale_mult)
	pippo.Command ( "loop" )

	exit ( )
	pass

if __name__ == '__main__':
	try:
		match int(input('numero esercizio? ')):
			case 3: Punto3 ( )
			case 4: Punto4 ( )
			case 5: Punto5 ( )
			case 6: Punto6 ( )
	except ValueError:
		print ( 'no' )
