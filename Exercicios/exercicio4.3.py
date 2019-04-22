import turtle
import math

bob = turtle.Turtle()
alice = turtle.Turtle()

def square(t, lenght, n):
	for i in range(4):
		t.lt(n)
		t.fd(lenght)
		t.fd(lenght)
		t.lt(n)
		
def polygon(t, lenght, n):
	angle = 360.0/n
	for i in range(n):
		t.fd(lenght)
		t.lt(angle)

def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = angle / n
	for i in range(n):
		t.fd(step_length)
		t.lt(step_angle)

def circle(t, r):
	circumference = 2 * math.pi * r
	n = int(circumference / 3 ) + 1
	lenght = circumference / n
	polygon(t, lenght, n)


#square(bob, lenght=90, n=70)
#square(n=20, lenght=40, t=alice)
#polygon(alice, 29, 20)
#circle(bob, r=100)
arc(bob, 100, 100)
turtle.mainloop()