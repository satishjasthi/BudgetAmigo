from flask import Flask
app = Flask(__name__)

@app.route('/')
def login_page():
    return 'Hello, Docker!'