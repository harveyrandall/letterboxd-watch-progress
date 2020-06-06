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
    today = datetime.date.today()
    days_passed = (today - datetime.date(today.year, 1, 1)).days + 1
    data = letterboxd.get_timeseries(day_of_year)
    return {
        'data': data
    }

@app.route('/api/monthly')
def monthly_count():
    pass