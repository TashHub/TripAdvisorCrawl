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


array = [['','']]

array.append(["Le Meridien", "https://fsdfsdfsdfsdf"])
array.append(["Le Meridien", "https://sdfsdfsd"])
array.append(["Le Meridien", "https://fsdfsdf"])

del array[0]
for i in array:

    print(i[1])
    # if(i[1]is not ''):
    #     print(i[1])