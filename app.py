from flask import Flask
from flask import jsonify
app = Flask(__name__)

def tosec(t):
    sec=t*2
    return sec


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /sec'

@app.route('/sec/<t>')
def changesec(t):
    result =tosec(t)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
