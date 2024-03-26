from flask import Flask
app = Flask(__name__)
@app.route('/')
def heelo_world():
    return '<h1>Hello from my azurewebapp</h2>'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
