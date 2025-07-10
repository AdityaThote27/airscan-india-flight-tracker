# ✈️ AirScan India – Live Flight Tracker

A sleek and powerful flight tracking dashboard built using **Flask**, **Chart.js**, and **Python**, visualizing live flight data, airline distribution, status breakdown, and departure trends.

> 🚀 Built with real-world airline routes and simulated flight data using API/Web scraping logic. Features CSV export and interactive charts (bar/pie toggle).

---

## 🔍 Features

- ✅ Track live flights on selected Indian routes  
- 📊 Dynamic charts:
  - Flights per Airline (Bar/Pie toggle)
  - Status distribution (Scheduled, Delayed, Landed)
  - Departure time histogram
- 📥 Export live flight data to CSV
- 🎨 Clean UI with responsive layout (Chart.js)

---

## 🔌 Data Source: API & Web Scraping Simulation

In a full-scale version, flight data would be pulled from APIs like:

- [AviationStack API](https://aviationstack.com/)
- [FlightAware API](https://flightaware.com/commercial/firehose/firehose_documentation.rvt)
- Web scraping logic using `requests` and `BeautifulSoup` (e.g., scraping airline sites)

🔧 **Current Version** uses a simulated `ROUTE_DATA` dictionary to mimic scraped/parsed flight records, structured similarly to what actual APIs return.

---

## 🛠️ Technologies Used

- **Backend**: Python 3.11, Flask  
- **Frontend**: HTML, CSS, Jinja2, Chart.js  
- **Data Manipulation**: Pandas  
- **File Download**: CSV (generated on-the-fly)  
- **Chart Interactivity**: JavaScript + Chart.js toggle logic  

---


