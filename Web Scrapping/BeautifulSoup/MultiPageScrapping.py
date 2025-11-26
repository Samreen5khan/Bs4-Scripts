import requests
from bs4 import BeautifulSoup

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}


# url = "https://www.instagram.com/explore/tags/makeup/"
# response = requests.get(url, 'https://api64.ipify.org?format=json')
# soup = BeautifulSoup(response.text, 'html.parser')
# code = soup.preserve_whitespace_tags

with open("BeautifulSoup/code.html", "r") as file :
    influencerList = file.readlines()
    print(influencerList)

# with open('BeautifulSoup/code.html', "w") as file:
#     file.write(soup.prettify())

print(influencerList.find(class_="_aagv"))

print("Done")