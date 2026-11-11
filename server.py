import socket as sck
import main

IP = "127.0.0.1"
PORT = 5090

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as server:
    server.bind((IP, PORT))
    server.listen(5)

    print("Server in ascolto su " + IP + ":" + str(PORT))

    with server.accept()[0] as client:
        print("Connessione accettata da " + str(client.getsockname()))
        data = client.recv(1024)
        parola = data.decode()
        print("Dati ricevuti dal client:", parola)
        bwt_result = main.bwt_algorithm(parola)
        client.sendall(bwt_result.encode())
        print("Dati inviati al client:", bwt_result)
        
print("Chiusura connessione")
    
