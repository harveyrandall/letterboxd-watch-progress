from flask import Flask

app = Flask(__name__)

@app.route('/api/time')
def index():
    return {'data': None}