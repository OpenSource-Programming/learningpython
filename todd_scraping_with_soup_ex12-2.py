#!/usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

import requests

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# User input, if nothing then use default provided for the exercise
url = input('Enter - ')
if len(url) < 1: 
    url = "http://py4e-data.dr-chuck.net/comments_974077.html"

# Original method provided in class example
#html = urlopen(url, context=ctx).read()

#My method from research and using requests.get
html = requests.get(url)

soup = BeautifulSoup(html.content, "html.parser")

# Initialize vars to 0 for sum and count
comments_sum = 0
comments_count = 0

# Retrieve all span tags
tags = soup('span')
for tag in tags:    
    # This is the comments column and what we want to sum
    comments_sum += int(tag.contents[0])   
    comments_count += 1

print("Count", comments_count)
print("Sum", comments_sum)
