from flask import Flask, request, render_template
import random

app = Flask(__name__)
def get_condition(degrees):
    if degrees >= 100:
        return "fever"
    else:
        return "cold"

def generate_lucky_number():
    return random.randint(1, 100)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/health', methods=['GET'])
def health():
    condition = None
    if 'degree' in request.args:
        degree = float(request.args['degree'])
        condition = get_condition(degree)
    return render_template('health.html', condition=condition)

@app.route('/luckynumber', methods=['GET'])
def lucky_number():
    number = generate_lucky_number()
    return render_template('luckynumber.html', number=number)

if __name__ == '__main__':
    app.run(debug=True)
