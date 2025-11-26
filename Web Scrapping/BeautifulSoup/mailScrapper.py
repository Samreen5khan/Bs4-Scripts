import requests
from bs4 import BeautifulSoup
#Use BeautifulSoup documentation for referrence (crummy.com)


#open and read the html file and save in a variable
with open("BeautifulSoup/sample.html", "r") as file :
    html_doc = file.read()

