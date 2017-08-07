import itertools

plain  = 'Hello World'
cipher = 'testt estte'

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

def encrypt(message, key):
	encrypted = ""
	for num in range(0, len(message)):
		messageCh = message[num].lower()
		keyCh = key[num].lower()
		index1 = alphabet.index(messageCh)
		index2 = alphabet.index(keyCh)
		new_index = (index1 + index2) % len(alphabet)
		encrypted = encrypted + alphabet[new_index]
	return encrypted

def decrypt(cipher, keylength):
	keyguesses = [''.join(i) for i in itertools.product(alphabet, repeat = keylength)]
	for key in keyguesses:
		attemptedDecrypt = encrypt(
		if encrypt(key, cipher)
		#print(encrypt(cipher, key))

def main():
	encrypted = encrypt(plain, cipher)
	print("Encrypted message: " + encrypted)
	print("Decrypting...")
	decrypt(cipher, 4)

if __name__ == "__main__":
	main()