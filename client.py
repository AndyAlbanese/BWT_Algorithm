import socket as sck

IP = "127.0.0.1"
PORT = 5090

message = input("Inserisci la parola da cifrare: ")

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as client:
    client.connect((IP, PORT))
    print ("Connesso al server")
    client.sendall(message.encode())
    data = client.recv(1024)
    print("Dati ricevuti dal server:", data.decode())

print("Chiusura connessione")
