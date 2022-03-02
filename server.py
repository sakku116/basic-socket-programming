'''
ini adalah latihan pertama socket programming menggunakan python.
server ini akan berjalan di jaringan local (satu koneksi).
jadi, client.py dapat dijalankan pada device berbeda dengan koneksi sama.
'''

import socket
import threading

PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname()) # mendapat ipv4 address otomatis
ADDR = (SERVER, PORT)
# untuk keperluan buffer
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (family, type)
my_server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} conneceted")

    connected = True

    while connected:
        # menerima message
        msg_length = conn.recv(HEADER).decode(FORMAT) # secara default dia berupa bit, dan harus di decode

        # saat pertama kali dijalankan msg_length berisi None
        if msg_length: # if not None
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                '''
                jika msg berisi "DISCONNECT",
                maka while akan berhenti,
                dan menutup hubungan
                '''
                conn.send("you have been disconnected".encode(FORMAT))
                connected = False

            # mengirim pesan kembai kepada client
            conn.send("msg recieved".encode(FORMAT))
            print(f"{addr} : {msg}")

        else:
            pass

    conn.close()

# main
def start():
    my_server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = my_server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # (args=) akan me pass argument
        thread.start()

        # print proses yang berjalan dalam threading
        print(f"[ACTIVE CONNECTION] {threading.activeCount() - 1}")

print("[STARTING] server is starting....")
start()
