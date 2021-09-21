import csv
import requests
import lxml
import bs4
from bs4 import BeautifulSoup
import time
import os

pages = [0,10,20,30,40,50,60,70]

with open('indeed.csv', 'a', encoding='utf-8', newline='') as f_output:
    csv_print =csv.writer(f_output)

    file_is_empty = os.stat('indeed.csv').st_size==0
    if file_is_empty:
        csv_print.writerow(['Job Title', 'Company', 'Location', 'Salary', 'Days Since Posted'])

#source = requests.get("https://ca.indeed.com/jobs?q=Data+Analyst&l=Canada").text
    for page in pages:
        source = requests.get("https://ca.indeed.com/jobs?q=Data+Analyst&l=Canada&start={}".format(page)).text
        soup = BeautifulSoup(source, 'lxml')

        for jobs in soup.find_all(class_='result'):
            #print(jobs.prettify())
            #print('----------')

            try:
                #job_title = jobs.h2.text.strip()
                job_title = jobs.select_one('h2.jobTitle > span').text.strip()
            except Exception as e:
                job_title = None
            print ('Job Title:' , job_title)

            try:
                company = jobs.find('span', class_='companyName').text.strip()
            except Exception as e:
                company = None
            print ('Company:' , company)

            try:
                location = jobs.find('div', class_='companyLocation').text.strip()
            except Exception as e:
                location = None
            print ('Location:' , location)

            try:
                salary = jobs.find('span', class_='salary-snippet').text.strip()
            except Exception as e:
                salary = None
            print ('Salary:' , salary)

            try:
                days = jobs.find('span', class_='date').text.strip()
            except Exception as e:
                salary = None
            print ('Days since posted:' , days)

            csv_print.writerow([job_title,company,location,salary,days])
            print('----')

            time.sleep(0.5)

