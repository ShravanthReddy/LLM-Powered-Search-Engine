from seleniumWebdriver import Driver
from bs4 import BeautifulSoup

class HTML_parser:
    def __init__(self):
        self.driver = Driver()
        self.parsed_html = {} # key: url, value: html content

    def parse_html(self, webpage_urls):
        for key, val in webpage_urls.items():
            self.driver.open_website(val)
            html = self.driver.get_html()
            soup = BeautifulSoup(html, 'html.parser')
            self.parsed_html[val] = soup
            
        return self.parsed_html

