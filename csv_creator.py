import csv
csvOut=open("C:/Users/tash/Desktop/trip_data.csv", "w")
spamWriter = csv.writer(csvOut, delimiter=' ', quotechar='|')
spamWriter.writerow(['Spam'] * 5 + ['Baked Beans'])
spamWriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
csvOut.close()