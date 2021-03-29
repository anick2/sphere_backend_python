import json
from datetime import datetime

def app(environ, start_response):
    
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    url = environ['HTTP_HOST'] + environ['PATH_INFO']

    data = json.dumps({"time": now, "url": url})
    bdata = bytes(data, 'utf-8')
    
    start_response("200 OK", [
        ("Content-Type", "application/json")
    ])
    
    return [bdata]
