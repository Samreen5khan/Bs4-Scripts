import requests
from bs4 import BeautifulSoup
import json

import xlsxwriter

# MoneyControl = requests.get("https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php")
url = "https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php"
MoneyControl = requests.get(url, 'https://api64.ipify.org?format=json')

#using an instant of beautiful soup
soup = BeautifulSoup(MoneyControl.text, "html.parser")
# print(soup.prettify())

# //class="TAL"
workbook = xlsxwriter.Workbook('MoneyControlGainer.xlsx')
worksheet = workbook.add_worksheet()
#This will scrap product details within a specific class
# table = soup.find('table', class_='TAL') 
# print(table)
# for child in soup.find_all(class_="data_table_ajax_loading"):

# Keep track of the current row
row_num = 0
col_num = 0

for tableHeading in soup.find_all("th"):
    # print(tableHeading)
    tableHeadingText = tableHeading.get_text(strip=True)
    worksheet.write(row_num, col_num, tableHeadingText)
    col_num += 1

row_num += 1
col_num = 0

# for CompanyName in soup.find_all("td", class_="PR"):
    
#     for title in CompanyName.find("a", attrs={'title': True}):
#     # print(tableHeading)
#         CompanyNameText = title.get_text(strip=True)
#         worksheet.write(row_num, col_num, CompanyNameText)
        
#         # CompanyName.find_all("td")
#         # for details in title.find("td"):
#             col_num =+ 1
#             Companydetails = details.get_text(strip=True)
#             worksheet.write(row_num, col_num, Companydetails)  

        # row_num += 1

# Loop through each row (tr) in the table
for row in soup.find_all("tr"):
    col_num = 0
    
    # Find the main company name td within the current row
    company_td = row.find("td", class_="PR")
    if company_td:
        # Find the <a> tag inside the company_td
        company_link = company_td.find("a", attrs={'title': True})
        if company_link:
            company_name_text = company_link['title']
            worksheet.write(row_num, col_num, company_name_text)
            col_num += 1
    
    # Find all other td tags within the same row
    other_details = row.find_all("td")[1:] # Get all td's from the second one onwards
    for detail_td in other_details:
        company_details = detail_td.get_text(strip=True)
        worksheet.write(row_num, col_num, company_details)
        col_num += 1

    row_num += 1

    
    

# for table in soup.find_all("table"):
 # Extract all the text from the table
    # table_text = table.get_text(strip=True)
    
    
    # print(table_text)

     # Write the text to the worksheet
    # worksheet.write(row_num, 0, table_text)

    # Move to the next row for the next table
    # row_num += 1
    # print(row_num)


        # print(result)
        # if(result != ""):
            # for row in enumerate(result):
                # worksheet.write(row, 0)
                # print("written")      
        
        # worksheet.write()
        # with open("MoneyControlGainer.txt", "a") as file :
            # file.write(result + "\n")   
            # print(result)


# worksheet.write('A1', 'Hello..')
# worksheet.write('B1', 'Geeks')
# worksheet.write('C1', 'For')
# worksheet.write('D1', 'Geeks')

workbook.close()


# data = []
# table = soup.find(class_="data_table_ajax_loading")

# for row in table.find_all('tr'):
    # cols = [td.get_text(strip=True) for td in row.find_all(['td', 'th'])] # Include 'th' for rows that might also contain headers
    # if cols: # Ensure the row is not empty
        # data.append(cols)

# print(data)

# with open("MoneyControlGainer.txt", "a") as file :
        # file.write(data)

print("Done")

