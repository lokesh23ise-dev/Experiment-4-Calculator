from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = float(data.get('num1'))
    num2 = float(data.get('num2'))
    op = data.get('operation')

    if op == 'add': result = num1 + num2
    elif op == 'sub': result = num1 - num2
    elif op == 'mul': result = num1 * num2
    elif op == 'div':
        result = num1 / num2 if num2 != 0 else "Error: Div by Zero"
    else: result = "Invalid"

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
