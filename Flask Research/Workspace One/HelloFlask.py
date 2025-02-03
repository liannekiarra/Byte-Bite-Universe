from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def helloThere():
    return 'Welcome to Flask Lily'

@app.route('/Welcome')
def welcomeToWebProgramming():
    return 'Welcome to Flask Web Programming - This is fundamental knowledge on Web Programming and Development'

if __name__ == '__main__':
    app.run()
