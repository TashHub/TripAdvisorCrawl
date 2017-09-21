import requests
a =[]
my_url = "https://www.tripadvisor.com/Hotel_Review-g298342-d2554952-Reviews-Maritim_Crystals_Beach_Hotel_Mauritius-Belle_Mare.html"

my_url1 = "https://www.tripadvisor.com/Hotel_Review-g298343-d305531-Reviews-or1955-Sugar_Beach_Golf_Spa_Resort-Flic_En_Flac.html"

request = requests.get(my_url1, allow_redirects=True)
if request.status_code == 200:
    print('Web site exists')
else:
    print('Web site does not exist')

print(request.history)

if(request.history):
    print("broke!!!!!!!!!")