import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find and print the title of the page
title = soup.find('title').get_text()
print('Page Title:', title)

# Find and print all the links on the page
for link in soup.find_all('a'):
    print('Link:', link.get('href'))