from bs4 import BeautifulSoup

#Getting html content and assigning to r
#r = requests.get("https://www.tripadvisor.com/Hotels-g293816-Mauritius-Hotels.html")

r = requests.get("https://www.tripadvisor.com/Hotel_Review-g1152294-d1152299-Reviews-Four_Seasons_Resort_Mauritius_at_Anahita-Beau_Champ.html")

print("Heloooo")
soup = BeautifulSoup(r.content)

#print soup.prettify()

soup.find_all("div class='review-container'")
#find = soup.find_all("div class='review-container'")

#print find