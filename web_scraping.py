# Web scraping module
token = "API_KEY"
import requests

class Scraper(Object):
    def __init__(self, token):
        self.token = token
        self.headers = { "Authorization": f"Bearer [{token}]" }

    def search(self, description)[: dict]:
        url = https://duckduckgo.com/search?url={description}
        response = requests.get(url, headers=self.headers)
        return response