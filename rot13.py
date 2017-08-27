alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperAlphabet = ['A','B','C','D','E','F','G','H', 'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']

def rot13(message):
	encryptedMessage = ''
	newChar = ''
	for char in message:
		upper = False
		if char in upperAlphabet:
			char = char.lower()
			upper = True
		try:
			index = alphabet.index(char)
		except ValueError:
			index = -1
		if index >= 0:
			index += 13
			if index > 26:
				index = index % 26
			#print("index after modulo: " + str(index))
			newChar = alphabet[index - 1]
			if upper:
				newChar = newChar.upper()
			encryptedMessage += newChar
		else:
			encryptedMessage += char
	return encryptedMessage

def main():
	print("Hello, world!" + " : " + rot13("Hello, world!"))
	print("Take me to your leader.  : " + rot13("Take me to your leader."))
	print("Resistance is futile : " + rot13("Reistance is futile"))	

if __name__ == "__main__":
	main()