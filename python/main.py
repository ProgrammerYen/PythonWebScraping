from bs4 import BeautifulSoup

FILE_PATH = "C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula/python_work/web_scraping/html/home.html"
with open(FILE_PATH, "r") as html_file:
    contents = html_file.read()
    
    soup = BeautifulSoup(contents, "lxml")

    # all h3 tags in the html file
    courses = soup.find_all("h3")
    
    # all button elements which hold the prices of the courses.
    course_prices = soup.find_all("button")
    
    # the corresponding course and price
    course_and_price = {}
    
    # appending values to the dictionary with the course corresponding to its price.
    for i in range(len(courses)):
        course_and_price[courses[i].text] = course_prices[i].text    
     
    # displaying our data   
    print("Here are the following courses and their prices.\n")
    for course, price in course_and_price.items():
        price = price.split()[-1]
        print(course + "\n" + f"Price: {price}\n")     