import requests

def main(url):

    if (requests.get(url, allow_redirects=True).history):
        status = 1
        print("BROKE!!!!!!!!!!!!!!!!")
    else:
        print("NO REDIRECT!!!")


def exe(hotel_array):
    for hotel in hotel_array:
        print(hotel[0])