import pickle
import time, socket, sys
from rsa import Rsa

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

#  Same operations like in client
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1236
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

# Client sends its name to the server
client_name = conn.recv(1024)
client_name = client_name.decode()
print(client_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
conn.send(name.encode())

#  Clients inform server to taking server's name
text = conn.recv(1024)
text = text.decode()

# Request the public key from client
conn.send("\n Client please send your public key for encryption".encode())
client_public_key = conn.recv(4096)
client_public_key = pickle.loads(client_public_key)
print("\n Client public is : ", client_public_key)

conn.send("Clientın public keyş alındı.".encode())  # Inform taking the private key of client
message2 = conn.recv(1024) # Client request the server key


# Public and private keys generated
ciphering = Rsa()
ciphering.generate_prime(100, 300)
serverPublic, serverPrivate = ciphering.generate_public_and_private_key()
print("Server public key : ", serverPublic, "Server private key is : ", serverPrivate, "\n\n")

# Server sends its public key to the client
serverPublic = pickle.dumps(serverPublic)
conn.sendall(serverPublic)

while True:
    message = input(str("Me :\t"))
    message = ciphering.encrypt(client_public_key, message) # Encrypt server message with client's public key
    if message == "[e]":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode()) # Sends ciphertext to the client
    message = conn.recv(1024)   # Takes the coming ciphering message from client
    message = message.decode()
    print(client_name, ":\t", "(Encrypted)=>", message, "\t(Decrypted)=>", ciphering.decrypt(serverPrivate, message)) #Solves the crypted message


