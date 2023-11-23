from flask import jsonify
from app import app
from .scraping import scrape_flight_status

@app.route('/flight_status/<flight_number>')

def get_flight_status(flight_number):
    status = scrape_flight_status(flight_number)
    return jsonify({"flight_number": flight_number, "status": status})