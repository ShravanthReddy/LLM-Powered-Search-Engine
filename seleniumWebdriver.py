from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class Driver:
    def __init__(self) -> None:
        self.file_path = "./webpage.html"
        self.options = Options()
        self.options.headless = False
        self.webdriver_service = Service('./ChromeDriver/chromedriver')
        self.driver = webdriver.Chrome(service=self.webdriver_service, options=self.options)
        self.html = ""
        
    def open_website(self, url):
        self.driver.get(url)
        self.parse_html()

    def parse_html(self):
        self.html = self.driver.page_source

    def get_html(self):
        return self.html