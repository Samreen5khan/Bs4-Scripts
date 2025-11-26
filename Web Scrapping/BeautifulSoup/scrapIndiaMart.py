import requests
from bs4 import BeautifulSoup
import json

# IndimartPage = reques-ts.get("https://seller.indiamart.com/messagecentre") #

with open("BeautifulSoup/IndiaMart.html", "r") as file :
    IndimartPage = file.read()


#using an instant of beautiful soup
soup = BeautifulSoup(IndimartPage, "html.parse") #, "html.parser"


#This will scrap names (scrap using class names)
# for child in soup.find_all(class_="c_num"):
#     result = child.get_text()

#     with open("BeautifulSoup/result.txt", "a") as file :
#         file.write(result + "\n")

#This will scrap product details within a specific class
# for child in soup.find_all(class_="c-div"):
#     for product in child.find(class_="prdct_dsply"):
#         result= product.get_text()
#         with open("BeautifulSoup/result.txt", "a") as file :
#             file.write(result + "\n")   
            # print("written")

#This will scrap company name,city,state, country (code for tags)
# for child in soup.find_all("c_state"):
#     result = child.get_text()

#     with open("BeautifulSoup/result.txt", "a") as file :
#         file.write(result + "\n")


#This code will scrap mail using id selector : id="email_head"
# for child in soup.find_all(attrs={'id':'email_head_lv'}):
#     result = child
#     print(result)

#     with open("BeautifulSoup/result.txt", "a") as file :
#         file.write(result + "\n")


# print(result)
print("Done")
