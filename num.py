from flask import Flask, jsonify, render_template, redirect, request, url_for
import random

num = Flask(__name__)

target_number = random.randint(1, 100)

@num.route('/')
def index():
    return render_template('num.html')

@num.route('/guess', methods=['POST'])
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
        target_number = random.randint(1, 100)  # Genereerib uue numbri järgmise mängu jaoks

    return jsonify({"message": message})

if __name__ == '__main__':
    num.run(debug=True)