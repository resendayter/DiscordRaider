import requests, threading #you need to pip install requests
url = "webhook url here"
send = "the message for the raid"

while True:
    def function():
        requests.post(url,json={'content': send})
    function()
