import time, socket, sys
from rsa import Rsa
import pickle

print("\nWelcome to Chat \n")
print("Initialising....\n")
time.sleep(1)

client_socket = socket.socket()   # Open a socket for client
hostt = socket.gethostname()      # Take host from socket
ip = socket.gethostbyname(hostt)  # Take ip
print(hostt, "(", ip, ")\n")
host = ip
name = input(str("\nEnter your name: "))
port = 1236
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
client_socket.connect((host, port))  # Client connect to server
print("Connected...\n")

client_socket.send(name.encode())  # Client send its name to the server
server_name = client_socket.recv(1024)  # Clients receive the server name
server_name = server_name.decode()
print(server_name, "has joined the chat room\nEnter [e] to exit chat room\n")

client_socket.send("Server name is confirmed \n".encode())
message = client_socket.recv(1024)  #Server waits client's public key

# Ciphering for client
ciphering = Rsa()
ciphering.generate_prime(200, 300)
clientPublic, clientPrivate = ciphering.generate_public_and_private_key()
print("Client public key is ", clientPublic, " client private key is : ", clientPrivate)

# Client sends its private key
clientPublic = pickle.dumps(clientPublic)
client_socket.sendall(clientPublic)
client_socket.recv(1024)

# Client send request for taking server's public key
client_socket.send("Server please send public key ? ".encode())
# Server send its public key
server_public_key = client_socket.recv(1024)
server_public_key = pickle.loads(server_public_key)
print("Server public key is :", server_public_key, "\n\n")


while True:
    message = client_socket.recv(1024)  # Takes the server ciphering message
    message = message.decode()
    print(server_name, "\t:(Encrypted)=>\t", message, "Decrypting message is =>", ciphering.decrypt(clientPrivate, message)) # Solves the message
    message = input(str("Me:\t"))
    message = ciphering.encrypt(server_public_key, message)  # Server encrypt the its message and solved it
    if message == "[e]":
        message = "Left chat room!"
        client_socket.send(message.encode())
        print("\n")
        break
    client_socket.send(message.encode())
