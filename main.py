def bwt_algorithm(parola):
    #BWT ALGORITHM

    parola = (parola+"$")

    rotazioni = []
    for i in range(len(parola)): #For with the length of the word, it outputs all the possible rotations of a word
        rotazioni.append(parola[i:] + parola[:i]) #takes the from the index i to the end of the word , adding the rest of the word excluding the character at index i

    # Sorting the rotations manually with bubble sort

    for i in range(len(rotazioni)): #For with the length of the list
        for j in range(len(rotazioni) - 1 - i): 
            if rotazioni[j] > rotazioni[j + 1]: #Sorts the list alphabetically
                rotazioni[j], rotazioni[j + 1] = rotazioni[j + 1], rotazioni[j] #if the condition is true, the position of the two words if exchanged

    bwt = "" #create the word that will contain the last letters of the sorted rotations
    for rotazione in rotazioni: #For-Each that takes each word in the list of sorted rotations
        bwt += rotazione[-1] #Takes the last letter of each word and adds it to the new word, Note: the list is already sorted 

    return bwt #Returns the new word that contains the last letters of the sorted rotations