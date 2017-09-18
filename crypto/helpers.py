alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperAlphabet = ['A','B','C','D','E','F','G','H', 'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def rotate_character(character, rot):
	upper = False
	if character in upperAlphabet:
		upper = True
	position = alphabet_position(character)
	if position >= 0:
		position += rot
	else:
		return character
	if position >= 26:
		position = ((position + 1) % 26) -1

	#print("Returning new character at alphabet position: " + str(position))
	if upper:
		return upperAlphabet[position]
	else:
		return alphabet[position]

def alphabet_position(letter):
	letter = letter.lower()
	index = -1
	try:
		index = alphabet.index(letter)
		#I am not catching ValueError because if the letter is not in the alphabet above, index will remain -1, I return that.
	except:
		pass
	return index