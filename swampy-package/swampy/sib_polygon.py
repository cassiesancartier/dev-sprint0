# Polygon excercise from Week 0

# Name: Cassie Sancartier

from TurtleWorld import * 	
from math import pi	
world = TurtleWorld()			
bob = Turtle()		
bob.delay = 0.01		

# This is where you put code to move bob

# Exercise 2

def general_poly(turtle, length, sides, theta):
	for i in range(sides):
		fd(turtle, length)
		lt(turtle, theta)


def square(turtle, length):
    general_poly(turtle, length, 4, 90)


def polygon(turtle, length, sides):
	theta = 360 / sides
    general_poly(turtle, length, sides, theta)


def circle(turtle, radius):
	arc(turtle, radius, 360)


def arc(turtle, radius, theta):	
	arc_length_degrees = 2 * radius * pi * theta / 360
	sides = 35
	segment_length = arc_length_degrees / sides
	segment_angle = theta / sides
	general_poly (turtle, segment_length, sides, segment_angle)
	

square(bob, 100)

polygon(bob, 75, 6)

circle(bob, 60)

arc(bob, 100, 50)


wait_for_user()					
