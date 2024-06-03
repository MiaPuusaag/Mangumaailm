from flask import Flask, render_template

kodu = Flask(__name__)

@kodu.route('/')
def home():
    return render_template('kodu.html')

if __name__ == '__main__':
    kodu.run(debug=True)