import requests
from bs4 import BeautifulSoup

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

url = "https://www.amazon.in/s?k=iphone&crid=1WEAQ4Z662Q6U&sprefix=ip%2Caps%2C1255&ref=nb_sb_noss_2"

response = requests.get(url, 'https://api64.ipify.org?format=json')
#print(ipAddress.json())

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())
