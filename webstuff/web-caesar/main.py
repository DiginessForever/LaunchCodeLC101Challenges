from flask import Flask, request

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

app = Flask(__name__)
app.config['DEBUG'] = True

htmlBegin = '''
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
'''

rot = 0
message = ""
form = '''
	<form method="POST" action="/encrypt">
		Rotate By<input type="text" name="rot" value="{rot:d}"/>
		<input type="textarea" name="text" value="{text:s}"/>
		<input name="encryptButton" type="submit" text="Submit Query" />
	</form>
'''

htmlEnd = '''
</body>
</html>
'''


@app.route("/")
def index():
    return htmlBegin + form.format(rot=rot, text=message) + htmlEnd
    response_html

@app.route("/encrypt", methods=['POST'])
def encrypt():
	global message
	encryptedMessage = ""
	message = request.form['text']
	rotate = int(request.form['rot'])
	for char in message: 
		encryptedMessage += rotate_character(char, rotate)
	print(encryptedMessage)
	message = encryptedMessage
	return htmlBegin + form.format(rot=rotate, text=encryptedMessage) + htmlEnd

app.run()