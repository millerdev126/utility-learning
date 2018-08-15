"""
Tool for scraping product data from Newegg.com
It grabs data regarding category, brand, product name, shipping
and price for each page it looks at.

Current Issues: Doesn't seem to be running full code. Suspect
                 issue with pyCharm, and not the script. I've
                 commented out the document writing while I
                 troubleshoot the scraping issues.

Michael Miller
8/14/18
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


# Web pages respectively: RAM, Processors, Graphics Cards, Motherboards
my_url = ['https://www.newegg.com/Desktop-Memory/SubCategory/ID-147?Tid=7611',
          'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&IsNodeId=1&N=100007671%20601306869',
          'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48',
          'https://www.newegg.com/AMD-Motherboards/SubCategory/ID-22']
url_count = 0

# Open and prepare target file
filename = "products.csv"
f = open(filename, 'w')

headers = "Category, Brand, Product_Name, Shipping Costs, Price \n"

f.write(headers)


# Opening connection, storing page, closing connection
for url in my_url:
    uClient = uReq(my_url[url_count])
    page_html = uClient.read()
    uClient.close()
    url_count = 1 + url_count
    print(url_count)

    # Html parsing
    page_soup = soup(page_html, "html.parser")

    containers = page_soup.findAll("div", {"class": "item-container"})

    for container in containers:
        # grab category (same for most entries)
        category = page_soup.h1.text

        # grab brand name
        brand = container.div.div.a.img["title"]

        # grab item title
        title_container = container.findAll("a", {"class": "item-img"})
        img_text = str(title_container[0].img)
        product_name = img_text.partition('alt="')[2].partition('" src="')[0]

        # grab shipping costs
        shipping_container = container.findAll("li", {"class": "price-ship"})
        shipping = shipping_container[0].text.strip()

        # find price for each item
        site_price = container.findAll("li", {"class": "price-current"})
        final_price = site_price[0].text.strip()
        final_price = final_price.partition("$")[2].partition("(")[0]

        # print data so far
        '''
        print("Category: " + category)
        print("Brand: " + brand)
        print("Product Name: " + product_name)
        print("Shipping: " + shipping)
        print("Price: " + final_price)
        '''
        f.write(category + "," + brand + "," + product_name.replace(",", "-") + "," + shipping + "," + final_price + '\n')

f.close()
print("Done")






