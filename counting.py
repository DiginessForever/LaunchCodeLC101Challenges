def countCharsInString(string):
	'''take in a string, get a count of each unique character's occurrences, print these all out'''
	#Thank you to the submitter of the answer here:
	#https://stackoverflow.com/questions/26579392/sorting-string-values-according-to-a-custom-alphabet-in-python
	
	dict = {}
	for char in string:
		if char in dict:
			dict[char] += 1
		else:
			dict[char] = 1
	#print('Not sorted: ' + str(dict.items()))
	#print('Yes sorted: ' + str(sorted(dict.items())))
	#for key,value in sorted(dict.items()):
	#	print(key + " : " + str(value))

	#Create a sorted list of the sorted key/value pairs in the dictionary
	alphabet="@#$%^&*()/*+,.?!-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'"
	sortedList = sorted(dict, key=lambda word: [alphabet.index(c) for c in word])
	for word in sortedList:
		print(word + ' : ' + str(dict[word]))

def main():
	str = input('Give me a string:\n')
	countCharsInString(str)

if __name__ == "__main__":
	main()
