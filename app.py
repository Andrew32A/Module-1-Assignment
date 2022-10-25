from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """Displays a madlib to the user based on adjective and noun."""
    return f'This really cool {noun} is super {adjective}!'

@app.route('/multiply/<number1>/<number2>')
def mult(number1, number2):
    """Multiplies two numbers."""
    answer = int(number1)*int(number2)
    return f'{number1} times {number2} is {answer}'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Repeat a string any number of times"""
    isWord = word.isalpha()
    isNum = n.isdigit()
    if isWord == False or isNum == False:
        return "Invalid input. Please try again by entering a word and a number!"
    else:
        return (word + " ")*int(n)
        
@app.route('/dicegame')
def dicegame():
    """Rolls a 6 sided dice"""
    dice = random.randint(1,6)
    state = ""
    if dice == 6:
        state = "Win"
    else:
        state = "Lose"
    return f'You rolled a {dice}, you {state}!'


if __name__ == '__main__':
    app.run(debug=True)

