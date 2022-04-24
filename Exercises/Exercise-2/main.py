import requests
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from bs4 import BeautifulSoup

url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"

def scrape_data(url):
    """Scrapes data from a given url

    Args:
        url (str): The url of the website to be scrapped to get the csv file
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser').find_all('a')
    for link in soup:
        if link.get("href") == "01011099999.csv":
            download_uri = f"{url}{link.get('href')}"
            csv_content = requests.get(download_uri)
            open("01011099999.csv", "wb").write(csv_content.content)
    print("Download Successful")
    
if __name__ == "__main__":
    scrape_data(url)
    filepath = '/home/mubarak/data-engineering-practice/Exercises/Exercise-2/01011099999.csv'
    os.rename(filepath, "climatological-data-14:03.csv")
