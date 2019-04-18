import os

def desenha_linha_mais():
	print('+', '-', '-', '-', '-', '+', '-', '-', '-', '-',  '+')

def desenha_linha_coluna():
	print('|', ' ', ' ', ' ', ' ', '|',  ' ', ' ', ' ', ' ', '|')	

def prints_four(f):
	f()
	f()
	f()
	f()


desenha_linha_mais()
prints_four(desenha_linha_coluna)
desenha_linha_mais()
prints_four(desenha_linha_coluna)
desenha_linha_mais()

os.system("PAUSE")