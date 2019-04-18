import os

def do_twice(f, value):
	f(value)
	f(value)

def print_twice(arg):
	print(arg)
	print(arg)	

def do_four(do_twice, value):
	do_twice(value)
	do_twice(value)

do_twice(print_twice, 'spam')
print(' ')	
do_four(print_twice, 'spam')


os.system("PAUSE")