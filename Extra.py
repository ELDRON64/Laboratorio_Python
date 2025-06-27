#
# Extra.py
#
# Elia Castellarin
#
# 26 Giugno 2025
# 
# versione 1.0
# 
# palline che si muovo
#

import pygame

# pygame setup
pygame.init()
Window = pygame.display.set_mode((1280, 720))
Timer = pygame.time.Clock()

Box = [ 0,
	Window.get_width ( ),
	0,
	Window.get_height ( ) ]

Radius = 10
bouncy = 0.7

Balls = []
# spawn balls
for i in range ( 0, 100 ):
	Balls.append ( [ Radius*2 + i*Radius*2,
			 Window.get_height ( ) / 2, 
			 [ i*100, -i] ] )
	# the cordiantes are X, Y, velocoty X, velocty Y

def dot ( X, Y ):
	return X[0]*Y[0] + X[1]*Y[1]

def Update_Balls ( dt ):
	global Balls
	global Radius
	global Box
	global bouncy

	gravity = 98.1

	for Ball in Balls:
		# apply gravity
		Ball[2][1] += gravity * dt

		Ball[0] += Ball[2][0] * dt
		Ball[1] += Ball[2][1] * dt
		# apply collisions
		for Ball2 in Balls:
			if Ball2 == Ball:
				continue

			## calculate distance - Radius*2 using taxy for efficinecy
			d = pow ( Ball[0] - Ball2[0], 2 ) + pow ( Ball[1] - Ball2[1], 2 )
			d = pow ( d, 1/2 )

			if d < Radius*2:
				## apply reaction divided between the balls
				normal_vector = [ ( Ball[0] - Ball2[0] ) / d, ( Ball[1] - Ball2[1] ) / d ]

				d -= Radius * 2

				Ball[0] += normal_vector[0] * - d
				Ball[1] += normal_vector[1] * - d
				Ball2[0] += normal_vector[0] * d
				Ball2[1] += normal_vector[1] * d

				## apply velity reaction
				## velocity -= plane_normal * ( dot ( plane_normal, velocity ) ) * ( 1 + bouncy );
				dot_prod = dot ( normal_vector, Ball[2] )
				Ball[2][0] -= normal_vector[0] * dot_prod * ( 1 + bouncy )
				Ball[2][1] -= normal_vector[1] * dot_prod * ( 1 + bouncy )

				dot_prod = dot ( normal_vector, Ball2[2] )
				Ball2[2][0] -= normal_vector[0] * dot_prod * ( 1 + bouncy )
				Ball2[2][1] -= normal_vector[1] * dot_prod * ( 1 + bouncy )

		# make sure it is in the bounding box
		if Ball [0] - Radius < Box[0]:
			Ball[0] = ( Ball[0] - Radius ) * -1 + Radius
			Ball[2][0] *= -1
		if Ball [0] + Radius > Box[1]:
			Ball[0] = ( Ball[0] - Box[1] + Radius ) * -1 + Box [1] - Radius
			Ball[2][0] *= -1
		if Ball [1] - Radius < Box[2]:
			Ball[1] = ( Ball[1] - Radius ) * -1 + Radius
			Ball[2][1] *= -1
		if Ball [1] + Radius > Box[3]:
			Ball[1] = ( Ball[1] - Box[3] + Radius) * -1 + Box [3] - Radius
			Ball[2][1] *= -1

end = False
particles = []
particles_timer = 1
while not end:
	# check for closing
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			end = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			## check if collided with a ball is yes delete it if not spawn one
			for Ball in Balls:
				d = pow ( Ball[0] - pos[0], 2 ) + pow ( Ball[1] - pos[1], 2 )
				d = pow ( d, 1/2 )
				if d < ( Radius * 4 ):
					Balls.remove ( Ball )
					particles.append ( [ Ball[:2], particles_timer ])

			## add ball 
			Balls.append ( [pos[0],pos[1],[0,0]] )
	
	Window.fill ( "purple" )

	dt = Timer.tick ( ) / 500
	Update_Balls ( dt )

	## render balls
	for ball in Balls:
		pygame.draw.circle ( Window, "green", ball[:2], Radius )

	for part in particles:
		pygame.draw.circle ( Window, "red", part[0], Radius )
		part[1] -= dt
		if ( part[1] < 0 ):
			particles.remove ( part )

	# switch the back render with front one
	pygame.display.update()

pygame.quit()
