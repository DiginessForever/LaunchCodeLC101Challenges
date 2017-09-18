from flask import Flask, request

app = Flask(__name__)
form_html = '''
	<!DOCTYPE html>
	<html>
		<head>
		</head>
		<body>
			<form method="POST" action="/hello">
				<input type="text" name="name" />
				<input type="date" name="birthdate"/>
				<input name="postThis" type="submit" text="go" />
			</form>
		</body>
	</html>
	'''
response_html = '''
	<!DOCTYPE html>
	<html>
		<head></head>
		<body>
			<h1>Hello {name:s}></h1>
			<span>Your birthday is {birthday:s}</span>
		</body>
	</html
	'''

@app.route('/')
def handle_stuff():
	
	print(request.form)
	return form_html


@app.route('/hello', methods=['POST'])
def handle_hello():
	#could also do method=['GET', 'POST']
	#return 'HELLO {}'.format(request.form['name'])

	return response_html.format(name=request.form['name'],
		birthday=request.form['birthday'])

if __name__ == "__main__":
	app.run(debug=True) #This starts the web server / starts listening



