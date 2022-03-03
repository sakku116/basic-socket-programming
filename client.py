import socket

PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# membuat koneksi dengan SERVER
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def sendToServer(msg):
    # mengirim pesan ke server
    client.send(msg.encode('utf-8'))

    recieve_msg = client.recv(2048).decode('utf-8')
    print(f"(server) : {recieve_msg}\n")

def start():
    print("###############################")
    print(f"[STARTING] connected to {ADDR}")
    print("> type 'DISCONNECT' to disconnect from server")
    print("############################### \n")

    while True:
        sendToServer(input("enter a message: "))

start()
