import os
import re
from pathlib import Path
from scrape_weather import weather_parser 
from extract_from_txt import text_to_email

import sched
import time


dir_work = str(Path(__file__).absolute())
len_main = len('\main.py')
dir_work = dir_work[:-len_main]

city_names = ["Toronto", "Peterborough", "Scarborough"]
#generate weather.txt file
text_file = dir_work + '\weather.txt'
email = "mohamed.azouz@ryerson.ca"
subject = "Weather in your Cities"



if __name__ == '__main__':
    weather_parser(city_names,dir_work)
    text_to_email(text_file,email,subject)




