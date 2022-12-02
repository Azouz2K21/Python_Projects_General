import requests

from bs4 import BeautifulSoup

import os


def weather_parser(cities , dir):
    completeName = os.path.join(dir, "weather" + ".txt")
    f = open(completeName, "w")


    url_li = []
    i=0
    for city in cities:
        url = "https://www.google.com/search?q=" + "weather " + city
        url_li.append(url) 
        html = requests.get(url).content

        soup = BeautifulSoup(html, 'html.parser')

        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
        time_skyDescription = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'})
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

        if temp is None or time_skyDescription is None or listdiv is None:
            continue
        temp = temp.text
        time_skyDescription = time_skyDescription.text
        
        data = time_skyDescription.split('\n')
        time = data[0]
        sky = data[1]
        strd = listdiv[5].text

        pos = strd.find('Wind')
        otherData = strd[pos:]
        temp_str = "The weather in " + cities[i] + " is:" + "\n" + str(temp) + "\n"
        time_str = "Time: " + str(time) + "\n\n\n"
        f.write(temp_str)
        f.write(time_str)
        i+=1

    f.close()






