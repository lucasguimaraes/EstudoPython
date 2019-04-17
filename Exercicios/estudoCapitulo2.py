import os

linha1 = 'mama mia '
linha2 = 'let me go '

def print_twice(bruce):
	print(bruce)
	print(bruce)


def concatena(parte1, parte2):
	concat = parte1+ parte2
	print_twice(concat)


concatena(linha1, linha2)

os.system("PAUSE")