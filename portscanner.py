import socket
import threading
from queue import Queue


alvo = input("Digite o alvo\n")
portas = range(1,int(input("Digite o intervalo de portas\n"))+1)
fila = Queue()
portas_abertas = []


def varredordeporta(porta):
	s = socket.socket()
	try:
		s.connect((alvo, porta))
		return True
	except:
		return False

def preencher_fila(portas):
	for porta in portas:
		fila.put(porta)

def trabalhador():
	while not fila.empty():
		porta = fila.get()
		if varredordeporta(porta):
			print(f'A porta {porta} está aberta.')
			portas_abertas.append(porta)
		
preencher_fila(portas)

threads = []

for t in range(100):
	thread = threading.Thread(target=trabalhador)
	threads.append(thread)

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()

print('As portas abertas são',portas_abertas)


