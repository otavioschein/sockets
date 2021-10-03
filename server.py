import threading
import socket

PORT = 5051
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()
users_connected = []


def handle_client(conn, addr):
    user_connected = conn.recv(1024).decode(FORMAT)
    users_connected.append(user_connected)
    print(f"[NEW CONNECTION] {user_connected} Connected")

    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMAT)
            if not msg:
                break

            if msg == "DISCONNECTED":
                users_connected.remove(user_connected)
                connected = False

            print(f"{user_connected}: {msg}")

            if msg == '/list':
                print("\nUsers connected to the server:")
                for uc in users_connected:
                    print(f"    - {uc}")

            with clients_lock:
                for c in clients:
                    c.sendall(f"{user_connected}: {msg}".encode(FORMAT))

    finally:
        with clients_lock:
            clients.remove(conn)

        conn.close()


def start():
    print('[SERVER STARTED]!')
    server.listen()
    while True:
        conn, addr = server.accept()
        with clients_lock:
            clients.add(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


start()
