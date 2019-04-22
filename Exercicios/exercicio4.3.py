import turtle

bob = turtle.Turtle()

def square(t, lenght, n):
	#for i in range(4):
		t.fd(lenght)
		t.lt(n)
		t.fd(lenght)
		t.lt(n)
		
def polygon(t, lenght, n):
	for i in range(n):
		angle = 360.0/n
		t.fd(lenght)
		t.lt(angle)

##square(bob, 90, 70)
polygon(bob, 52, 7)

turtle.mainloop()