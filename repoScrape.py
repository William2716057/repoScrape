import requests
from bs4 import BeautifulSoup

repo = input("enter github profile name: ")

URL = "https://github.com/" + repo + "?tab=repositories"

print(URL)

path_to_scrape = requests.get(URL)
print(path_to_scrape)