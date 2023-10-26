# import requests
# from bs4 import BeautifulSoup
# import json

# # Replace this URL with the Amazon product page URL you want to scrape.
# url = 'https://www.amazon.com/TCL-Unlocked-Android-Smartphone-Display/dp/B087LYQ22N/ref=sr_1_1_sspa?crid=17OSYBMPPLBAI&dchild=1&keywords=smartphone&qid=1611056472&s=electronics&sprefix=smart%2Celectronics-intl-ship%2C250&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWTVBTDNGWU9JR0pDJmVuY3J5cHRlZElkPUEwNDQ0MTQyMlRLVUE2MDFGSjhFQSZlbmNyeXB0ZWRBZElkPUEwMzE2MjI3MU1HMVlXSko2RjRTUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find the script tag containing the image data.
# script_tags = soup.select('script')
# print(script_tags)
# for script in script_tags:
#     # Check if the script tag contains the image data you need.
#     if 'colorImages' in str(script):
#         # Extract the image data from the script tag.
#         start_index = str(script).find('{"hiRes":')
#         end_index = str(script).rfind('}')
#         image_data = str(script)[start_index:end_index + 1]

#         # Convert the image data to a Python dictionary.
#         image_data_dict = json.loads(image_data)

#         # Iterate through the image data and print or save the image URLs.
#         for key, value in image_data_dict.items():
#             if 'hiRes' in value:
#                 print(f"Variant: {key}, URL: {value['hiRes']}")



##########################################################################################################
# good

# import time
# import requests

# # The URL of the web page you want to save
# url = 'https://www.amazon.com/TCL-Unlocked-Android-Smartphone-Display/dp/B087LYQ22N/ref=sr_1_1_sspa?crid=17OSYBMPPLBAI&dchild=1&keywords=smartphone&qid=1611056472&s=electronics&sprefix=smart%2Celectronics-intl-ship%2C250&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWTVBTDNGWU9JR0pDJmVuY3J5cHRlZElkPUEwNDQ0MTQyMlRLVUE2MDFGSjhFQSZlbmNyeXB0ZWRBZElkPUEwMzE2MjI3MU1HMVlXSko2RjRTUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
# max_retries = 3

# for retry in range(max_retries):
    
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         html_content = response.text
#         print(html_content)
#         with open('webpage.html', 'w', encoding='utf-8') as file:
#             file.write(html_content)
#         print(f'HTML source saved to webpage.html')
#         break
#     elif response.status_code == 503:
#         print(f'Retry {retry + 1}: Received a 503 error. Retrying in {2**retry} seconds.')
#         time.sleep(5**retry)
#     else:
#         print(f'Failed to retrieve the web page. Status code: {response.status_code}')
#         break



# from bs4 import BeautifulSoup
# import re

# import requests

# url = 'https://www.amazon.com/HP-Ryzen-5500U-Graphics-15-ef2099nr/dp/B0C1PQL8QB/ref=sr_1_10?qid=1698341913&s=computers-intl-ship&sr=1-10&th=1'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(response.text)
# # Load and parse the saved HTML source
# # with open('Amazon.com_ TCL 10L, Unlocked Android Smartphone with 6.53_ FHD + LCD Display, 48MP Quad Rear Camera System, 64GB+6GB RAM, 4000mAh Battery - Arctic White _ Cell Phones & Accessories.html', 'r', encoding='utf-8') as file:
# #     html_source = file.read()

# # soup = BeautifulSoup(html_source, 'html.parser')
# print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
# print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
# print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
# print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
# print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
# print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
# # Use a regular expression to find image URLs that start with "https," end with ".jpg," and contain "_AC"
# # image_urls = soup.select('#altImages ul li span span span span img')
# image_urls = soup.find_all('#ivLargeImage img')
# # image_urls = soup.find_all('img')
# print(image_urls)
# # Extract and print the matched image URLs
# # for img in image_urls:
# #     src = img['src']
# #     if src[-4:] == ".jpg":

# #             print( src)


import requests
from bs4 import BeautifulSoup

# URL of the web page you want to scrape
url = 'https://www.amazon.com/HP-Ryzen-5500U-Graphics-15-ef2099nr/dp/B0C1PQL8QB/ref=sr_1_10?qid=1698341913&s=computers-intl-ship&sr=1-10&th=1'

# Send a GET request to the URL
response = requests.get(url)
print(response.content)
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all img tags with class="a-dynamic-image"
img_tags = soup.find_all("img", class_="a-dynamic-image")

# Extract the source (src) attribute of each img tag
image_sources = [img["src"] for img in img_tags]

# Print the image sources
for source in image_sources:
    print(source)