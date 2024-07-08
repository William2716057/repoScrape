import requests
from bs4 import BeautifulSoup
repo = input("enter github profile name: ")

#URL = "https://github.com/" + repo + "?tab=repositories"

URL = f"https://github.com/{repo}?tab=repositories"

print(URL)

response = requests.get(URL)
print(response)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    repos = soup.find_all('a', itemprop='name codeRepository')
    
    for repo in repos:
        print(repo.text.strip())
        
else:
    print("Failed to retrieve")
    