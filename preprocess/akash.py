import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

def check(title):
    cnt = 0
    for i in title:
        if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return False
    return True

def search(from_, to, namespace):
    time.sleep(0.01)
    url = f'https://tamil.wiki/wiki/Special:AllPages?from={from_}&to={to}&namespace={namespace}'
    df = pd.DataFrame()
    href = []
    text_content = []

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        ul_tag = soup.find("ul", {"class": "mw-allpages-chunk"})
        li_tags = ul_tag.find_all("li")
        for li in li_tags:
            link = li.find('a')
            next = link.get("href")
            title = link.text
            # if check(link.text):
            href.append(next)
            text_content.append(title)
    except:
        pass

    if href != []:
        df['href'] = href
        df['Text content'] = text_content
        df.to_csv(f"{from_}_{to}_{namespace}.csv")
        print(f'{from_} {to} {namespace} yes')
    else:
        print(f'{from_} {to} {namespace}')

namespace = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '828', '829']
characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ஃ', 'அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ', 'க', 'க்ஷ', 'ச', 'ஜ', 'ஞ', 'ட', 'த', 'ந', 'ப', 'ம', 'ய', 'ர', 'ற', 'ல', 'ழ', 'வ', 'ஷ', 'ஸ', 'ஸ்ரீ', 'ஹ']

# for i in characters[12:20]:
#     for j in characters:
#         if i != j:
#             for k in namespace:
#                 search(i, j, k)

# search('ஹ', '', 0)
# search('ஃ', 'அ', 0)

for i in namespace[1:]:
    search('', '', i)

# for i in range(20, len(characters)):
#         search(characters[i], characters[i+1], 0)

# eng = "abcdefghijklmnopqrstuvwxyzஃ"

# for i in range(len(eng)-1):
#     search(eng[i], eng[i+1], 0)

# df = pd.DataFrame()
# href = []
# text_content = []

# url = "https://tamil.wiki/wiki/Main_Page_(English)"

# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# links = soup.find_all('a', {'class': 'external text'})

# for link in links:
#     href.append(link['href'])
#     text_content.append(link.text)

# df['href'] = href
# df['Text content'] = text_content
# df.to_csv("./_mwiki_mMain_Page_(English).csv")
