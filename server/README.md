Set basic authedication in call:
Username : ```admin```
Password : ```Complexpass#123```

Create New Index using 
```json
{
    "name": "tamilwiki",
    "storage_type": "disk",
    "shard_num": 3,
    "mappings": {
        "properties": {
            "title": {
                "type": "text",
                "index": true,
                "store": true,
                "highlightable": true
            },
            "content": {
                "type": "text",
                "index": true,
                "store": true,
                "highlightable": true
            }
        }
    }
}
```

in endpoint of ```POST``` ```http://localhost:4080/api/index```

Create new document : ```PUT``` ```http://localhost:4080/api/:target/_doc/:id```
here target is ```tamilwiki``` and id is document name