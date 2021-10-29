import socket
import sys
import time
import threading

PORT = 5051
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
commands = ['/key', '/list', '/exit']
commands_print = "\n/exit -> exit program.\n" \
           "/list -> list connected users.\n" \
           "/key -> commands.\n"
dirty_words = ["fuck", "shit", "cock", "pussy"]


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(msg):
    message = msg.encode(FORMAT)
    connection.send(message)


def start_connection():
    print('===== WELCOME TO THE CHAT =====\n'
          'Type /key for help. Be polite and enjoy!')
    return connect()


def end_connection():
    send("DISCONNECTED")
    time.sleep(1)
    print('Disconnected')
    connection.close()
    sys.exit()


def receive_message():
    while True:
        received_message = connection.recv(1024).decode(FORMAT)

        if received_message == "get_username":
            send(input('Username:'))
            continue

        if received_message == "BANNED":
            send("User is banned for 10 seconds!\n")
            continue

        print(received_message)


def send_message():
    while True:
        message = input()

        if any(word in message for word in dirty_words):
            send("User is banned for 10 seconds!")
            time.sleep(10)
            continue

        if message == '/key':
            print(commands_print)
            continue

        if message == '/list':
            send('/list')
            continue

        if message == '/exit':
            end_connection()
            break

        if message not in commands:
            send(message)


connection = start_connection()
thread1 = threading.Thread(target=receive_message)
thread2 = threading.Thread(target=send_message)

thread1.start()
thread2.start()
