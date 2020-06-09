from flask import Flask, Response
import letterboxd

app = Flask(__name__, static_folder='./client/build', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')
    
@app.route('/api/')
def api_root():
    return Response(
        "This is the root api path, call explicit endpoints for data",
        status=418,
    )

@app.route('/api/daily')
def daily_count():
    data = letterboxd.get_timeseries()
    return {
        'diary': data
    }

@app.route('/api/monthly')
def monthly_count():
    pass
