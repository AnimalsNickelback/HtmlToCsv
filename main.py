from bs4 import BeautifulSoup
import csv
import os
import sys

print("Enter File to Parse")
file = input()

if os.path.isfile(file):
    htmlfile = open(file, 'r')
else:
    print("File not found. Check Path")
    sys.exit()

file_contents = htmlfile.read()

soup = BeautifulSoup(file_contents, "html.parser")

table = soup.find(id="ratings-table")

tableBody = table.tbody

masterList = []

# Iterating over every team
for item in tableBody.find_all('tr'):
    teamList = []

    # Iterating over every stat
    for stat in item.find_all('td'):
        if stat.find('a'):
            aContent = stat.find('a').contents[0]
            teamList.append(aContent)

        elif stat.find('span'):
            spanContent = stat.find('span').contents[0]
            teamList.append(spanContent)

        else:
            teamList.append(stat.contents[0])

    masterList.append(teamList)

finalList = []
for item in masterList:
    if item != []:
        finalList.append(item)


# Create csv
fields = ['Rank', 'Team', 'conf', 'W-L', 'NetRtg', 'ORtg', 'Seed', 'DRtg', 'Seed', 'AdjT', 'Seed', 'Luck',
          'Seed', 'NetRtg', 'Seed', 'ORtg', 'Seed', 'DRtg', 'Seed', 'NetRtg', 'Seed']

with open('teamRankings.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(finalList)



