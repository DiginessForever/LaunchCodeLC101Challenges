import sys #Going to check the version and use the appropriate input() method
			#Python2 does not handle eof characters correctly and you must use raw_input() instead
			#Python3 has corrected this, and I'll just use input() in that case

from helpers import *

def encrypt(message, key):
	'''This method uses rotate_character & alphabet_position methods from helpers.py to perform viginere cypher using
		a key, meaning each position of the message is rotated by a different amount, according to the rotation of
		the key letter at that position.
		For further info, watch this CS50 description of the viginere cypher:
		https://www.youtube.com/watch?v=9zASwVoshiM&feature=youtu.be
	'''
	encryptedMessage = ''
	count = 0
	for char in message:
		if char in alphabet or char in upperAlphabet:
			rotation = alphabet.index(key[count % len(key)].lower())
			encryptedMessage += rotate_character(char, rotation)
			count += 1
		else:
			encryptedMessage += char
	return encryptedMessage

def getInput(prompt):
	inputMessage = ''
	if (int(sys.version[0]) == 3):
		inputMessage = input(prompt)
	else:  #Assuming that if Python version is not 3, it's 2...
		inputMessage = raw_input(prompt)
	return inputMessage

def clean(key):
	'''This removes any non-alpabetic characters from the key'''
	newKey = ''
	for char in key:
		if char in alphabet or char in upperAlphabet:
			newKey += char

	return newKey

def main():
	from sys import argv
	message = ''
	key = ''
	#print("This is what the user typed on the command line:", argv)
	if (len(argv) > 1) and argv[1].lower() == "help":
		print("To specify the message and key from the command line, \nput both in quotes separated by a space: for example:\npython vigenere.py 'Hello World!' 'bacon'\n'Hello World!' is the first argument and is the message to encrypt.\n'bacon' is the second argument and is the key to use to encrypt.\nAny digits will be removed from the key before it is used.")
		quit()
	if (len(argv) == 3):
		message = argv[1]
		key = argv[2]
	elif (len(argv) != 1):
		print("To specify the message and key from the command line, put them in quotes in that order, both surrounded by quotes, with a space between them")
	if message == '' and key == '':
		message = getInput("Type a message:")
		key = getInput("Encryption key:")

	key = clean(key)
	print("message: " + message + "\nkey: " + key)
	print(encrypt(message, key))

if __name__ == "__main__":
	main()

#Unit tests:
#print(encrypt("Hello, World!", "bacon"))
#print(encrypt("Hello, World!", "AAAA"))  #This is rotating the entire string by 0 - 
										  #you get the same string because A's alphabet position is 0.
#print(encrypt("Hello, World!", "ZZZZ"))  #The key is not case sensitive, giving uppper case will not influence results.
										  #Z rotates by 25 (or -1)
#print(encrypt("Hello, World!", "BBBB"))  #I remember the rotation of 1 result quite well, or I'll know it when I see it.

