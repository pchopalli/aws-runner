from flask import Flask
from flask import jsonify
app = Flask(__name__)

def tosec(t):
    hr=int(t.split(':')[0])
    min=int(t.split(':')[1])
    sec=int(t.split(':')[2])
    hr=hr*3600
    min=min*60
    sec=hr+min+sec
    return sec


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /sec'

@app.route('/sec/t')
def changesec(t):
    result =tosec(t)
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)