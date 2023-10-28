import math
import requests
from bs4 import BeautifulSoup
import re

def extract_resolution(url):
    match = re.search(r'_AC_(\d+)_', url)
    if match:
        return int(match.group(1))
    return 0

def scrapurl(url,code):
    product_category = ''
    product_name = ''
    product_description = ''
    product_price = None
    product_rate = None
    product_rate_number = None
    product_images = []
    product_images_urls = []
    if url == '':
        return (code,url,'None' ,'None', 'None', None, None, 'None', 'None')
    else:
        response = requests.get(url, headers={'User-Agent': '', 'Accept-Language': 'en-US, en;q=0.5'})
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            
            main_product_cat = soup.select('#wayfinding-breadcrumbs_feature_div ul li span a')[0].get_text().strip()
            product_cat = soup.select('#wayfinding-breadcrumbs_feature_div ul li span a')
            for category in product_cat:
                product_category = product_category + category.get_text().strip()+ ","
        except:
            pass
        try:
            product_name = soup.select('#productTitle')[0].get_text().strip()
        except:
            pass
        try:
            product_rate = soup.select('#acrPopover span a span')[0].get_text().strip()
        except:
            pass
        try:
            product_rate_number = soup.select('#acrCustomerReviewText')[0].get_text().strip()
        except:
            pass
        try:
            whole_price = soup.select('.a-price-whole')[0].get_text().strip()[:-1]
            fraction_price = soup.select('.a-price-fraction')[0].get_text().strip()
            product_price = whole_price + "." + fraction_price  # Combine whole and fraction parts
            product_price = product_price.replace(',', '')  # Remove commas
            product_price = float(product_price)  # Convert to float
            product_price = math.ceil(product_price)  # Convert to float
            # product_price = int(product_price)  # Convert to int
        except:
            pass
        try:
            product_description = ''
            product_desc = soup.select('#feature-bullets ul li span')[:-1]
            for desc in product_desc:
                product_description = product_description + desc.get_text() + ','
        except:
            pass
        try:
            # Find the script containing the JSON data
            # script = soup.find('script', string=lambda text: text and 'jQuery.parseJSON' in text)
            # data = script.text
            # data = data.strip()
            # pattern = re.compile(r"hiRes.*?jpg")
            # matches = pattern.findall(data)
            
            # for match in matches[:5]:
            #     link = match[8:]
            #     product_images_urls.append(link)
            
            image_urls = soup.select('#altImages ul li span span span span img')
            for image in image_urls[:6] :
                image_url = image['src']
                if image_url.endswith(".jpg"):
                    image_url = image_url.replace("_AC_US40_", "_AC_SL1500_")
                    product_images_urls.append(image_url)

            product_images_urls = set(product_images_urls)
            product_images_urls = list(product_images_urls)


        except:
            pass

        # old images way :

        # try:
        #     # product_images = soup.select('.imgTagWrapper img')
        #     # product_images_urls = [image['src'] for image in product_images]
        #     image_urls = soup.find_all('img')
        #     image_resolutions = [(img.get('src'), extract_resolution(img.get('src'))) for img in image_urls if img.get('src') and img.get('src').endswith(".jpg") and "_AC_" in img.get('src') and "https://m.media-amazon.com/images/I/" in img.get('src')]

        #     sorted_images = sorted(image_resolutions, key=lambda x: x[1], reverse=True)

        #     top_8_images = sorted_images[:8]

        #     selected_urls = [url for url, _ in top_8_images]
        #     for link in selected_urls:
        #         link = re.sub(r'L\..*?\.', 'L.', link)
        #         print(link)
        #         product_images_urls.append(link)

        # except:
        #     pass
        

        return code,url,main_product_cat, product_name, product_price, product_rate, product_rate_number, product_description[:-1],str(product_images_urls)
