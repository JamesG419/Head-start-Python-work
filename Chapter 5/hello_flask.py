

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() -> set:
	return 'Hello world from Flask!'

app.run()