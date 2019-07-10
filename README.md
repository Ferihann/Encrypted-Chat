# Encrypted-Chat

This chat application simply makes messaging secure . RSA algorithm was used for encryption and decryption operation and socket programming was used for communication. According to RSA algorithm , both two messager(client and server) have 2 keys one is public and the other one is private . 

Firstly , public keys are swapped between server and client .Then ,when client want to  send message to the server , client encrypt its message with server's public key and send it. Encrypting message that comes to the server can be only solved by server since only server's private key solves this message . In the same way when server sends message , it encrypts with client public key.

As a result , messaging is made more secure with that method , even anyone reach messages , he/she can not solve because of the not having private keys

![Alt Text](https://github.com/Ferihann/Encrypted-Chat/blob/master/Screenshot%20from%202019-07-10%2009-03-30.png)

![Alt Text](https://github.com/Ferihann/Encrypted-Chat/blob/master/Screenshot%20from%202019-07-10%2009-03-06.png)
