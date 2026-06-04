import socket

HOST = '127.0.0.1'
PORTA = 3535

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((HOST, PORTA))

print("Conectado ao servidor!")

while True:
    mensagem = input("Cliente: ")

    cliente.send(mensagem.encode())

    if mensagem.lower() == "sair":
        break

    resposta = cliente.recv(1024)

    print("Servidor:", resposta.decode())