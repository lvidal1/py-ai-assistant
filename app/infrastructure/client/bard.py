import requests


class bard:
    def __init__(self, api_key):
        self.api_key = api_key

    def prompt(self, text):
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "text/plain",
        }
        data = {"input": text}
        req = requests.post("https://api.bardapi.dev/chat", headers=headers, json=data)

        response = req.json()

        if "output" in response:
            return response["output"]
        else:
            return "Error"
