from bs4 import BeautifulSoup
import requests 
from lxml import etree #parses HTML content retrieved from the URL
import pandas as pd
url = 'https://www.scrapethissite.com/pages/simple/'

response=requests.get(url)

# response sends request and .txt retrieves raw data, done in html format
all_info = BeautifulSoup(response.text, 'lxml') 


country_info = all_info.find('div', class_ = 'col-md-4 country') #singlur section of country
all_country_info = all_info.find_all('div', class_ = 'col-md-4 country')# all countries info

# extracting titles and added one that had a different tag put these in list to add to columns
titles = country_info.find_all('strong')
table_titles = [title.text.strip() for title in titles]
table_titles.insert(0, 'Country Name:')
#print(table_titles)


rows = []

for element in all_country_info:

    country_name = element.find('h3', class_ ='country-name').text.strip()
    capital = element.find('span', class_ ='country-capital').text.strip()
    population = element.find('span', class_='country-population').text.strip()
    area = element.find('span', class_='country-area').text.strip()

    rows.append([country_name, capital, population, area])
#print(rows)

# puts my titles and data in dataframe
df = pd.DataFrame(columns =table_titles, data= rows)
print(df.head())

#puts dataframe into newly created cvs file and prevents df index field to be put as column in dvs
df.to_csv('output.csv', index=False, encoding='utf-8')

