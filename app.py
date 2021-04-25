from flask import Flask
app = Flask(__name__, static_folder='docs')

@app.route('/')
def hello():
    name = "Hello World"
    return name

if __name__ == "__main__":
    app.run(debug=True)