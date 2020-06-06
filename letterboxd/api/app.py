from flask import Flask, Response
import letterboxd

app = Flask(__name__)

@app.route('/api/')
def index():
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