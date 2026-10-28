#BWT ALGORITHM

parola = (input("Inserisci la parola da cifrare: ")+"$")

for i in range(len(parola)):
    parola = parola[i:] + parola[:i]
    print(parola) #String Rotation
