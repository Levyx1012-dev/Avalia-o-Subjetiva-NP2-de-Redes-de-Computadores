import socket

HOST = '0.0.0.0'
PORTA = 3535

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((HOST, PORTA))

servidor.listen()

print(f"Servidor sendo executado na porta {PORTA}...")

cliente, endereco = servidor.accept()

print(f"Conexão recebida de {endereco}")

while True:
    mensagem = cliente.recv(1024)

    if not mensagem:
        break

    texto = mensagem.decode()

    if texto.lower() == "sair":
        print("Cliente encerrou a conexão.")
        break

    print(f"Cliente: {texto}")

    resposta = input("Servidor: ")
    cliente.send(resposta.encode())