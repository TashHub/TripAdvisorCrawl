import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import socket

hotels_array = [['','']]
def main():
    hotels_array = [['','']]

    filename = "hotels.csv"
    f = open(filename, "w")

    headers = "Hotels, Hotel_link\n"

    f.write(headers)

    # Start LOOP
    my_url = "https://www.tripadvisor.com/Hotels-g293816-Mauritius-Hotels.html"

    while my_url is not None:
        try:

            # print(my_url)
            # Assigning website url to variable
            # my_url = "https://www.tripadvisor.com/Hotels-g293816-Mauritius-Hotels.html"

            # my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20card"

            # Opening up connection and grabbing that web page; download it
            uClient = uReq(my_url)

            # Storing html page in page_html
            page_html = uClient.read()

            uClient.close()

            # call soup function

            # html parser
            page_soup = soup(page_html, "html.parser")

            # print(page_soup.h1)

            # Grabs each hotel listed
            containers = page_soup.find_all("div", {"class": "listing_title"})

            # Going through each hotel
            for hotel in containers:
                hotel_name = hotel.a.text
                hotel_link = hotel.a.get('href')
                hotel_full_link = ("https://www.tripadvisor.com" + hotel_link)
                hotels_array.append([hotel_name , hotel_full_link])
                f.write(hotel_name + "," + hotel_full_link + "\n")

            # check number of hotels retrieved
            # print(len(containers))

            # get next link
            next_button = page_soup.find(attrs={"class": "nav next taLnk ui_button primary"})
            if next_button is not None:
                next_button_link = (next_button.get('href'))

            # print(next_button_link)

            new_url = "https://www.tripadvisor.com" + next_button_link

            if new_url == my_url:
                break
            else:
                my_url = "https://www.tripadvisor.com" + next_button_link

            # End WHILE LOOP

        except socket.timeout:
            print("Timeout in OnlyHotelScrap")

    # for i in hotels_array:
    #     print(i)
    f.close()

    return hotels_array
