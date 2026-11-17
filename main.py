def bwt_algorithm(parola):
    #BWT ALGORITHM FUNCTION

    parola = (parola+"$")

    rotazioni = []
    for i in range(len(parola)): #a For cycle with the length of the word, it outputs all the possible rotations of a word
        rotazioni.append(parola[i:] + parola[:i]) #takes the firts part of the word,from the index i to the end of it (excluding the character at index "i") , adding the first character of the word to the end of the new word, "appending" it to the list 'rotazioni'.

    # Sorting the rotations manually with bubble sort

    for i in range(len(rotazioni)): #a For cycle with the length of the list 'rotazioni'
        for j in range(len(rotazioni) - 1 - i): #another For cycle with the length of the list 'rotazioni' minus 1 and minus the index of the first For cycle, the requirement of the bubble sort.
            if rotazioni[j] > rotazioni[j + 1]: #Sorts the list "alphabetically", taking the ascii value of the words.
                rotazioni[j], rotazioni[j + 1] = rotazioni[j + 1], rotazioni[j] #if the condition is true, the position of the two words if exchanged

    #From now on the list 'rotazioni' is sorted alphabetically, the BWT algorithm can continue.

    bwt = "" #create the variable that will contain the last letters of the sorted rotations
    for rotazione in rotazioni: #For-Each that takes each word in the list of sorted rotations
        bwt += rotazione[-1] #Takes the last letter of each word and adds it to the new word.

    return bwt #Returns the new word that contains the last letters of the sorted rotations, in this case for the server to transmit to the client.