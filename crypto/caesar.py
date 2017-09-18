import sys #Going to check the version and use the appropriate input() method
			#Python2 does not handle eof characters correctly and you must use raw_input() instead
			#Python3 has corrected this, and I'll just use input() in that case

from helpers import *

def encrypt(text, rot):
	encryptedMessage = ''
	for char in text:
		encryptedMessage += rotate_character(char, rot)
	return encryptedMessage

def main():
	#The commented out lines are unit tests.
	#print("A, 0 : " + rotate_character('A', 0))
	#print("A, 1 : " + rotate_character('A', 1))
	#print("A, 26 : " + rotate_character('A', 26))
	#print("A, 27 : " + rotate_character('A', 27))
	#print("a, 0 : " + rotate_character('a', 0))
	#print("a, 1 : " + rotate_character('a', 1))
	#print("a, 26 : " + rotate_character('a', 26))
	#print("a, 27 : " + rotate_character('a', 27))
	#print("Hello, World (0) : " + encrypt("Hello, world!", 0))
	#print("Hello, World (26) : " + encrypt("Hello, world!", 26))
	#print("Hello, World (1) : " + encrypt("Hello, world!", 1))
	#print("Hello, World (27) : " + encrypt("Hello, world!", 27))

	#print("Take me to your leader! (13) : " + encrypt("Take me to your leader!", 13))
	#print("Resistance is futile (13) : " + encrypt("Resistance is futile", 13))

	message = ''
	rotate = 0
	if (int(sys.version[0]) == 3):
		message = input("Type a message:")
		rotate = int(input("Rotate by:"))
	else:  #Assuming that if Python version is not 3, it's 2...
		message = raw_input("Type a message:")
		rotate = int(raw_input("Rotate by:"))
	print(encrypt(message, rotate))

if __name__ == "__main__":
	main()