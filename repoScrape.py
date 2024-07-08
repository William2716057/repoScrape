import requests
from bs4 import BeautifulSoup
import csv

repo = input("enter github profile name: ")
page = 1

URL = f"https://github.com/{repo}?page={page}&tab=repositories"

print(URL)

response = requests.get(URL)
print(response)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    repos = soup.find_all('a', itemprop='name codeRepository')
    
    #for repo in repos:
        #print(repo.text.strip())
    with open('repositories.csv', 'w', newline='') as csvfile:
        fieldnames = ['Repository Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header
        writer.writeheader()
        
        # Write each repository name to the CSV file
        for repo in repos:
            repo_name = repo.text.strip()
            print(repo_name)
            writer.writerow({'Repository Name': repo_name})
        
else:
    print("Failed to retrieve")
    
