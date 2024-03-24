# Description: This file is the main file for the application. 
from search_engines import Search_engines

def main():
    search_engine_obj = Search_engines()
    search_engine_obj.search("Picasso Biography")
    print(search_engine_obj.get_webpage_urls())

if __name__ == "__main__":
    main()