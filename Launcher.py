import program, OnlyHotelScrap, OnlyCommentScrap


# hotel_array = [['Le Meridien','https://www.google.com']]
#
#
# hotel_array.append(['La Pirogue','https://bing.com'])
# hotel_array.append(['Le Morne','https://bing.com'])
# hotel_array.append(['La Suffren','https://bing.com'])
# hotel_array.append(['Lux Hotel','https://bing.com'])
#
# program.main("https://www.tripadvisor.com/Hotel_Review-g298342-d2554952-Reviews-or390-Maritim_Crystals_Beach_Hotel_Mauritius-Belle_Mare.html")
# program.exe(hotel_array)


# START
hotels_array = OnlyHotelScrap.main()

del hotels_array[0]
print(len(hotels_array))

# print(hotels_array[1][1])
# print(hotels_array[0][1])

OnlyCommentScrap.main(hotels_array)



# for i in hotels_array:
#     print(i[1])
