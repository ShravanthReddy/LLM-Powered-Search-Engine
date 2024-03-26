from bs4 import BeautifulSoup
import requests
import re

class HTML_parser:
    def __init__(self):
        self.parsed_text = {} # key: url, value: html content

    def parse_html(self, webpage_urls, snippet):
        for key, val in webpage_urls.items():
            try:
                soup = BeautifulSoup(requests.get(val).content, 'html.parser')
                text = re.sub(r'\s+', ' ', soup.get_text()).strip()
                if not text:
                    text = snippet[key]

                self.parsed_text[val] = text
            except Exception as e:
                continue
            
        return self.parsed_text