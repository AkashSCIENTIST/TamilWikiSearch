import requests
import os

folder_path = "./files2"

url = "http://localhost:4080/api/tamilwiki/_doc/{}"
data = {"name": "John", "age": 30}
username = "admin"
password = "admin"

for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        title = ".".join((filename.split("."))[:-1])
        print(title)
        full_path = folder_path + "/" + filename

        with open(full_path, encoding="utf-8") as f:
            content = f.read()
            data = {"title":title, "content":content}
            req_url = url.format(title)
            response = requests.put(req_url, json=data, auth=(username, password))

            if response.status_code == 200:
                print("PUT request successful for {}".format(title))
            else:
                print("Error:", response.status_code)
