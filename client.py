import socket

HEADER = 64
PORT = 8080
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

DISCONNECTED_STATE = False

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    # mengirip pesan ke server
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)

    recieve_msg = client.recv(2048)
    print(recieve_msg)

while DISCONNECTED_STATE == False:
    send(input("enter a message: "))
