import requests
import pandas


url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"

r = requests.get(url)

print(r.content[:100])