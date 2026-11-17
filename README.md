# Burrows-Wheeler Transform in Python

This personal project is an introduction to the Burrows-Wheeler Transform (BWT), a method of rearranging text that can make it easier to compress.

V1.0:
This version of the program asks the user for a word, adds `$` as an end-of-text marker, and displays rotations of the resulting string.
It focuses on illustrating this rotation step, while a complete BWT also sorts the rotations and takes the last character from each row to produce the transformed text.

V2.0:
This version of the program includes the sorting of the list of rotations, and at last takes the last character of every rotation, forming the encoded word

# SOCKET Server and Client
V3.0:
Creation of the files "client.py" and "server.py", 2 sockets that send data to eachother (in this case a string that the server transforms in a "encoded" string, sending it back to the client).
The new version of the entire script consists in the "trasformation" of the "main.py" file in a function, so that the script "server.py" can recall the function in order to trasform the string passed by the client.
The 2 sockets use TCP and IPv4 protocols, assuring the arrival of all the data that the client and server send to eachother.