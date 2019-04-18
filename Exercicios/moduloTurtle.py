import turtle

bob = turtle.Turtle()
bob.color('red', 'yellow')
bob.begin_fill()
while True:
	bob.fd(200)
	bob.lt(170)
	if abs(bob.pos()) < 1:
		break
bob.end_fill()
turtle.mainloop()
