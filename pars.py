import requests
from bs4 import BeautifulSoup
from pprint import pprint
HOST = 'https://www.kivano.kg/'
URL = 'https://www.kivano.kg/noutbuki'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
def get_html(url,params=''):
    r = requests.get(url,headers=HEADERS,params=params,verify=False)
    return r
def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_="item product_listbox oh")
    anime = []
    for item in items:
        anime.append({
            'title':item.find('div',class_="listbox_title oh").get_text(strip=True),
            'price':item.find('div',class_="listbox_price text-center").get_text(strip=True)
        })
    return anime
html = get_html(URL)
file = open('anime.csv','a')
file.write(f'{get_content(html.text)}\n')
pprint(get_content(html.text))
