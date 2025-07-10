from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

def test_flight_data():
    url = "http://api.aviationstack.com/v1/flights"
    params = {
        "access_key": API_KEY,
        "dep_iata": "DEL",
        "arr_iata": "BOM",
        "limit": 2
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)

test_flight_data()
