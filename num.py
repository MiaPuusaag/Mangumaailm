from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)

target_number = random.randint(1, 100)

@app.route('/')
def home():
    return render_template('kodu.html')

@app.route('/num')
def num():
    return render_template('num.html')

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
        target_number = random.randint(1, 100)  
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)
