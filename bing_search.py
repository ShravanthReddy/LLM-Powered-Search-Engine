import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
load_dotenv()

class Bing_search:
    def __init__(self):
        self.api_key = os.getenv("BING_SEARCH_API_KEY")
        self.url = os.getenv("URL")
        self.webpage_names = []
        self.webpage_urls = {}
        self.exclude_domains = ["google", "facebook", "twitter", "instagram", "youtube", "tiktok", "kremlin"]
        self.reqd_pages = 5
        self.default_pages = 7
        self.headers = {
            'Ocp-Apim-Subscription-Key': self.api_key,
        }
        self.params = {
            'q': "",
            'count': self.default_pages,
            'offset': 0,
            'mkt': 'en-us',
            'safesearch': 'Moderate',
        }

    def search(self, query):
        self.params['q'] = query
        self.make_request()

    def make_request(self):
        try:
            response = requests.get(
                self.url,
                headers=self.headers,
                params=self.params,
            )

            response.raise_for_status()
            webpage_urls = [result["url"] for result in response.json()["webPages"]["value"]]

            for webpage in webpage_urls:
                domain = urlparse(webpage).netloc
                web_page = domain.split('.')[1]
                if web_page not in self.exclude_domains:
                    self.webpage_names.append(web_page)
                    self.webpage_urls[self.webpage_names[-1]] = webpage

                if len(self.webpage_names) == self.reqd_pages:
                    break

        except Exception as e:
            print('An Error occurred:', str(e))

    def get_webpage_urls(self):
        return self.webpage_urls