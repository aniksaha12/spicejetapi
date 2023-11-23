import requests
from bs4 import BeautifulSoup

def scrape_flight_status(flight_number):
    url = f'https://book.spicejet.com/flightstatus.aspx?flightNumber={flight_number}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"Error: Unable to fetch data from SpiceJet website. Status Code: {response.status_code}"

    print(response.text)  # Add this print statement to check the HTML content

    soup = BeautifulSoup(response.text, 'html.parser')
    status_element = soup.find('div', {'class': 'FlightStatusTable'})

    print(status_element)  # Add this print statement to check the status element

    if status_element:
        flight_status = status_element.find('td', {'class': 'statusvalue'})
        if flight_status:
            return flight_status.text.strip()
        else:
            return "Error: Flight status information not found on the page."
    else:
        return "Error: Flight status container not found on the page."
