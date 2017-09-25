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

from urllib.request import urlopen as uReq
import requests
import re

from bs4 import BeautifulSoup as soup
import CommentScrap

# new_url = "https://www.tripadvisor.com/Hotel_Review-g298342-d2554952-Reviews-or490-Maritim_Crystals_Beach_Hotel_Mauritius-Belle_Mare.html"
# uClient = uReq(new_url)
#
# print(uClient.geturl())
#
# if(new_url is not uClient.geturl()):
#     print("REDIRECTED")
# # check if there is redirection
# print(requests.get(new_url, allow_redirects=True).history)

string = "lux*"
print(string)

st = string.replace("*", "")
print(st)