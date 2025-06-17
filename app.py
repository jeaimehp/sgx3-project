from flask import Flask

app = Flask(__name__)

# / Route that displays hello world
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, world!\n'

# /<variable> to list as name
@app.route('/<name>', methods=['GET'])
def hello_name(name):
    return f'Hello, {name}!\n'


# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8002')
