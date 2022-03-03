import socket
import sys

'''
masukkann argument pada command line berupa ip_address yang digunakan server
'''

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

if __name__ == "__main__":
    try:
        # mendapatkan ip address dari argument
        SERVER = sys.argv[1]
        PORT = 8080
        ADDR = (SERVER, PORT)

        # membuat koneksi dengan SERVER
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        start()
        
    except:
        print('[ADDR ERROR] please enter the ip_address argument that server running in')
        exit()

