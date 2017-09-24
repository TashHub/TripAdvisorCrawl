from urllib.request import urlopen as uReq
import requests

from bs4 import BeautifulSoup as soup


def main(comments_link_array, name):
    # def main():
    # print("Creating file with hotel name: " + name)
    filename = name + ".csv"
    f = open(filename, "w")

    headers = "Comment Title, Comment\n"

    f.write(headers)
    # comment_url = "https://www.tripadvisor.com/ShowUserReviews-g298342-d2554952-r237662272-Maritim_Crystals_Beach_Hotel_Mauritius-Belle_Mare.html#CHECK_RATES_CONT"

    # for comment_url in comments_link_array:
    uClient = uReq(comments_link_array[1])

    # Storing html page in page_html
    comment_html = uClient.read()

    uClient.close()

    # call soup function

    # html parser
    comment_soup = soup(comment_html, "html.parser")

    title = comment_soup.find("span", {"class": "noQuotes"})
    comment = comment_soup.find("p", {"class": "partial_entry"})

    # removing comma from text because csv
    cmm = comment.text.replace(",", "|")

    f.write(title.text + "," + cmm + "\n")

    # print("Closing file with hotel name: " + name)
    f.close()
