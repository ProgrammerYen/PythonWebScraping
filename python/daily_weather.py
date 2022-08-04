from bs4 import BeautifulSoup
import requests

html_code = requests.get("https://www.bbc.co.uk/weather/2634867").text

soup = BeautifulSoup(html_code, "lxml")
temp_in_wallington = soup.find("span", class_="wr-value--temperature--c")
print("It is currently " + str(temp_in_wallington.text[:2]) + " degrees celsius in Wallington.")