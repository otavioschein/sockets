import threading
import socket

PORT = 5051
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []
clients_lock = threading.Lock()
users_connected = []


def handle_global_message(username, message):
    for c in clients:
        c.sendall(f"{username}: {message}".encode(FORMAT))


def handle_list_command(username):
    string = "\nUsers connected: "
    for uc in users_connected:
        string += ''.join(f"\n      - {uc}")
    # conn.send(string.encode(FORMAT))
    handle_global_message(username, string)


def handle_message(conn, addr, username):
    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMAT)
            if not msg:
                break

            if msg == "DISCONNECTED":
                connected = False

            if msg == '/list':
                handle_list_command(username)

            print(f'{username}: {msg}')

            with clients_lock:
                handle_global_message(username, msg)

    finally:
        with clients_lock:
            clients.remove(conn)
            users_connected.remove(username)

        conn.close()


def start():
    print('[SERVER STARTED] ===== THE CHAT =====')
    server.listen()
    while True:
        # espera por uma nova conexão
        conn, addr = server.accept()
        with clients_lock:
            clients.append(conn)
        conn.send('get_username'.encode(FORMAT))
        username = conn.recv(1024).decode(FORMAT)
        users_connected.append(username)
        handle_global_message(username, f"[NEW CONNECTION] {username} Connected.\n")
        thread_message = threading.Thread(target=handle_message, args=(conn, addr, username))
        thread_message.start()


start()
