#!/usr/bin/env python
# coding: utf-8

# # Web Scraping Assignment

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# Importing liabraries

# In[307]:


# importing the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


# ## Que 1

# 1. Write a python program to display all the header tags from wikipedia.org and make data frame

# In[261]:


page=requests.get('https://en.wikipedia.org/wiki/Main_Page')
page


# In[262]:


#To get content of the website
soup= BeautifulSoup(page.content,"html.parser")
soup


# In[270]:


#getting Page content
Wiki_Content=BeautifulSoup(page.content) 


# In[272]:


wiki_header=[] #Creating a blank arrayList
for i in Wiki_Content.find_all('span',class_='mw-headline'):
    wiki_header.append(i.text)
wiki_header


# In[273]:


AllHeader=pd.DataFrame({'Wikipedia Page Headers':wiki_header})
AllHeader


# Another method

# In[266]:


headers = []


# In[267]:


#Find all the header tags in the HTML content using the find_all method
for header in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
    #Extracting data from headers
    text = header.text.strip()
    level = header.name
    headers.append((text, level))


# In[268]:


#Creating and printing dataframe of all headers
df = pd.DataFrame(headers, columns=["Text", "Level"])
print(df)


# ## Que 2

# 2. Write a python program to display list of respected former presidents of India(i.e. Name , Term ofoffice) from 
# https://presidentofindia.nic.in/former-presidents.htm and make data frame.

# In[275]:


page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page


# In[ ]:


# Response [404] means can not scrap data


# In[19]:


#To get content of the website
soup= BeautifulSoup(page.content,"html.parser")
soup


# In[40]:


page_title = soup.title


# In[41]:


page_head = soup.head


# In[42]:


print(page_title, page_head)


# In[83]:


#Find all the former presidents in the HTML content using the find method
former_pres=soup.find('div',class_='president-listing')
#or can use this syntax-: records=soup.find_all('span',attr={'class':'field-content'})
records


# In[59]:


#len(records)


# In[72]:


url='https://presidentofindia.nic.in/former-presidents'
response = requests.get(url)


# In[93]:


soup= BeautifulSoup(page.content,"html.parser")
soup


# In[73]:


presidents = []


# In[74]:


for president in soup.select("tbody tr"):
    name = president.select("td")[0].text.strip()
    term = president.select("td")[1].text.strip()
    presidents.append((name, term))


# In[76]:


header_tags = soup.find_all([ "h3", "h4", "h5"])


# In[77]:


df = pd.DataFrame(presidents, columns=["Name", "Term"])
print(df)


# ## Que. 3

# 3. Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team andrating.
# c) Top 10 ODI bowlers along with the records of their team andrating.

# # 3-a

# In[86]:


# Que 3-a
page=requests.get('https://www.cricketworldcup.com/')
page


# In[88]:


url='https://www.cricketworldcup.com/'


# In[89]:


response = requests.get(url)


# In[94]:


soup= BeautifulSoup(page.content,"html.parser")
soup


# In[90]:


teams = []


# In[91]:


for team in soup.select("tbody tr"):
    name = team.select("td")[1].text.strip()
    matches = team.select("td")[2].text.strip()
    points = team.select("td")[3].text.strip()
    rating = team.select("td")[4].text.strip()
    teams.append((name, matches, points, rating))


# In[92]:


df = pd.DataFrame(teams, columns=["Team", "Matches", "Points", "Rating"])# dataframe is created for team details
df = df.head(10)  # get only top 10 teams using head() method
print(df)


# # 3-b

# In[140]:


from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import requests


# In[126]:


url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

sauce = urllib.request.urlopen(url).read()

soup = BeautifulSoup(sauce,'html.parser')

p_name = []
country_name = []
rating = []


# In[127]:


# for the player in the banner ( first player)
player_1_block = soup.find('tr',attrs={'class':'rankings-block__banner'})
player_1_block_ranking_ = soup.find('div',attrs={'class':'rankings-block__banner--rating'}) 


# In[128]:


p_name.append(player_1_block.find('div',class_ = "rankings-block__banner--name-large").text)
country_name.append(player_1_block.find_all('div')[-2].text.strip('\n'))
rating.append(player_1_block_ranking_.text)


# In[129]:


table_rows = soup.find_all('tr',attrs={'class':'table-body'})


