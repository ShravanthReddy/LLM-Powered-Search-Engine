# Description: This file is the main file for the application. 
from search_engines import Search_engines

menu_options = ["Type to search", "Change default search engine", "Exit"]

def initiate_search(search_engine_obj):
    query = input("\nType to search: ")
    search_engine = search_engine_obj.get_search_engine()
    search_engine.search(query)
    print(f"\nSearch results for the query '{query}' are as follows:")
    print(search_engine.get_webpage_urls())

def change_search_engine(search_engine_obj):
    try:
        search_engine_idx = input(f"Please select the search engine you want to use: \n1. Bing\n2. Google\nCurrently selected engine: {search_engine_obj.currently_selected_engine}\nPlease enter the index of the search engine that you prefer: ")
        search_engine_idx = int(search_engine_idx)
    except Exception as e:
        if search_engine_idx.lower() == "menu":
            process_menu(menu, search_engine_obj)
        elif search_engine_idx.lower() == "exit":
            exit_func()

        print("Error: Invalid input. Please enter the serial number of the engine to continue.")
        search_engine_obj.change_search_engine()

def exit_func():
    print("\nThank you for tryin out the LLM powered Search Engine. Have a nice day! :)")
    exit()

def process_menu(menu_option, search_engine_obj):
    if menu_option == 1:
        initiate_search(search_engine_obj)

    elif menu_option == 2:
        change_search_engine(search_engine_obj)

    elif menu_option == 3:
        exit_func()

def menu():
    try:
        print("\nWelcome to the LLM powered Search Engine, please choose an option from the following menu:\n-------------------------------------------")
        for idx, option in enumerate(menu_options):
            print(f"{idx + 1}. {option}")

        menu_option = int(input("-------------------------------------------\nPlease enter the serial number of the option you want to select: "))
        
    except Exception as e:
        print("\n--------------------------------------------------------------------------------\nError: Invalid input. Please enter the serial number of the option to continue.\n--------------------------------------------------------------------------------")
        return menu()

    if menu_option not in range(1, len(menu_options) + 1):
        print("\n--------------------------------------------------------------------------------\nError: Invalid input. Please enter the serial number of the option to continue.\n--------------------------------------------------------------------------------")
        return menu()

    return menu_option

def main():
    search_engine_obj = Search_engines()
    menu_option = menu()
    process_menu(menu_option, search_engine_obj)

    # search_engine_obj.search("Picasso Biography")
    # print(search_engine_obj.get_webpage_urls())

if __name__ == "__main__":
    main()