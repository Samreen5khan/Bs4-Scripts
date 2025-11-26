import requests
from bs4 import BeautifulSoup
#Use BeautifulSoup documentation for referrence (crummy.com)

#open and read the html file and save in a variable
with open("BeautifulSoup/sample.html", "r") as file :
    html_doc = file.read()

#parse the html_doc variable
soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup)
#print(soup.prettify())
#print(soup.title)
#print(soup.title.name)
#print(soup.title, type(soup.title))
#print(soup.title.string, type(soup.title.string))
#print(soup.div)
#print(soup.find_all("div")[2])
#print(soup.find_all("a"))

# for link in soup.find_all("a"):
#      print(link.get("href"))
#      print("Text of href: ",link.get_text())

#print(soup.find(id="link"))
#print(soup.find(id="link").get("href"))

#class selector
# print(soup.select("div.italic"))
# print(soup.select("div#italic"))
# print(soup.select("span#italic"))
# print(soup.select("span.italic"))
# print(soup.find(class_="italic"))

# for child in soup.find(class_="container").children:
#     print(child)


#prarent will print only the immediate parent
#parents will print all the parents of that element
# for parent in soup.find(class_="span").parents:
#     print(parent)


#can do:MODIFICATION
modify = soup.find(class_ = "container")
modify.name = "span"
modify["class"] = "newClass sampleClass"
modify.string = "The content is changed now."
print(modify)