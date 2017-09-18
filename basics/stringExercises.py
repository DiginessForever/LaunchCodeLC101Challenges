print('pineapple'<'Peach'):   #prints false do to sort order of strings - capital letters come before lower case, etc
print(‘Python’[1])
print(“Strings are sequences of characters.”[5])
print(len(“wonderful”))
print(‘Mystery’[:4])
print(‘p’ in ‘Pineapple’)
print(‘apple’ in ‘Pineapple’)
print(‘pear’ not in ‘Pineapple’)
print(‘apple’ > ‘pineapple’)
print(‘pineapple’ < ‘Peach’)
print('Horton hears a who'[4:8])

myString = 'Forescore and seven years ago'
for char in myString:
  print(char)
for char in range(0, myString):
  print(myString[char])
