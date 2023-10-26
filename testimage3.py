import requests
import time

url = 'https://www.amazon.com/TCL-Unlocked-Android-Smartphone-Display/dp/B087LYQ22N/ref=sr_1_1_sspa?crid=17OSYBMPPLBAI&dchild=1&keywords=smartphone&qid=1611056472&s=electronics&sprefix=smart%2Celectronics-intl-ship%2C250&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWTVBTDNGWU9JR0pDJmVuY3J5cHRlZElkPUEwNDQ0MTQyMlRLVUE2MDFGSjhFQSZlbmNyeXB0ZWRBZElkPUEwMzE2MjI3MU1HMVlXSko2RjRTUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
max_retries = 3
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

for retry in range(max_retries):
    response = requests.get(url, headers=headers)

    
    if response.status_code == 200:
        html_content = response.text
        with open('webpagee.html', 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f'HTML source saved to webpage.html')
        break
    elif response.status_code == 503:
        print(f'Retry {retry + 1}: Received a 503 error. Retrying in {2**retry} seconds.')
        time.sleep(2**retry)
    else:
        print(f'Failed to retrieve the web page. Status code: {response.status_code}')
        break
