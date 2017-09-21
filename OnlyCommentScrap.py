from urllib.request import urlopen as uReq
import requests

from bs4 import BeautifulSoup as soup

comments_link_array = [['','']]
offset = 0
status = 0

filename = "hotels.csv"
f = open(filename, "w")

headers = "Person, Hotel_link\n"

f.write(headers)

# Start LOOP
ini_url = "https://www.tripadvisor.com/Hotel_Review-g298342-d2554952-Reviews-Maritim_Crystals_Beach_Hotel_Mauritius-Belle_Mare.html"

my_url = "https://www.tripadvisor.com/Hotel_Review-g298342-d2554952-Reviews-Maritim_Crystals_Beach_Hotel_Mauritius-Belle_Mare.html"

while my_url is not None:
    print(my_url)
    uClient = uReq(my_url)

    # check if there is redirection
    if(requests.get(my_url, allow_redirects=True).history):
        status = 1
        print("BROKE!!!!!!!!!!!!!!!!")
        break

    # Storing html page in page_html
    hotel_page_html = uClient.read()

    uClient.close()

    # call soup function

    # html parser
    hotel_page_soup = soup(hotel_page_html, "html.parser")

    # print(page_soup.h1)

    # Grabs each hotel listed
    comments_containers = hotel_page_soup.find_all("div", {"class": "quote"})

    for comment in comments_containers:
        comment_link = comment.a.get('href')
        comment_title = comment.a.get_text()
        comment_full_link = ("https://www.tripadvisor.com" + comment_link)

        comments_link_array.append([comment_title , comment_full_link])
        print(comment_title)
        # f.write(hotel_name + "," + hotel_full_link + "\n")

    if status is not 1:
        next_button = hotel_page_soup.find(attrs={"class": "nav next taLnk "})
        if next_button is not None:
            offset += 5
            print(offset)
            new_url = "https://www.tripadvisor.com/Hotel_Review-g298342-d2554952-Reviews-or" + str(offset) +"-Maritim_Crystals_Beach_Hotel_Mauritius-Belle_Mare.html"
    else:
        print("BROKE")
        break

    my_url = new_url

    # End LOOP