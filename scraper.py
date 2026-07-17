import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv



url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
if response.status_code == 200:
    print("<<<status code ok>>>")
    
else:
      print("erore")
      
    
soup = BeautifulSoup(response.text, "html.parser")

jobs = []


cards = soup.find_all("div", class_="card-content")

for card in cards:
    
    title = card.find("h2").get_text(strip=True)
    
    company = card.find("h3").get_text(strip=True)
    
    location = card.find("p", class_="location").get_text(strip=True)

    link = card.find_all("a")[1]["href"]

    jobs.append({
        
         "title": title,
         "company" : company,
         "location": location,
         "link" : link
        
        })    
    

python_jobs = []

for job in jobs: 
    if "python" in job["title"].lower():
        python_jobs.append(job)
        
df = pd.DataFrame(python_jobs)
df.to_csv(
     "jobs.csv",
     index=False,
     encoding = "utf-8-sig"     
)
    








print(f"{(len(jobs))} jobs saved...")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    