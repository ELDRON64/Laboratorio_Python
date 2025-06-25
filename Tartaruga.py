import turtle
import numpy as np

def make_window\
( bkg_color = "lightgreen", title = "hoholero" ):
    """Crea una finestra con background e titolo e ritorna la nuova finestra"""
    new_window = turtle.Screen()
    new_window.bgcolor(bkg_color)
    new_window.title(title) 
    return new_window

class Tartaruga :
	def __init__\
    ( self, color : str, pen_size : int ):
		"""Crea una nuova tartaruga.
		Dato un colore e dimensione del tratto"""  
		self.color = color
		self.pen_size = pen_size
		## inizialization
		T = turtle.Turtle ( )
		T.shape ( 'turtle' )
		T.color ( color )
		T.pensize ( pen_size )
		T.setheading ( 90 ) # face up
        
		self.turtle = T

	def reset\
    ( self ) -> None:
		"""Resetta la tartaruga al suo stato iniziale"""
		self.turtle.reset ( )
		self.turtle.color ( self.color )
		self.turtle.pensize ( self.pen_size )
		self.turtle.setheading ( 90 ) # face up
	
	def move\
	( self, x : int, y :int, absolute : bool = False ) -> None:
		"""Muove la tartuaruga"""
		if absolute:
			self.turtle.penup ( )
			self.turtle.goto ( x, y )
			self.turtle.pendown ( )
			return

		self.turtle.penup ( )
		self.turtle.forward ( -y )
		self.turtle.left ( 90 )
		self.turtle.forward ( x )
		self.turtle.right ( 90 )
		self.turtle.pendown ( )
	
	def draw_cross\
	( self, size = 10, color = "_", angle = 0 ) -> None:
		"""Disegna una croce di lato s, centrata alla attuale posizione"""
		if not color == "_":
			self.turtle.color ( color ) # color

		self.turtle.setheading ( 90 - angle ) # face up ( rotata clockwise )
		
		## centering routine
		delta_pos = [size/2,3*size/2]
		self.move ( delta_pos[0], delta_pos[1] )
		
		## drawing routine
		for _ in [0,1,2,3]:
			self.turtle.forward ( size )
			self.turtle.left ( 90 )
			self.turtle.forward ( size )
			self.turtle.right ( 90 )
			self.turtle.forward ( size )
			self.turtle.right ( 90 )

		## reset position
		self.move ( -delta_pos[0], -delta_pos[1] )

	def draw_rect\
	( self, h = 10, w = 10, color = "_", angle = 0 ) -> None:
		"""Disegna un rettangolo di altezza (da alto a basso) h e larghezza ( da dx a sx ) w"""
		if not color == "_":
			self.turtle.color ( color ) # color
		self.turtle.setheading ( 90 - angle ) # face up ( rotata clockwise )

		## centering routine
		delta_pos = [-w/2,h/2]
		self.move ( delta_pos[0], delta_pos[1] )

		for _ in [0,1]:
			self.turtle.forward ( h )
			self.turtle.left ( 90 )
			self.turtle.forward ( w )
			self.turtle.left ( 90 )
	
		## reset position
		self.move ( -delta_pos[0], -delta_pos[1] )

	def draw_regular\
	( self, s = 30, sides = 3, color = "_", angle = 0 ) -> None:
		"""draws a regular polygon with side = s"""
		s = s / np.sin ( 360/sides )

		if not color == "_":
			self.turtle.color ( color ) # color

		## generate point cloud
		pos = self.turtle.pos ( )

		points = []
		for spichio in range (0,sides):
			ang = np.deg2rad ( 360/sides * spichio + angle )
			point = [ np.sin ( ang )*s+pos[0], np.cos ( ang )*s +pos[1] ]
			points.append ( point )
		
		## start at last point
		self.turtle.penup ( )
		self.turtle.goto ( points[len(points)-1][0], points[len(points)-1][1] )
		self.turtle.pendown ( )

		## print ( points )

		## connect points
		for point in points:
			self.turtle.goto ( point[0],point[1] )
		
		self.move (pos[0],pos[1],True)

	def draw_square\
	( self, s = 10, color = "_", angle = 0 ) -> None:
		self.draw_rect ( s, s, color, angle )

if __name__ == "__main__":
	ww = make_window ( )
	aa = Tartaruga ( "green", 10 )
	aa.draw_cross ( 40,angle=30 )
	aa.reset ( )
	aa.draw_regular ( sides= 5, angle = 0 )

	ww.mainloop ( )