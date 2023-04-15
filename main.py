import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    """Scrape the page source form the URL"""
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def send_email():
    print("Email was Sent!")


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    
    if extracted != "No upcoming tours":
        print(extracted)
        send_email()