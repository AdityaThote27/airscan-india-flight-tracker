import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

def get_flight_data(source, destination):
    url = "http://api.aviationstack.com/v1/flights"
    params = {
        "access_key": API_KEY,
        "dep_iata": source,
        "arr_iata": destination,
        "limit": 10
    }

    response = requests.get(url, params=params)
    data = response.json()

    flights = []
    if "data" in data:
        for flight in data["data"]:
            flights.append({
                "airline": flight["airline"]["name"],
                "flight_number": flight["flight"]["iata"],
                "departure": flight["departure"]["airport"],
                "arrival": flight["arrival"]["airport"],
                "status": flight["flight_status"]
            })
    return flights
