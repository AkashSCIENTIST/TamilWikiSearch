from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/search")
def search(tamil_text: str = Form(...), english_text: str = Form(...)):
    print(tamil_text, english_text)
    url = "http://localhost:4080/api/tamilwiki/_search"
    search_text = tamil_text + " " + english_text
    username = "admin"
    password = "Complexpass#123"
    data = {
        "search_type": "match",
        "query": {
            "term": search_text,
            "field": "_all"
        },
        "sort_fields": ["_score"]
    }
    response = requests.put(url, json=data, auth=(username, password))
    return response.json()