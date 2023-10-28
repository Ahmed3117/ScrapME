
# from bs4 import BeautifulSoup
# import requests
# import re
# def extract_resolution(url):
#     match = re.search(r'_AC_(\d+)_', url)
#     if match:
#         return int(match.group(1))
#     return 0
# url = 'https://www.amazon.com/SUUSON-Mount%E3%80%90Upgraded%E3%80%91-%E3%80%90Bumpy-Friendly%E3%80%91-Dashboard-Windshield/dp/B0CH14PBX9/ref=sr_1_8?qid=1698361379&s=electronics&sr=1-8'
# headers = {'User-Agent': '', 'Accept-Language': 'en-US, en;q=0.5'}
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')
# image_urls = soup.find_all('img')

# image_resolutions = [(img.get('src'), extract_resolution(img.get('src'))) for img in image_urls if img.get('src') and img.get('src').endswith(".jpg") and "_AC_" in img.get('src') and "https://m.media-amazon.com/images/I/" in img.get('src')]

# sorted_images = sorted(image_resolutions, key=lambda x: x[1], reverse=True)

# top_8_images = sorted_images[:8]

# selected_urls = [url for url, _ in top_8_images]
# for url in selected_urls:
#     url = re.sub(r'L\..*?\.', 'L.', url)
#     print(url)








import re
import requests
from bs4 import BeautifulSoup
import json

# URL of the web page you want to scrape
url = 'https://www.amazon.com/Samsung-970-EVO-Plus-MZ-V7S1T0B/dp/B07MFZY2F2/ref=pd_bxgy_img_sccl_1/142-9564931-5385363?content-id=amzn1.sym.43d28dfc-aa4f-4ef6-b591-5ab7095e137f&pd_rd_i=B07MFZY2F2&th=1'

headers = {'User-Agent': '', 'Accept-Language': 'en-US, en;q=0.5'}
response = requests.get(url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

image_urls = soup.select('#altImages ul li span span span span img')

replacement = "_AC_SL1500_"
for image in image_urls :
    image_url = image['src']
    image_url = image_url.replace("_AC_US40_", replacement)

    print(image_url)