# In[296]:


for i in table_rows[:10]:
    p_name.append(i.find('a').text)
    country_name.append(i.find('span',class_="table-body__logo-text").text)
    rating.append(i.find('td',class_ ="table-body__cell rating").text)


# In[297]:


top_ten_men_batsmen= pd.DataFrame({'player_name': p_name,'country':country_name,'ranking': rating})
top_ten_men_batsmen


# # 3-c

# In[308]:


# Que 3-C
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import requests


url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}


# In[309]:



sauce = urllib.request.urlopen(url).read()

soup = BeautifulSoup(sauce,'html.parser')


# In[315]:


p_name = []
country_name = []
rating = []


# In[317]:



player_bowler = soup.find('tr',attrs={'class':'rankings-block__banner'})
player_bowler_ranking = soup.find('div',attrs={'class':'rankings-block__banner--rating'}) 

p_name.append(player_bowler.find('div',class_ = "rankings-block__banner--name-large").text)
country_name.append(player_bowler.find_all('div')[-2].text.strip('\n'))
rating.append(player_bowler_ranking.text)


# In[318]:


table_rows = soup.find_all('tr',attrs={'class':'table-body'})


# In[319]:


for i in table_rows[:10]:
    p_name.append(i.find('a').text)
    country_name.append(i.find('span',class_="table-body__logo-text").text)
    rating.append(i.find('td',class_ ="table-body__cell rating").text)


# In[320]:


#Created dataframe for top 10 odi men bowlers
df_top10_bowlers = pd.DataFrame({'player_name': p_name,'country':country_name,'ranking': rating})
df_top10_bowlers


# ## Que 4

#  Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# # 4-b

# In[250]:


women_team_url=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
women_top10_batting=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')
women_top10_allRouder=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')

women_team_url
women_top10_batting
women_top10_allRouder


# In[251]:


women_10_top_team=BeautifulSoup(women_team_url.content)
women_10_top_batting=BeautifulSoup(women_top10_batting.content)
women_10_top_allrounder=BeautifulSoup(women_top10_allRouder.content)


# In[252]:


#Top 10 ODI Batsmen
battingRating=[]

for i in women_10_top_batting.find('div',class_="rankings-block__banner--rating"):
    battingRating.append(i.text)

for i in women_10_top_batting.find_all('td',class_="table-body__cell u-text-right rating"):
    battingRating.append(i.text)


battingTeam=[]
battingTeam.append('AUS')
for i in women_10_top_batting.find_all('span',class_="table-body__logo-text"):
    battingTeam.append(i.text)

df=pd.DataFrame.from_dict({'Team':battingTeam[0:10],'Rating':battingRating[0:10]},orient='index')
top_10_batting=df.transpose()
top_10_batting


# # 4-a

# In[164]:


from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import requests


url = 'https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting'


# In[276]:


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}
sauce = urllib.request.urlopen(url).read()

soup = BeautifulSoup(sauce,'html.parser')


# In[166]:


p_name = []
country_name = []
rating = []


# In[167]:


# for the player in the banner ( No 1 player) using find method
player_1_block = soup.find('tr',attrs={'class':'rankings-block__banner'})
player_1_block_ranking_ = soup.find('div',attrs={'class':'rankings-block__banner--rating'}) 


# In[168]:


p_name.append(player_1_block.find('div',class_ = "rankings-block__banner--name-large").text)
country_name.append(player_1_block.find_all('div')[-2].text.strip('\n'))
rating.append(player_1_block_ranking_.text)


# In[169]:


table_rows = soup.find_all('tr',attrs={'class':'table-body'})


# In[170]:


for row in table_rows[:10]:
    p_name.append(row.find('a').text)
    country_name.append(row.find('span',class_="table-body__logo-text").text)
    rating.append(row.find('td',class_ ="table-body__cell rating").text)


# In[171]:


#Creating Dataframefro women-player name, country and ratings
df_womens_odi_players = pd.DataFrame({'player_name': p_name,'country':country_name,'ranking': rating})

df_womens_odi_players


# # 4-c

# In[174]:


from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import requests


url = 'https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

sauce = urllib.request.urlopen(url).read()

soup = BeautifulSoup(sauce,'html.parser')


# In[175]:


p_name = []
country_name = []
rating = []


# In[176]:


