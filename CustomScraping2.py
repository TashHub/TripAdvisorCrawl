import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def main():

    hotels_array = [[]]
    filename = "hotels.csv"
    f = open(filename, "w")

    headers = "Hotels, Hotel_link\n"

    f.write(headers)

    # Start LOOP
    my_url = "https://www.tripadvisor.com/Hotels-g293816-Mauritius-Hotels.html"

    while my_url is not None:
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

        # check number of hotels retrieved
        print(len(containers))

        # Going through each hotel
        for hotel in containers:
            hotel_name = hotel.a.text
            hotel_link = hotel.a.get('href')
            hotel_full_link = ("https://www.tripadvisor.com" + hotel_link)

            # Go through each hotel to get reviews
            hotelClient = uReq(hotel_full_link)

            print(hotel_full_link)
            # Storing hotel page in hotel_html
            hotel_html = hotelClient.read()
            hotelClient.close()
            # call soup function
            # html parser
            hotel_soup = soup(hotel_html, "html.parser")

            comment_link = hotel_soup.find_all("div", {"class": "quote isNew"})

            for comment in comment_link:
                comment_link_container = comment.a.get('href')
                print(comment_link_container)



            # Finding review count by class tag
            reviews = hotel_soup.find(attrs={"class": "reviews_header_count block_title"})
            reviews_count = reviews.text

            reviews_container = hotel_soup.find_all(attrs={"class": "prw_rup prw_reviews_text_summary_hsx"})

            # for review in reviews_container:
            print(len(reviews_container))
            # print(hotel_full_link)



        # get next link
        next_button = page_soup.find(attrs={"class": "nav next taLnk ui_button primary"})
        if next_button is not None:
            next_button_link = (next_button.get('href'))

        print(next_button_link)

        my_url = "https://www.tripadvisor.com" + next_button_link

        # End LOOP

