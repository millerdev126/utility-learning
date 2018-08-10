from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/Desktop-Memory/SubCategory/ID-147?Tid=7611'

# Opening connection, storing page, closing connection
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# Html parsing
page_soup = soup(page_html, "html.parser")

print(page_soup.h1)


