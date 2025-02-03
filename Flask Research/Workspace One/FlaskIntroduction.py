from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloThere():
  return 'Welcome to Flask Introduction'


@app.route('/Welcome')
def WelcomeToWebProgramming():
  return 'Welcome to Flask Web Programming - This is fundamental knowledge on Web Programming and Development'


@app.route('/WebDevelopment')
def information():
  return 'Flask is a web development framework used to develop applications in Python3 it is such a usefull toolkit to build web things'


if __name__ == "__main__":
  app.run()
  
