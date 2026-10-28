#BWT ALGORITHM

parola = (input("Inserisci la parola da cifrare: ")+"$")

rotazioni = []
for i in range(len(parola)):
    rotazioni.append(parola[i:] + parola[:i])
    print(rotazioni) #String Rotation
