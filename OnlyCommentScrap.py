from urllib.request import urlopen as uReq
from urllib.error import URLError, HTTPError
import requests
import re

from bs4 import BeautifulSoup as soup
import CommentScrap


def main(hotels_array):
    print("Now getting hotel array from OnlyHotelScrap with length " + str(len(hotels_array)))

    # Start LOOP

    for hotel in hotels_array:

        comments_link_array = [['', '']]
        offset = 0
        status = 0

        name = hotel[0]
        name.replace(" ", "")
        print()
        my_url = hotel[1]

        index = re.search(r'\b(Reviews)\b', my_url)
        first = my_url[0:index.end() + 1]
        second = my_url[index.end() + 1:len(my_url)]

        new_url = my_url
        while new_url is not None:
            print(new_url)
            try:
                uClient = uReq(new_url)

                # check if there is redirection
                #if(requests.get(new_url, allow_redirects=True).history):
                if(new_url is not uClient.geturl()):
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

                # Grabs each comment links listed
                comments_containers = hotel_page_soup.find_all("div", {"class": "quote"})

                for comment in comments_containers:
                    comment_link = comment.a.get('href')
                    comment_title = comment.a.get_text()
                    comment_full_link = ("https://www.tripadvisor.com" + comment_link)

                    comments_link_array.append([comment_title, comment_full_link])
                    # print(comment_title)
                    # f.write(hotel_name + "," + hotel_full_link + "\n")

                if status is not 1:
                    next_button = hotel_page_soup.find(attrs={"class": "nav next taLnk "})
                    if next_button is not None:
                        offset += 5
                        print(offset)
                        # index = re.search(r'\b(Reviews)\b', my_url)
                        # first = my_url[0:index.end() + 1]
                        # second = my_url[index.end() + 1:len(my_url)]
                        new_url = first + "or" + str(offset) + "-" + second
                    else:
                        print("No NEXT Button found")
                else:
                    print("BROKE")
                    break
            except URLError as u:
                print("comment link URL error: " + u.reason)

            except HTTPError as e:
                print("comment link HTTP error:" + e.code)
            except e:
                print("Timeout !")
                continue
        my_url = new_url

        del comments_link_array[0]
        print("Number of comments for " + name + " is " + str(len(comments_link_array)))
        CommentScrap.main(comments_link_array, name)

            # End LOOP

    return comments_link_array