import os

def adicionaEspacoEmBranco(cont):
	while cont >= 0:
		cont -= 1		
		print(' ', end='')

def right_justify(s):
	tamanho_palavra = len(s)
	espaco_em_branco = 70 - tamanho_palavra
	adicionaEspacoEmBranco(espaco_em_branco)
	print(s)	

right_justify('Morrienmaoseipqqq')

os.system("PAUSE")	