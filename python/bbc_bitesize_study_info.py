from bs4 import BeautifulSoup
import requests


subject_lvl = input("What academic level are you currently (KS3/GCSE): ").strip().lower()
if subject_lvl == "ks3":
    html_code = requests.get("https://www.bbc.co.uk/bitesize/levels/z4kw2hv").text
    
elif subject_lvl == "gcse":
    html_code = requests.get("https://www.bbc.co.uk/bitesize/levels/z98jmp3").text

else:
    print("That is an invalid response")
    
try:
    soup = BeautifulSoup(html_code, "lxml")
    subject_lst = soup.find_all("div", class_="bitesize-subject-card__label")
    print("\nHere are all the relevant subjects regarding your academic level.")
    for subject in subject_lst:
        print(subject.text)
        
except:
    pass