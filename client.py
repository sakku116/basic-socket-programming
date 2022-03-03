import socket

PORT = 8080
SERVER ='192.168.10.6'
ADDR = (SERVER, PORT)

# membuat koneksi dengan SERVER
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def sendToServer(msg):
    # mengirim pesan ke server
    client.send(msg.encode('utf-8'))

    recieve_msg = client.recv(128).decode('utf-8')
    print(f"(server) : {recieve_msg}\n")

def start():
    print("###############################")
    print(f"[STARTING] connected to {ADDR}")
    print("> type '-disconnect' to disconnect from server")
    print("############################### \n")

    while True:
        input_msg = input("enter a message: ")
        
        if input_msg == "!disconnect":
            sendToServer(input_msg)
            exit()
        else:
            sendToServer(input_msg)

start()
