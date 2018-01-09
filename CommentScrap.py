from urllib.request import urlopen as uReq
from urllib.error import URLError, HTTPError
import requests
import socket

from bs4 import BeautifulSoup as soup


def main(comments_link_array, name):

    print("Creating file with hotel name: " + name)
    nm = name.replace("*","")
    filename = nm + ".csv"
    f = open(filename, "w", encoding="utf-8")

    headers = "Comment Title, Comment\n"

    f.write(headers)
    # comment_url = "https://www.tripadvisor.com/ShowUserReviews-g298342-d2554952-r237556936-Maritim_Crystals_Beach_Hotel_Mauritius-Belle_Mare.html#CHECK_RATES_CONT"

    for comment_url in comments_link_array:
        try:
            uClient = uReq(comment_url[1], data=None, timeout=500)

            # Storing html page in page_html
            comment_html = uClient.read()

            uClient.close()

            # call soup function

            # html parser
            comment_soup = soup(comment_html, "html.parser")
            # print(page_soup.h1)
            # Grabs each hotel listed

            title = comment_soup.find("span", {"class": "noQuotes"})
            comment = comment_soup.find("p", {"class": "partial_entry"})
            location = comment_soup.find("span", {"class": "expand_inline userLocation"})
            date = comment_soup.find("span", {"class": "ratingDate relativeDate"})
            mob = comment_soup.find("span", {"class": "ui_icon mobile-phone"})

            # if comment_soup.find("span", {"class": "ui_bubble_rating bubble_10"}):
            #     rating = 1
            # if comment_soup.find("span", {"class": "ui_bubble_rating bubble_20"}):
            #     rating = 2
            # if comment_soup.find("span", {"class": "ui_bubble_rating bubble_30"}):
            #     rating = 3
            # if comment_soup.find("span", {"class": "ui_bubble_rating bubble_40"}):
            #     rating = 4
            # if comment_soup.find("span", {"class": "ui_bubble_rating bubble_50"}):
            #     rating = 5
            rating = comment_soup.find("div", {"class": "rating"})
            rating_inside = rating.find('span')
            span_inside = rating_inside.find('span')
            rating_value = (span_inside.attrs['alt'][0])
            #print(rating_value)


            tle = title.text.replace(",", "|")
            cmm = comment.text.replace(",", "|")
            if location:
                loc = location.text.replace(",", "|")
            dte = date.attrs['title']

            date_splitted = dte.split()
            month = date_splitted[0]
            day = date_splitted[1].replace(",", "")
            year = date_splitted[2]

            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            month_index = months.index(month) + 1

            date_formatted = day + "-" + str(month_index) + "-" + year
            if mob:
                mobile = "Yes"
            else:
                mobile = "No"

            f.write(tle + "," + cmm + "," + loc + "," + ""+date_formatted+"" + "," + mobile + "," + str(rating_value) +"\n")

            # print(title.text)
            # print(comment.text)

        except URLError as u:
            print("Comment URL error: " + u.reason)

        except HTTPError as e:
            print("comment HTTP error:" + e.code)
        except f:
            print("Timeout in CommentScrap!")
            continue

        except socket.timeout:
            print("Timeout Exception caught")


    # print("Closing file with hotel name: " + name)
    f.close()
