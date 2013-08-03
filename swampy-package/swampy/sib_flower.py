# Flower excercise (4.2) from Week 0

# Name: Cassie Sancartier



# This is where you put code to move bob

from TurtleWorld import * 		
world = TurtleWorld()			 	
bob = Turtle()		
bob.delay = 0.0001	
from math import pi

def general_poly(turtle, length, sides, theta):
    for i in range(sides):
	fd(turtle, length)
	lt(turtle, theta)

def arc(turtle, radius, theta):	
	arc_length_degrees = 2 * radius * pi * theta / 360
	sides = 35
	segment_length = arc_length_degrees / sides
	segment_angle = theta / sides
	general_poly (turtle, segment_length, sides, segment_angle)

def petal(turtle, radius, theta):
	for i in range(2):
		arc(turtle, radius, theta)
		lt(turtle, 180 - theta)

def flower(turtle, radius, theta, petals):
	for i in range(petals):
		petal(turtle, radius, theta)
		lt(turtle, 360 / petals)

def move_flower(turtle, length):
	pu(turtle)
	turtle.heading = 0
	fd(turtle, length)
	pd(turtle)


			
flower(bob, 75.0, 65.0, 7)
move_flower(bob, 150)

flower(bob, 65.0, 65.0, 10)
move_flower(bob, 150)

flower(bob, 170.0, 25.0, 20)






wait_for_user()					

