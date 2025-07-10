from flask import Flask, render_template, request, send_file, session
import pandas as pd
from collections import Counter
from io import BytesIO

app = Flask(__name__)
app.secret_key = 'airscan123'

# Simulated data
ROUTE_DATA = {
    "DEL-BOM": [
        {"airline": "IndiGo", "flight_number": "6E203", "from": "DEL", "to": "BOM", "status": "Scheduled", "dep_time": "10:00", "arr_time": "12:00"},
        {"airline": "Air India", "flight_number": "AI101", "from": "DEL", "to": "BOM", "status": "Landed", "dep_time": "09:00", "arr_time": "11:00"},
    ],
    "BLR-DEL": [
        {"airline": "SpiceJet", "flight_number": "SG401", "from": "BLR", "to": "DEL", "status": "Delayed", "dep_time": "08:00", "arr_time": "10:30"},
    ],
    "BOM-HYD": [],
    "MAA-BLR": [],
    "CCU-DEL": []
}

@app.route('/', methods=['GET', 'POST'])
def index():
    flights = []
    airline_stats = {}
    status_stats = {}
    dep_time_stats = {}

    if request.method == 'POST':
        route = request.form['route']
        flights = ROUTE_DATA.get(route, [])
        session['flights'] = flights

        if flights:
            df = pd.DataFrame(flights)

            # Convert dep_time to hour for histogram
            df['hour'] = pd.to_datetime(df['dep_time'], format='%H:%M').dt.hour

            airline_counts = df['airline'].value_counts()
            status_counts = df['status'].value_counts()
            hour_counts = df['hour'].value_counts().sort_index()

            # Convert to native types to avoid JSON serialization issues
            airline_stats = {
                'labels': airline_counts.index.tolist(),
                'values': [int(x) for x in airline_counts.values]
            }
            status_stats = {
                'labels': status_counts.index.tolist(),
                'values': [int(x) for x in status_counts.values]
            }
            dep_time_stats = {
                'labels': [str(x) for x in hour_counts.index.tolist()],
                'values': [int(x) for x in hour_counts.values]
            }

    return render_template(
        'index.html',
        flights=flights,
        airline_stats=airline_stats,
        status_stats=status_stats,
        dep_time_stats=dep_time_stats
    )

@app.route('/download_csv')
def download_csv():
    flights = session.get('flights', [])
    if not flights:
        return "No data to download", 400

    df = pd.DataFrame(flights)
    output = BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, mimetype='text/csv', as_attachment=True, download_name='flights.csv')

if __name__ == '__main__':
    app.run(debug=True)
