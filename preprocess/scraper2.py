import pandas as pd #type: ignore
import requests #type: ignore
from bs4 import BeautifulSoup #type: ignore
import time
import os
from tqdm import tqdm #type: ignore

csv_files = os.listdir("missedouts")

def search(title):
    # time.sleep(0.01)
    # print(title)
    try:
        url = f'https://tamil.wiki/index.php?title={title.replace(" ", "_")}&action=edit'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = soup.find("textarea", {"id": "wpTextbox1"})
        val = text_content.text
        return val
    except:
        return "Permission error"

def solve(csvfile):
    dir = "missedouts"
    files = pd.read_csv(f"{dir}\\{csvfile}")
    del files["Unnamed: 0"]
    layer3 = {}
    for title in files['Text content']:
        layer3[title] = search(title)
    files["layer3"] = layer3
    files.to_csv(f"{dir}\\{csvfile}")
    return layer3

exlist = []

for csv_file in csv_files:
    layer3 = solve(csv_file)
    dir = "layer3_text"
    os.mkdir(f'{dir}\\{csv_file[:-4]}')
    print(csv_file)
    for title, value in layer3.items():
        print(csv_file, " => ", title)
        try:
            with open(f"{dir}\\{csv_file[:-4]}\\{title}.txt", 'w', encoding="utf-8") as file:
                file.write(layer3[title])
        except Exception as e:
            exlist.append(str(e))

print()
print(*exlist, sep="\n\n")
