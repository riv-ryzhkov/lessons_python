# pip install bs4



import requests
from bs4 import BeautifulSoup as BS
import csv
import time


###################################################################################
#
# for i in range(1, 5):
#     url = 'https://quotes.toscrape.com/page/{}'.format(i)
#     response = requests.get(url)
#
#     soup = BS(response.text, 'html.parser')
#     # print(type(soup))
#     # print(soup)
#
#     quotes = soup.find_all('span', class_='text')
#     # print(type(quotes))
#     # print(quotes)
#     authors = soup.find_all('small', class_='author')
#     tags = soup.find_all('div', class_='tags')
#     print('=' * 80)
#     for i in range(len(quotes)):
#         print(quotes[i].text)
#         print('Author: \t' + authors[i].text)
#         tagsforquote = tags[i].find_all('a', class_='tag')
#         print('tags:  \t\t#', end='')
#         for tagforquote in tagsforquote:
#             print(tagforquote.text, end=' #')
#         print()
#         print('=' * 80)

############################################################################
#
# url = 'https://www.bbc.com/ukrainian'
#
# page = requests.get(url)
#
# # if page.status_code != 200:
# #     print('No connection!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# #     a = input()
#
# print(page.status_code)
#
# soup = BS(page.text, 'html.parser')
#
#
# allNews = soup.find_all('div', attrs={'dir': 'ltr'})
# # print(allNews)
#
# for el in allNews:
#     pr = el.find_all('span')
#     for i in pr:
#         print(i.text)
#         print('='*80)





# ################################# olx ###################################
# def get_content(url):
#     resp = requests.get(url)
#     print(resp.status_code)
#     rows = []
#     # session = requests.session()
#     if resp.status_code == 200:
#         page = BS(resp.text, 'html.parser')
#         # print(page)
#         # breakpoint()
#         # table = page.find(id='offers_table')
#         table = page.find(id='listContainer')
#         # print('listContainer :', table)
#         # breakpoint()
#         tr_list = table.find_all('tr', attrs={'class': 'wrap'})
#         # print('class: wrap :', tr_list)
#         # breakpoint()
#         for tr in tr_list:
#             title_cell = tr.find('td', attrs={'class': 'title-cell'})
#             # print('class: title-cell', title_cell)
#             title = title_cell.find('h3')
#             # print(title)
#
#             title_text = title.text
#             title_text = title_text.replace('\n', '')
#             # print('title_text :', title_text)
#             href = title.a['href']
#             href = title.a['href'].replace(';promoted', '')
#             # print('ref: ', href)
#             # breakpoint()
#             td_price = tr.find('td', attrs={'class': 'td-price'})
#             price_str = td_price.text.replace('\n', '')
#             # print('price_str :', price_str)
#             price_temp = ''.join(c for c in price_str if c.isdigit())
#             if price_temp:
#                 price = int(price_temp)
#             else:
#                 price = 'договорная'
#             tmp = {'title': title_text, 'price_str': price_str, 'price': price, 'url': href}
#             # tmp = {'title': title_text, 'price': price, 'url': href}
#             rows.append(tmp)
#         return rows
#
#
# def parse_content(content):
#     csv_title = ['title', 'price_str', 'price', 'url']
#     print(csv_title)
#     with open('olx.csv', 'w', encoding='utf8') as f:
#         wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
#         wr.writeheader()
#         wr.writerows(content)
#
#
# # url = 'https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/komplektuyuschie-i-aksesuary/videokarty/'
# # url = 'https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/komplektuyuschie-i-aksesuary/videokarty/?page={}'
# # url = 'https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/komplektuyuschie-i-aksesuary/materinskie-platy/?page={}'
# url = 'https://m.olx.ua/elektronika/kompyutery-i-komplektuyuschie/komplektuyuschie-i-aksesuary/videokarty/?page={}'
#
# res = []
# for i in range(1, 2):
#     time.sleep(2)
#     res += get_content(url.format(i))
# for i in res:
#     for key, val in i.items():
#         print(key, val, sep='\t')
#     print('-' * 80)
# parse_content(res)
#

#############################################################################
############## PRICE.UA ХОЛОДИЛЬНИКИ / ПЛАНШЕТЫ #############################
# def get_content(url):
#     resp = requests.get(url)
#     print(resp.status_code)
#     rows = []
#     session = requests.session()
#     if resp.status_code == 200:
#         page = BS(resp.text, 'html.parser')
#         product = page.find(id='fluid-grid')
#         # list_products = product.find_all('div', attrs={'class': 'product-block type2 ga_container black-link-style split-4-cards is-model'})
#         list_products = product.find_all('div', attrs={'class': 'product-block'})
#         for div in list_products:
#             prod = div.find('div', attrs={'class': 'white-wrap'})
#             title = prod.a['title']
#             href = prod.a['href']
#             price_wrap = div.find('div', attrs={'class': 'price-wrap'})
#             price_str = price_wrap.text
#             price = [el for el in price_str if el.isdigit()]
#             price = int(''.join(price))
#             tmp = {'title': title, 'price_str': price_str, 'price': price, 'url': href}
#             rows.append(tmp)
#         return rows
#
# def parse_content(content):
#     csv_title = ['title', 'price_str', 'price', 'url']
#     # print(csv_title)
#     with open('price.csv', 'w', encoding='utf8') as f:
#         wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
#         wr.writeheader()
#         wr.writerows(content)
#
#
# url = 'https://price.ua/ua/catc371t2/page{}.html'
# # url = 'https://price.ua/ua/catc6399t2/page{}.html'
# res = []
# for i in range(1, 5):
#     time.sleep(2)
#     res += get_content(url.format(i))
# for i in res:
#     for key, val in i.items():
#         print(key, val, sep='\t')
#     print('-' * 60)
# parse_content(res)

