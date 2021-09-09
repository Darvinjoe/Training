from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.cricbuzz.com/live-cricket-scorecard/32257/ind-vs-eng-2nd-test-england-tour-of-india-2021")

soup = BeautifulSoup(page.text)
# print(soup.prettify())
tbl = soup.find_all("div",class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[0]
# print(tbl.prettify())

names = [x.get_text() for x in tbl.find_all('div',class_="cb-col cb-col-27")]
# print(names)
player_names_1=[]
for i in names:
    player_names_1.append(i.strip())
print(player_names_1)

runs = [x.get_text() for x in tbl.find_all('div',class_="cb-col cb-col-8 text-right text-bold")]
player_runs_1=runs[1:]
print(player_runs_1)
x=input("enter the player name:")
x=x.capitalize()
# print(x)
for i in range(0,len(player_names_1)):
    if x==player_names_1[i]:
        print(f"The player name is {player_names_1[i]} and his first innings run is:{player_runs_1[i]}")


# print(soup.prettify())
tbl = soup.find_all("div",class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[4]
# print(tbl.prettify())

names = [x.get_text() for x in tbl.find_all('div',class_="cb-col cb-col-27")]
# print(names)
player_names_2=[]
for i in names:
    player_names_2.append(i.strip())
print(player_names_2)

runs = [x.get_text() for x in tbl.find_all('div',class_="cb-col cb-col-8 text-right text-bold")]
player_runs_2=runs[1:]
print(player_runs_2)
x=input("enter the player name:")
x=x.capitalize()
# print(x)
for j in range(0,len(player_names_2)):
    if x==player_names_2[j]:
        print(f"The player name is {player_names_2[j]} and his second innings run is:{player_runs_2[j]}")






