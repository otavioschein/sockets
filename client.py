import socket
import time

PORT = 5051
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

commands = "\n/exit -> sai do programa.\n" \
           "/list -> lista usuários conectados.\n" \
           "/key -> comandos possíveis.\n"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    answer_username = input('Enter your name: ')

    connection = connect()
    send(connection, answer_username)
    while True:
        message = input()

        if message == '/key':
            print(commands)
            continue

        if message == '/exit':
            break

        send(connection, message)

    send(connection, "DISCONNECTED")
    time.sleep(1)
    print('Disconnected')


start()
