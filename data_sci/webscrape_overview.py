#Webscrape_overview

#necessary imports
import requests
from bs4 import BeautifulSoup

#url to scrape
url = 'https://www.bbc.co.uk/news'

#requesting the page
response = requests.get(url)

#store the page content
page_content = response.text

#parse the page content
soup = BeautifulSoup(page_content, 'html.parser')

#display a snippet of the HTML content
print(page_content[:500])

#find all <a> tages (anchor tags) in the HTML
links = soup.find_all('a')

#iterate over the links and print their text
for link in links:
    print(link.text)
    
#for table extraction use pandas read_html