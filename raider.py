import requests, threading #you need to pip install requests
url = "webhook url here"
send = "the message for the raid"

def function():
    requests.post(url,json={'content': send})

while True:
    function()
