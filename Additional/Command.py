import Additional.Tartaruga as Tartaruga

def is_int ( s ):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

class Controller:
	def __init__(self):
		self.window = None 
		self.turtles = {}

	def Parse_Arguments\
	( self, comm : str, parameters : list[list] ) -> list:
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

		splitted_commad = comm.split ( " " )
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
				
				arguments[token] = value
				checking_parameter = True

			else:
				arg_name = "arg" + (str)(arguments_count)
				arguments[ arg_name ] = token
				arguments_count += 1

		return arguments

	def Draw_Command\
	( self, comm : str ) -> None:
		r"""Draws the selected thing
		every command has the following options:
			-a \<int> set a rotation angle for the figure
			-c \<color> colors the figure
			-t \<name> draws with the specified turle by defaults uses the first
		
			the possible shapes are:
		cross [option] ( draws a cross on screen )
			-s \<int> sets the cross size
		
		rect [options] ( draws a rectangle )
			-h \<int> sets the rectangle heigth
			-w \<int> sets the rectangle width
		
		squa [option] ( draws a square )
			-s \<int> size of the square

		tria [options] ( draws a equlateral traingle )
			-s \<int> set the triangle with side s

		poly [options] ( draws an regular polyong )
			-s \<int> set the poly side length
			-r \<int> set the poly sides

		if are provided more arguments they will be ignored
		"""
		
		parametri = [
			[ "-a", "-c", "-t", "-s", "-h", "-w", "-r" ],
			[ "-a", "int", 0 ],
			[ "-c", "str", "red" ],
			[ "-t", "str", "" ],
			[ "-s", "int", 20 ],
			[ "-h", "int", 20 ],
			[ "-w", "int", 20 ],
			[ "-r", "int", 3 ]
		]
		aviable_commands = [
			"cross",
			"rect",
			"squa",
			"tria",
			"poly"
		]

		parsed_command = self.Parse_Arguments ( comm, parametri )
		# print ( parsed_command )
		
		## check conformity
		if len ( parsed_command["comm"] ) == "":
			raise "no command"
		
		if not ( parsed_command["comm"] in aviable_commands ):
			print ( "unnown command" + parsed_command ['comm'] )
			raise BaseException ( "Command error" )

		## find the turle
		Tartaruga = (self.turtles [ parsed_command["-t"] ]) # this wont give and error because the firs creaded turtle other than its name has the "" name
		
		## executes the draw command
		match parsed_command["comm"]:
			case "cross" :
				Tartaruga.draw_cross (
					parsed_command["-s"], ## size
					parsed_command["-c"], ## color
					parsed_command["-a"]  ## angle
				)
			case "rect"  :
				Tartaruga.draw_rect (
					parsed_command["-h"], ## heigth
					parsed_command["-w"], ## width
					parsed_command["-c"],
					parsed_command["-a"]			
				)
			case "squa"  :
				Tartaruga.draw_square (
					parsed_command["-s"], ## size
					parsed_command["-c"],
					parsed_command["-a"]		
				)
			case "tria"  :
				Tartaruga.draw_regular (
					parsed_command["-s"],
					3, ## the only regular polygon with 3 sides
					parsed_command["-c"],
					parsed_command["-a"]			
				)
			case "poly"  :
				Tartaruga.draw_regular (
					parsed_command["-s"], ## size
					parsed_command["-r"], ## sides
					parsed_command["-c"],
					parsed_command["-a"]		
				)

	def Command\
	( self, comm : str ) -> int:
		r"""uses the unix style commands and executes them: <comm1> && <comm2> && <comm3> ...
		
		# This function exposes the following commands:
		
		start [options] ( creates a new window only one can be active )
			options are:
			-n <string> name of the window
			-b <color> background color of the window
		
		turtle [options] name ( creates a new turtle with a name )
			-c <string> default color of the turtle
			-p <int> default pen width
		
		end [options] ( delets the selected entity if not selected closes everything )
			opsions are:
			-t <string> kills the named turtle
		
		move [options] dx dy ( this function moves the turtle -t or the default one )
			-a this arguments set the turle position to ( dx,dy ) by default new_pos = old_pos + ( dx,dy )
			-t <string> tartaruga 
		
		clear ( resets the state of the turtles clearing the screan )

		loop [option] ( waits for you to close the window )
	 		-w <string> window to wait if not set waits for the default one

		if provided with an annown command it will be passed to Draw_Command """

		parametri = [
			[ "-n", "-b", "-c", "-p", "-t", "-a", "-w" ],
			[ "-n", "str", "" ],
			[ "-b", "str", "lightgreen" ],
			[ "-c", "str", "red" ],
			[ "-p", "int", 10 ],
			[ "-t", "str", "" ],
			[ "-a", "NIL", "NON" ],
			[ "-w", "str", "" ],
		]
		aviable_commands = [
			"start",
			"turtle",
			"end",
			"move",
			"clear",
			"loop",
			"help"
		]

		## first turtle 2 name : name and ""
		commands = comm.split ( " && ")
		for command in commands:
			# print ( "parsing ", command )
			parsed_command = self.Parse_Arguments ( command, parametri )
			# print ( parsed_command )

			## check conformity
			if len ( parsed_command["comm"] ) == "":
				raise "no command"
			
			if not ( parsed_command["comm"] in aviable_commands ):
				self.Draw_Command ( command )
			
			## execute command
			match parsed_command ["comm"]:
				case "start" :
					Wi = Tartaruga.make_window (
						parsed_command["-b"],
						parsed_command["-n"]
					)
					self.window = Wi
					
				case "turtle" :
					Ta = Tartaruga.Tartaruga (
						parsed_command["-c"],
						parsed_command["-p"]
					)
					if ( self.turtles == {} ):
						self.turtles [
							""
						] = Ta

					self.turtles [
						parsed_command["arg1"]	
					] = Ta
				case "end" :
					self.window.clear ( )
					self.window.bye ( )
					self.windows = None
					self.turtles = { }
					pass

				case "move" :
					self.turtles[ parsed_command ["-t"] ].move (
						(int)(parsed_command["arg1"]),
						(int)(parsed_command["arg2"]),
						True if parsed_command["-a"] == "YES" else False
					)
					pass
				
				case "clear":
					self.window.clear ( )
					self.turtles = { }
					pass
				
				case "loop":
					self.window.mainloop ( )

				case "help":
					print ( r"""uses the unix style commands and executes them: <comm1> && <comm2> && <comm3> ...
		
# This function exposes the following commands:

start [options] ( creates a new window only one can be active )
	options are:
	-n <string> name of the window
	-b <color> background color of the window

turtle [options] name ( creates a new turtle with a name )
	-c <string> default color of the turtle
	-p <int> default pen width

end [options] ( delets the selected entity if not selected closes everything )
	opsions are:
	-t <string> kills the named turtle

move [options] dx dy ( this function moves the turtle -t or the default one )
	-a this arguments set the turle position to ( dx,dy ) by default new_pos = old_pos + ( dx,dy )
	-t <string> tartaruga 

clear ( resets the state of the turtles clearing the screan )

loop [option] ( waits for you to close the window )
	-w <string> window to wait if not set waits for the default one

if provided with an annown command it will be passed to Draw_Command """)
					print ( r"""---------- DRAW COMMANDS ----------
	Draws the selected thing
every command has the following options:
	-a \<int> set a rotation angle for the figure
	-c \<color> colors the figure
	-t \<name> draws with the specified turle by defaults uses the first

	the possible shapes are:
cross [option] ( draws a cross on screen )
	-s \<int> sets the cross size

rect [options] ( draws a rectangle )
	-h \<int> sets the rectangle heigth
	-w \<int> sets the rectangle width

squa [option] ( draws a square )
	-s \<int> size of the square

tria [options] ( draws a equlateral traingle )
	-s \<int> set the triangle with side s

poly [options] ( draws an regular polyong )
	-s \<int> set the poly side length
	-r \<int> set the poly sides

if are provided more arguments they will be ignored""")

if __name__ == "__main__":
	pippo = Controller ( )
	# pippo.windows[""] = draw.make_window ( )
	# pippo.turtles["giancarlo"] = draw.Tartaruga ( "red", 10 )
	# pippo.Draw_Command ( "cross -s 10 -c green -a 36 -t giancarlo" )
	pippo.Command ( "start && turtle giancarlo -p 3 && cross -s 30 -c green -a 36 -t giancarlo && move 60 50 -a && sqar" )