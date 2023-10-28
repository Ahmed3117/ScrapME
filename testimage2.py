# from bs4 import BeautifulSoup


# with open('Amazon.com_ TCL 10L, Unlocked Android Smartphone with 6.53_ FHD + LCD Display, 48MP Quad Rear Camera System, 64GB+6GB RAM, 4000mAh Battery - Arctic White _ Cell Phones & Accessories.html', 'r', encoding='utf-8') as file:
#     html_source = file.read()
# soup = BeautifulSoup(html_source, 'html.parser')

# img_tags = soup.select('img')
# print(img_tags)
# for img in img_tags:
#     src = img.get('src')
#     if src:
#         print("Image URL:", src)

#------------------------------------------------------------
# perfect
# from bs4 import BeautifulSoup
# import requests

# url = 'https://www.amazon.com/dp/B0BXN5BJZP?ref_=sbi_dp_dk_cr_VFHHA_fs_nr&pf_rd_p=db0ef47b-9e9d-4e37-8d01-d8be849d8e24&pf_rd_r=D0E9Z6G53Q012F2HHP2P&pd_rd_wg=EECi5&pd_rd_i=Aur8Q&pd_rd_w=duFI1&content-id=amzn1.sym.db0ef47b-9e9d-4e37-8d01-d8be849d8e24&pd_rd_r=0Hv1Gq0xVuFyZ44lMGBw&th=1'
# headers = {'User-Agent': '', 'Accept-Language': 'en-US, en;q=0.5'}
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')
# image_urls = soup.find_all('img')

# for img in image_urls:
#     src = img.get('src')
#     if src:
#         if src.endswith(".jpg") and "_AC_" in src and "https://m.media-amazon.com/images/I/" in src:
#             print(src)

from bs4 import BeautifulSoup
import requests
import re
def extract_resolution(url):
    match = re.search(r'_AC_(\d+)_', url)
    if match:
        return int(match.group(1))
    return 0
url = 'https://www.amazon.com/SUUSON-Mount%E3%80%90Upgraded%E3%80%91-%E3%80%90Bumpy-Friendly%E3%80%91-Dashboard-Windshield/dp/B0CH14PBX9/ref=sr_1_8?qid=1698361379&s=electronics&sr=1-8'
headers = {'User-Agent': '', 'Accept-Language': 'en-US, en;q=0.5'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
image_urls = soup.find_all('img')

image_resolutions = [(img.get('src'), extract_resolution(img.get('src'))) for img in image_urls if img.get('src') and img.get('src').endswith(".jpg") and "_AC_" in img.get('src') and "https://m.media-amazon.com/images/I/" in img.get('src')]

sorted_images = sorted(image_resolutions, key=lambda x: x[1], reverse=True)

top_8_images = sorted_images[:8]

selected_urls = [url for url, _ in top_8_images]
for url in selected_urls:
    url = re.sub(r'L\..*?\.', 'L.', url)
    print(url)









# import requests

# # The URL of the web page you want to save
# url = 'https://www.amazon.com/TCL-Unlocked-Android-Smartphone-Display/dp/B087LYQ22N/ref=sr_1_1_sspa?crid=17OSYBMPPLBAI&dchild=1&keywords=smartphone&qid=1611056472&s=electronics&sprefix=smart%2Celectronics-intl-ship%2C250&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWTVBTDNGWU9JR0pDJmVuY3J5cHRlZElkPUEwNDQ0MTQyMlRLVUE2MDFGSjhFQSZlbmNyeXB0ZWRBZElkPUEwMzE2MjI3MU1HMVlXSko2RjRTUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# # Send an HTTP GET request to the URL
# response = requests.get(url, headers=headers)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Get the HTML content of the page
#     html_content = response.text

#     # Define a file name to save the HTML source
#     file_name = 'webpage.html'

#     # Open the file in write mode and save the HTML content
#     with open(file_name, 'w', encoding='utf-8') as file:
#         file.write(html_content)

#     print(f'HTML source saved to {file_name}')
# else:
#     print(f'Failed to retrieve the web page. Status code: {response.status_code}')
