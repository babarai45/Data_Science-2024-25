# web scraping using BeautifulSoup

import requests 
# requests is a Python module that you can use to send all kinds of HTTP requests.
#  It is an easy-to-use library with a lot of features ranging from passing parameters 
# in URLs to sending custom headers and SSL Verification.

from bs4 import BeautifulSoup
# BeautifulSoup is a Python library for parsing HTML and XML documents.
# It creates parse trees that is helpful to extract the data easily.

url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'
response = requests.get(url) # get the response from the url like opening the url in browser
print(response.status_code) # 200 means success
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

# print(soup.title)
# print(soup.title.string)
# print(soup.a