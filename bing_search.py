import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
from bs4 import BeautifulSoup

load_dotenv()

# Class to search for webpages using Bing Search API
class Bing_search:
    def __init__(self):
        self.api_key = os.getenv("BING_SEARCH_API_KEY")
        self.url = os.getenv("URL")
        self.webpage_names = [] # List to store the names of the webpages
        self.webpage_urls = {} # Dictionary to store the names of the webpages as keys and their URLs
        self.exclude_domains = ["google", "facebook", "twitter", "instagram", "youtube", "tiktok", "kremlin"] # List of domains to exclude from the search results
        self.reqd_pages = 5 # Number of pages to search for
        self.default_pages = 7 # Number of pages to search for by default
        self.headers = { # Headers for the request
            'Ocp-Apim-Subscription-Key': self.api_key,
        }
        self.params = { # Parameters for the request
            'q': "",
            'count': self.default_pages,
            'offset': 0,
            'mkt': 'en-us',
            'safesearch': 'Moderate',
        }

    # Function to search for the query
    def search(self, query):
        self.params['q'] = query
        response, is_valid = self.make_request()
        print(response, is_valid)
        if is_valid:
            self.process_response(response)

        return is_valid

    # Function to make the request to the Bing Search API
    def make_request(self):
        try:
            response = requests.get(
                self.url,
                headers=self.headers,
                params=self.params,
            )

            response.raise_for_status()
            return response.json(), True

        except Exception as e:
            print("Error: Search failed! ", e)
            return None, False
        
    def process_response(self, response):
        webpage_urls = [result["url"] for result in response["webPages"]["value"]]
        for webpage in webpage_urls:
            print(webpage)
            domain = urlparse(webpage).netloc
            domain_split = domain.split('.')
            if len(domain_split) > 2:
                web_page = domain_split[1]
            else:
                web_page = domain_split[0]

            if web_page not in self.exclude_domains and web_page not in self.webpage_names:
                self.webpage_names.append(web_page)
                self.webpage_urls[self.webpage_names[-1]] = webpage

            if len(self.webpage_names) == self.reqd_pages:
                break

    # Function to get the webpage URLs
    def get_webpage_urls(self):
        return self.webpage_urls