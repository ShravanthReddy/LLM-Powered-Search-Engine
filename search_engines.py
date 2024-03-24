from bing_search import Bing_search

class Search_engines:
    def __init__(self) -> None:
        self.available_search_engines = ["Bing", "Google"]
        self.search_engine_objs = {self.available_search_engines[0]: Bing_search(), self.available_search_engines[1]: ""}
        self.currently_selected_engine = self.search_engine_objs[self.available_search_engines[0]]

    def get_search_engine(self):
        return self.currently_selected_engine

    def change_default_engine(self):
        try:
            search_engine_idx = int(input(f"Please select the search engine you want to use: \n1. Bing\n2. Google\nCurrently selected engine: {self.currently_selected_engine}\nPlease enter the index of the search engine that you prefer: "))
        except Exception as e:
            print("Error: Invalid input. Please enter the serial number of the engine to continue.")
            self.change_default_engine()

        if search_engine_idx < len(self.available_search_engines):
            self.currently_selected_engine = self.search_engine_objs[self.available_search_engines[search_engine_idx]]