from flask import Flask, request
import requests

app = Flask(__name__)

def search(tamil_text, english_text):
    print(tamil_text, english_text)
    url = "http://localhost:4080/api/tamilwiki/_search"
    search_text = tamil_text + " " + english_text
    username = "admin"
    password = "admin"
    data = {
        "search_type": "match",
        "query": {
            "term": search_text,
            "field": "_all"
        },
        "sort_fields": ["_score"]
    }
    response = requests.post(url, json=data, auth=(username, password))
    print(response)
    return response.json()

@app.route('/', methods=['POST'])
def submit_form():
    print(request.form.__dict__)
    tamil_text = request.form.get('tamil_text')
    english_text = request.form.get('english_text')
    return search(tamil_text, english_text)

if __name__ == "__main__":
    app.run()
