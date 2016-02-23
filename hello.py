from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello {}!".format(request.args.get('name', 'Andrei'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
