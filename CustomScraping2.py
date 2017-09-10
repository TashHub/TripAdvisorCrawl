import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# Assigning website url to variable
my_url = "https://www.tripadvisor.com/Hotels-g293816-Mauritius-Hotels.html"

# my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20card"

# Opening up connection and grabbing that web page; download it
uClient = uReq(my_url)

# Storing html page in page_html
page_html = uClient.read()

uClient.close()

# call soup function

# html parser
page_soup = soup(page_html, "html.parser")

print (page_soup.h1)

# Grabs each hotel listed
containers = page_soup.find_all("div", {"class": "listing_title"})

# check number of hotels retrieved
print(len(containers))

for hotel in containers:
    hotel_name = hotel.a.text
    hotel_link = hotel.a.get('href')
    print("https://www.tripadvisor.com" + hotel_link)
