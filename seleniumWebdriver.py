from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
# import time
# from selenium. common. exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By

class Driver:
    def __init__(self) -> None:
        self.file_path = "./webpage.html"
        self.webdriver_service = Service('./ChromeDriver/chromedriver')
        self.driver = webdriver.Chrome(service=self.webdriver_service)
        self.html = ""
        
    def open_website(self, url):
        self.driver.get(url)
        self.parse_html()

    def parse_html(self):
        self.html = self.driver.page_source

    def get_html(self):
        return self.html