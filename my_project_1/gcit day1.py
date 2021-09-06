# print("hello world")
#
# name=input("what is your name?")
# greetings = "hope you done good "+name
# print(greetings)
#
# nums = [3, 4, 6, 2, 7]
# nums.sort()
# print(nums[-2])
#
# nums=[1,2,3,4,4,9,7,4]
# x=int(input("enter the number:"))
# sum=0
# for i in nums:
#     if x==i:
#         sum=sum+i
# print(sum)

# import json
# my_example=open("C:/Users/darvi/Desktop/GCIT TRAINING/Training/my_project_1/example_1.json","r")
# my_example_1=my_example.read()
# obj=json.loads(my_example_1)
#
# print(str(obj["fruit"]))
# print(str(obj["color"]))
# print(str(obj["size"]))

# import requests
# from bs4 import BeautifulSoup
# url="https://www.cricbuzz.com/live-cricket-scorecard/32058/4th-test-india-tour-of-england-2021"
#
# r=requests.get(url)
# soup=BeautifulSoup(r.text,"html.parser")
# league_table =soup.find("class",class_="cb-col cb-col-100 cb-scrd-hdr-rw")
# print(league_table)

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'
requests.get(url)
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
print(soup)

table_data = soup.find('table', class_ = 'table table-striped table-bordered table-hover table-condensed table-list')

headers = []
for i in table_data.find_all('th'):
    title = i.text
    headers.append(title)

df = pd.DataFrame(columns = headers)

for j in table_data.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [tr.text for tr in row_data]
        length = len(df)
        df.loc[length] = row