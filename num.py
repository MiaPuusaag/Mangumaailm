from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__, template_folder='templates', static_folder='images')

# Generate a random number for the guessing game
target_number = random.randint(1, 100)

@app.route('/')
def home():
    return render_template('kodu.html')

@app.route('/num')
def num():
    return render_template('num.html')

@app.route('/index')
def index():
    global money, coffee_count
    return render_template('index.html', money=money)

@app.route('/guess', methods=['POST'])
def guess():
    global target_number
    data = request.get_json()
    guess = int(data['guess'])

    if guess < target_number:
        message = "Liiga vähe!"
    elif guess > target_number:
        message = "Liiga palju!"
    else:
        message = "Arvasidki ära! Genereerin uue numbri..."
        target_number = random.randint(1, 100)  # Generate a new number for the next game

    return jsonify({"message": message})

# Initialize money and coffee count
money = 0

"""
@app.route('/buy_coffee', methods=['POST'])
def buy_coffee():
    global money, coffee_count
    coffee_price = 10
    if money >= coffee_price:
        coffee_count += 1
    return redirect(url_for('index'))

@app.route('/increase_money', methods=['POST'])
def increase_money():
    global money
    money += 1
    return redirect(url_for('index'))

"""

if __name__ == '__main__':
    app.run(debug=True)
