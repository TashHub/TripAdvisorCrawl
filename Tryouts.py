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

string = "January 17, 2017"

splitted = string.split()
month = splitted[0]
day = splitted[1].replace(",", "")
year = splitted[2]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
month_index = months.index(month) + 1
date_formatted = day + "-" + str(month_index) + "-" + year

print(splitted)
print(day)
print(month)
print(month_index)
print(year)

print(date_formatted)