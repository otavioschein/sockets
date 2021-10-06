import socket
import time

PORT = 5051
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

commands = "\n/exit -> exit program.\n" \
           "/list -> list connected users.\n" \
           "/key -> commands.\n"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    print('===== WELCOME TO THE CHAT =====\n'
          'Type /key for help. Be polite and enjoy!')
    answer_username = input('\nEnter your name: ')

    connection = connect()
    send(connection, answer_username)
    while True:
        message = input("-> ")

        if message == '/key':
            print(commands)
            continue

        if message == '/exit':
            break

        send(connection, message)

        if connection.recv(1024).decode(FORMAT) == "BANNED":
            print("You are banned from the server for 10 seconds!")
            send(connection, "User is banned for 10 seconds!")
            time.sleep(10)

    send(connection, "DISCONNECTED")
    time.sleep(1)
    print('Disconnected')


start()