###################################################################
############# SPORT.UA ############
#
# def get_content(url):
#     rows = []
#     page = requests.get(url)
#     print(page.status_code)
#     soup = BS(page.text, "html.parser")
#     news_line = soup.find(id='newsline')
#     allNews = news_line.findAll('div', 'item')
#     fav = input('Input your favorite sport in Ukrainian or "всі": ')
#     for data in allNews:
#         time_pub = data.find('span', attrs={'class': 'item-date'})
#         time_pub = time_pub.text.replace('\n', '').strip()
#
#         sport = data.find('span', attrs={'class': 'item-sport'})
#         sport = sport.text.replace('\n', '').strip()
#
#         title = data.a.text.replace('\n', '')
#         title = title.strip()
#
#         href = data.a['href']
#
#         if fav.lower() == sport.lower() or fav.lower() == 'всі':
#             print(time_pub)
#             print(sport)
#             print(title)
#             print(href)
#             print('=' * 60)
#             rows.append({'sport': sport, 'title': title, 'time of pub': time_pub, 'url': href})
#     return rows
#
# def parse_content(content):
#     csv_title = ['sport', 'title', 'time of pub', 'url']
#     print(csv_title)
#     # with open('sport.csv', 'w', encoding='utf8') as f:
#     with open('sport.csv', 'w') as f:
#         wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
#         wr.writeheader()
#         wr.writerows(content)
#
# url = 'https://new.sport.ua/uk'
# news = get_content(url)
# parse_content(news)

###################################################################















################################################################################
#### NEWS ######################################################################
###############################################################################
#
# url = 'http://mignews.com/mobile'
#
# page = requests.get(url)
# print(page.status_code)
# filteredNews = {}
# soup = BS(page.text, "html.parser")
# allNews = soup.findAll('div', class_='text-color-dark')
# # print(allNews)
# for data in allNews:
#     filteredNews[data.text.replace('\n', '')] = data.a['href']
# print('=' * 80)
# for key, vol in filteredNews.items():
#     print(key)
#     print(vol)
#     print('=' * 80)

#############################################


url = 'https://www.pravda.com.ua/'

page = requests.get(url)
print(page.status_code)
filteredNews = {}
soup = BS(page.text, "html.parser")
allNews = soup.findAll('div', class_="article_header")
# print(allNews)
for data in allNews:
    filteredNews[data.text.replace('\n', '')] = data.a['href']
print('=' * 80)
for key, vol in filteredNews.items():
    print(key)
    print(vol)
    print('=' * 80)
#################################################

# url ='https://sport.ua/uk'
#
# page = requests.get(url)
# print(page.status_code)
# soup = BS(page.text, "html.parser")
# news = soup.findAll('div', class_="main-news__item")
# print(news)
# for data in news:
#     text = data.img['alt']
#     href = data.a['href']
#     print(text)
#     print(href)
#     print('='*80)
#
#



######################################################3
#
# def get_links(url):
#     import requests
#     from bs4 import BeautifulSoup as soup
#     result = requests.get(url)
#     page = result.text
#     doc = soup(page, features='html.parser')
#     links = [element.get('href') for element in doc.find_all('a')]
#     return links
#
# urls = ['https://bottlepy.org/docs/dev/']
#
# for url in urls:
#     print('Links in', url)
#     for num, link in enumerate(get_links(url), start=1):
#         print(num, link)
#     print()

##########################################
#
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://quotes.toscrape.com/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# quotes = soup.find_all('span', class_='text')
# author = soup.find_all('small', class_='author')
# for i in range(len(quotes)):
#     print(quotes[i].text)
#     print('/', author[i].text, '/')
#     print('='*80)

# print(quotes)
# for quote in quotes:
#     print(quote.text)

################################################
#
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
#
# for n, i in enumerate(items, start=1):
#     itemName = i.find('h4', class_='card-title').text.strip()
#     itemPrice = i.find('h5').text
#     print(f'{n}:  {itemPrice} за {itemName}')


#####################################################
#
# url = 'https://www.bbc.com/ukrainian'
#
# page = requests.get(url)
# print(page.status_code)
# soup = BS(page.text, "html.parser")
# allNews = soup.find_all('div', attrs={'dir': 'ltr'})
# print(allNews)
# for el in allNews:
#     pr = el.find_all('span')
#     for i in pr:
#         print(i.text)
#         print('='*80)








