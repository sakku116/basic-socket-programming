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

# mmembuat server dan memulainya pada SERVER
my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (family, type)
my_server.bind(ADDR)

def handle_client(conn, addr):
    '''
    # SEND and RECIEVE

    ## .recv('argument') berisi panjang buffer berupa int, kemudian .decode('[format semisal utf-8]')
        karena .recv() akan menerima data sebagai bit, dan perlu decode menjadi format yang ditentukan

    ## .send('argument') berisi string sebagai data, kemudian string tersebut juga harus
        di .encode('[format semisal utf-8]') sebelum dikirim,
        (encode berarti mengubah string tersebut *dari* format yang ditentukan menjadi bit)
        karena .send() harus berisi object bit
    '''

    print(f"[NEW CONNECTION] {addr} conneceted")
    connected = True

    while connected:
        # menerima message
        message = conn.recv(100).decode('utf-8')

        if message == "DISCONNECT":
            # jika msg berisi "DISCONNECT",
            # maka while akan berhenti,
            # dan menutup hubungan.

            # mengirim callback disconnected ke client
            conn.send("you have been disconnected".encode('utf-8'))

            print(f"[DISCONNECT] {addr} disconnected")
            connected = False # break while loop

        else:
            # print message
            print("---------------------------")
            print(f"{addr} : {message}\n")
            # mengirim pesan callback kepada client
            conn.send("message recieved".encode('utf-8'))

    conn.close()

# main
def start():
    print("###############################")
    print("[STARTING] server is starting....")

    my_server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    print("############################### \n")

    while True:
        conn, addr = my_server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # (args=) akan me pass argument
        thread.start()

        # print proses yang berjalan dalam threading
        print(f"[CURRENT ACTIVE CONNECTION] {threading.activeCount() - 1}")

start()
