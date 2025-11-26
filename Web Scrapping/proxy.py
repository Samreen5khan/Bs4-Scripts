#ipaddress look up is the website to know the location of your device using ip addres
#use request module with proxy
import requests

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

#use Ipify (ip address api) to find get an ip address
ipAddress = requests.get('https://api64.ipify.org?format=json')
print(ipAddress.json())
