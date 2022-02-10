from bs4 import BeautifulSoup
import requests
import pandas as pd

pageContent = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
soup = BeautifulSoup(pageContent, 'lxml')

jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name =[]
recently_updated =[]
exp =[]
key_skills =[]
for job in jobs:
    recent_job = job.find('span', class_ = 'sim-posted').text
    if 'few' in recent_job :
        recently_updated.append("Yes")
    else:
        recently_updated.append("No")
    company_name.append(job.find('h3', class_ = 'joblist-comp-name').text.strip().strip('(More Jobs)'))
    exp.append(job.find('ul', class_ = 'top-jd-dtl clearfix').text.split('\n')[1].strip('card_travel'))
    key_skills.append(job.find('span', class_= 'srp-skills').text.strip().replace(' ',''))

df = pd.DataFrame({'Company_name':company_name, 'Exp': exp, 'key_skills' :key_skills, 'recently_updated':recently_updated })
print(df)