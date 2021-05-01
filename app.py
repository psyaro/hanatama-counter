from flask import Flask
import hanatama_core
import settings
app = Flask(__name__, static_folder='docs')

@app.route('/')
def hello():
    return hanatama_core.counter()[0]

@app.route(settings.private_hooks_url)
def private_hooks():
    return hanatama_core.send_to_discord()

if __name__ == "__main__":
    app.run(debug=True)