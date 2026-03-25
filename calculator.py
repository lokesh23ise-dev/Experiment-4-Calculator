from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Calculator API is Running! Use /add/5/10 to test."

@app.route('/<operation>/<int:num1>/<int:num2>')
def calculate(operation, num1, num2):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'mul':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        result = num1 / num2
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({
        "operation": operation,
        "num1": num1,
        "num2": num2,
        "result": result
    })

if __name__ == '__main__':
    app.run(debug=True)
