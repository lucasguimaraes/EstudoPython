import turtle

bob = turtle.Turtle()

def square(t, lenght, n):
	#for i in range(4):
		t.fd(lenght)
		t.lt(n)
		t.fd(lenght)
		t.lt(n)
		
def polygon(t, lenght, n):
	for i in range(4):
		t.fd(lenght)
		t.lt(lenght)
		t.fd(n)	

square(bob, 90, 70)
##polygon(bob, 70, 90)

turtle.mainloop()