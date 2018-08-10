from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/Desktop-Memory/SubCategory/ID-147?Tid=7611'

# Opening connection, storing page, closing connection
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# Html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "item-container"})

filename = "products.csv"
f = open(filename, 'w')

headers = "Brand, Product_Name, Shipping Costs\n"

f.write(headers)


for container in containers:
    # grab brand name
    brand = container.div.div.a.img["title"]
    # grab item title
    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text
    # grab shipping costs
    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    # print data so far
    f.write(brand + "," + product_name.replace(",", "-") + "," + shipping + '\n')

f.close()






