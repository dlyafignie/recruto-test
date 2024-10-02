from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name')
    message = request.args.get('message')
    return f'Hello {name}! Давай дружить!'

if __name__ == '__main__':
    app.run()
