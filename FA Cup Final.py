# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:48:03 2018

@author: Karim Noor Ali
"""

from bs4 import BeautifulSoup as soup #pip install bs4
import pandas as pd #pip install pandas
from selenium import webdriver #pip install selenium

chrome_path = r"F:\chromedriver.exe" #Download Chrome driver and specify the path
driver = webdriver.Chrome(chrome_path)

#Chelsea Data
url = 'https://us.soccerway.com/teams/england/chelsea-football-club/661/statistics/'
driver.get(url)

#First change the competition on the website to FA cup before continuing further
html = driver.page_source
html = soup(html,"html.parser")

Chl_Html = html.findAll("table",{"class":"table compare"})

Chl_preproc_odd = Chl_Html[0].findAll("tr",{"class":"first odd"})
Chl_preproc_even = Chl_Html[0].findAll("tr",{"class":"first even"})

i = 0
Labels = []
Chl_Stats = [] 
for stats in Chl_preproc_odd:
    label = stats.find("th").text
    Labels.append(label)
    number = stats.find("td").text
    Chl_Stats.append(number)
    label = Chl_preproc_even[i].find("th").text
    Labels.append(label)
    number = Chl_preproc_even[i].find("td").text
    Chl_Stats.append(number)
    if(i < 6):
        i+=1

del Labels[13:]
del Chl_Stats[13:]

Chl_Stats[10] = Chl_Stats[10].replace("m","")
Chl_Stats[11] = Chl_Stats[11].replace("m","")

Chl_Stats = list(map(float, Chl_Stats))

#*******************************Execute the above code first before continuing further*******************************

#For Manchester United Data
MU_url = 'https://us.soccerway.com/teams/england/chelsea-football-club/662/statistics/'
driver.get(MU_url)

#Change the competition on the opened website to FA cup before continuing further
MU_html = driver.page_source
MU_html = soup(MU_html,"html.parser")

MU_Html = MU_html.findAll("table",{"class":"table compare"})

MU_preproc_odd = MU_Html[0].findAll("tr",{"class":"first odd"})
MU_preproc_even = MU_Html[0].findAll("tr",{"class":"first even"})

j = 0
MU_Stats = [] 
for stats in MU_preproc_odd:
    number = stats.find("td").text
    MU_Stats.append(number)
    number = MU_preproc_even[j].find("td").text
    MU_Stats.append(number)
    if(j < 6):
        j+=1

del MU_Stats[13:]

MU_Stats[10] = MU_Stats[10].replace("m","")
MU_Stats[11] = MU_Stats[11].replace("m","")

MU_Stats = list(map(float, MU_Stats))

df = pd.DataFrame({"Label":Labels,"Chelsea Stats":Chl_Stats,"MU Stats":MU_Stats})

#Saving the data to Excel
df.to_excel('FA_Cup_Season_Stats.xlsx',columns=["Label","Chelsea Stats","MU Stats"],index=False)








