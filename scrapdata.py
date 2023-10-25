import requests
from bs4 import BeautifulSoup

def scrapurl(url):
    if url == '':
        return (url, 'None', 'None', None, None, 'None', 'None')

    product_name = 'None'
    product_description = 'None'
    product_price = None
    product_rate = None
    product_rate_number = None
    product_images = []
    product_images_urls = []

    response = requests.get(url, headers={'User-Agent': '', 'Accept-Language': 'en-US, en;q=0.5'})
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        product_description = ''
        product_desc = soup.select('#feature-bullets ul li span')[:-1]
        for desc in product_desc:
            product_description = product_description + desc.get_text() + ','
    except:
        pass
    try:
        product_price = soup.select('.a-price-whole')[0].get_text().strip()
    except:
        pass
    try:
        product_images = soup.select('.imgTagWrapper img')
        product_images_urls = [image['src'] for image in product_images]
    except:
        pass

    return url, product_price, product_description[:-1], str(product_images_urls)
