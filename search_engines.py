from bing_search import Bing_search
from html_parser import HTML_parser

class Search_engines:
    def __init__(self) -> None:
        self.available_search_engines = ["Bing", "Google"]
        self.search_engine_objs = {self.available_search_engines[0]: Bing_search(), self.available_search_engines[1]: ""}
        self.currently_selected_engine = self.available_search_engines[0]

    def get_current_engine(self) -> str:
        return self.currently_selected_engine

    def change_default_engine(self, search_engine_idx) -> bool:
        if search_engine_idx - 1 < len(self.available_search_engines):
            self.currently_selected_engine = self.available_search_engines[search_engine_idx - 1]
            return True
        
        return False
    
    def search(self, query):
        return self.search_engine_objs[self.currently_selected_engine].search(query)
    
    def get_webpage_urls(self):
        return self.search_engine_objs[self.currently_selected_engine].webpage_urls
    
    def get_html(self):
        html_parser = HTML_parser()
        return html_parser.parse_html(self.get_webpage_urls())