# for the player in the banner ( No 1 player) to get all head
player_1_block = soup.find('tr',attrs={'class':'rankings-block__banner'})
player_1_block_ranking_ = soup.find('div',attrs={'class':'rankings-block__banner--rating'}) 


# In[177]:


p_name.append(player_1_block.find('div',class_ = "rankings-block__banner--name-large").text)
country_name.append(player_1_block.find_all('div')[-2].text.strip('\n'))
rating.append(player_1_block_ranking_.text)


# In[178]:


table_rows = soup.find_all('tr',attrs={'class':'table-body'})


# In[179]:


for row in table_rows[:10]:
    p_name.append(row.find('a').text)
    country_name.append(row.find('span',class_="table-body__logo-text").text)
    rating.append(row.find('td',class_ ="table-body__cell rating").text)


# In[180]:


df_womens_odi_players = pd.DataFrame({'player_name': p_name,'country':country_name,'ranking': rating})

df_womens_odi_players


# # Que- 5

# Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make data frame-
# i) Headline
# ii) Time
# iii) News Link

# In[190]:


import requests
from lxml import html 
import pandas


# In[222]:


url="https://www.cnbc.com/world/?region=world"
page=requests.get("https://www.cnbc.com/world/?region=world")
page


# In[223]:


soup= BeautifulSoup(page.content,"html.parser")
soup


# In[226]:


cnbc_news=BeautifulSoup(page.content)


# In[227]:


#We are fetching all news under latest news section

Headline=[]
Time=[]
News_Link=[]

for i in cnbc_news.find_all('div',class_="LatestNews-headlineWrapper"):
    Headline.append(i.text.replace('2022',"Ago").split("Ago")[1])
    

    
for i in cnbc_news.find_all('time',class_="LatestNews-timestamp"):
    Time.append(i.text)

for i in cnbc_news.find_all('a',class_="LatestNews-headline"):
    News_Link.append(i['href'])
Latest_news=pd.DataFrame({'Headline':Headline,'Time':Time,'News Link':News_Link})
Latest_news


# # Que 6

# Write a python program to scrape the details of most downloaded articles from AI in last 90 days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles Scrape below mentioned details and make data frame-
# i) Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL

# In[278]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
import re


# In[279]:


article_url=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
article_url


# In[280]:


article_page=BeautifulSoup(article_url.content)


# In[283]:


paper_title=[]
authors=[]
publishedDate=[]
paperUrl=[]


for i in article_page.find_all('h2',class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR"):
    paper_title.append(i.text)

for i in article_page.find_all('span',class_="sc-1w3fpd7-0 pgLAT"):
    authors.append(i.text)
    
for i in article_page.find_all('span',class_="sc-1thf9ly-2 bKddwo"):
    publishedDate.append(i.text)

# find all the anchor tags with "href" 
# attribute starting with "https://"
for i in article_page.find_all('a',attrs={'href': re.compile("^https://")},class_="sc-5smygv-0 nrDZj"):
    paperUrl.append(i.get('href'))


# In[285]:


Ai_article=pd.DataFrame({'Paper Title':paper_title,'Authors':authors,'Published Date':publishedDate,'Paper URL':paperUrl})
Ai_article


# # Que 7

# Write a python program to scrape mentioned details from dineout.co.in and make data frame-
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[287]:


dine_url=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
dine_url


# In[288]:


dineout_page=BeautifulSoup(dine_url.content)


# In[289]:


RestaurantName=[]
Cuisine=[]
Location=[]
Ratings=[]
ImageURL=[]

for i in dineout_page.find_all('div',class_="restnt-info cursor"):
    RestaurantName.append(i.text)

for i in dineout_page.find_all('span',class_="double-line-ellipsis"):
    Cuisine.append(i.text.split("|")[1])

for i in dineout_page.find_all('div',class_="restnt-loc ellipsis"):
    Location.append(i.text)

for i in dineout_page.find_all('div',class_="restnt-rating rating-4"):
    Ratings.append(i.text)

for i in dineout_page.find_all('img',class_="no-img"):
    ImageURL.append(i['data-src'])


# In[293]:


Dineout=pd.DataFrame({'Restaurant name':RestaurantName,'Cuisine':Cuisine,'Location':Location,'Ratings':Ratings,'Image URL':ImageURL})
Dineout


# In[ ]:




