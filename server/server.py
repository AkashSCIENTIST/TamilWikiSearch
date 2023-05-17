from flask import Flask, request
import requests
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, support_credentials=True)


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
    return response.json()

@app.route('/', methods=['POST'])
@cross_origin(supports_credentials=True)
def submit_form():
    print(request.form.__dict__)
    tamil_text = request.form.get('tamil_text')
    english_text = request.form.get('english_text')
    return search(tamil_text, english_text)

if __name__ == "__main__":
    app.run()
