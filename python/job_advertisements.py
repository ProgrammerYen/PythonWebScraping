from bs4 import BeautifulSoup
import requests 

html_file = requests.get("https://uk.indeed.com/jobs?q=python&l&vjk=02b5977672d34166").text
soup = BeautifulSoup(html_file, "lxml")

# the relevant job results after searching "python" in the search bar.
relevant_job_titles = soup.find_all("a", class_="jcs-JobTitle css-jspxzf eu4oa1w0")[:10]

print("Here are the top 10 python-related jobs on Indeed:\n")
for i in relevant_job_titles:
    print(i.text)