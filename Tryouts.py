# array = [['','']]
#
#
# array.append(["Le Meridien" ,"https://lemeridien"])
#
# for i in array:
#     print(i[0])

# import re
#
# string = "https://www.tripadvisor.com/Hotel_Review-g488102-d477273-Reviews-Shandrani_Beachcomber_Resort_Spa-Blue_Bay.html"
# index = re.search(r'\b(Reviews)\b', string)
# first = string[0:index.end()+1]
# second = string[index.end()+1:len(string)]
# print(first)
# print(second)

#
# array = [['','']]
#
# array.append(["Le Meridien", "https://fsdfsdfsdfsdf"])
# array.append(["Le Meridien", "https://sdfsdfsd"])
# array.append(["Le Meridien", "https://fsdfsdf"])
#
# del array[0]
# for i in array:
#
#     print(i[1])
#     # if(i[1]is not ''):
#     #     print(i[1])

# from urllib.request import urlopen as uReq
# from urllib.error import URLError, HTTPError
# import requests
# import re
#
# from bs4 import BeautifulSoup as soup
# import CommentScrap
#
# new_url = "https://www.tripadvisor.com/Hotel_Review-g298343-d585517-Reviews-or95-Gold_Beach_Resort-Flic_En_Flac.html"
# try:
#     uClient = uReq(new_url)
# except URLError as u:
#     print("URL error: " + u.reason)
# except HTTPError as e:
#     print("HTTP error:" + e.code)
#
# print(uClient.geturl())
#
# if(new_url is not uClient.geturl()):
#     print("REDIRECTED")
# # check if there is redirection
# print(requests.get(new_url, allow_redirects=True).history)

# string = "lux*"
# print(string)
#
# st = string.replace("*", "")
# print(st)


#Splitting string for date,month,year

# string = "January 17, 2017"
#
# splitted = string.split()
# month = splitted[0]
# day = splitted[1].replace(",", "")
# year = splitted[2]
#
# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
#           "December"]
# month_index = months.index(month) + 1
# date_formatted = day + "-" + str(month_index) + "-" + year
#
# print(splitted)
# print(day)
# print(month)
# print(month_index)
# print(year)
#
# print(date_formatted)


from urllib.request import urlopen as uReq
from urllib.error import URLError, HTTPError
import requests
import re
import socket
from bs4 import BeautifulSoup as soup
import CommentScrap
import random

new_url = "https://www.tripadvisor.com/Hotel_Review-g488105-d568249-Reviews-Indian_Resort-Le_Morne.html"
uClient = uReq(new_url, timeout=100)

# check if there is redirection
# if(requests.get(new_url, allow_redirects=True).history):


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
    print(len(comments_containers))
    a = comment.find('a')
    if a:
        print("EXIST")
        comment_link = comment.a.get('href')
        comment_title = comment.a.get_text()
        comment_full_link = ("https://www.tripadvisor.com" + comment_link)

        # comments_link_array.append([comment_title, comment_full_link])
        # print(comment_title)
        # f.write(hotel_name + "," + hotel_full_link + "\n")
