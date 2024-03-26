from search_engines import Search_engines

menu_options = ["Type to search", "Change default search engine", "Exit"]

# Function to initiate the search
def initiate_search(search_engine):
    while True:
        query = input("\nType to search: ")
        if query.lower() == "exit":
            exit_func()
        if query.lower() == "menu": 
            process_menu(menu(), search_engine)

        is_search_success = search_engine.search(query)
        if is_search_success:
            print(search_engine.get_html())

# Function to change the currently selected search engine
def change_search_engine(search_engine):
    try:
        # Get the index of the search engine that the user wants to use from the available one's
        search_engine_idx = input(f"Please select the search engine you want to use: \n1. Bing\n2. Google\nCurrently selected engine: {search_engine.get_current_engine()}\nPlease enter the index of the search engine that you prefer: ")
        # Convert the index to an integer
        search_engine_idx = int(search_engine_idx)

    except Exception as e:
        # If the user enters menu or exit, then process the menu or exit function
        if search_engine_idx.lower() == "menu":
            process_menu(menu(), search_engine)
        elif search_engine_idx.lower() == "exit":
            exit_func()
        # If the user enters an invalid input, then prompt the user to enter the correct input
        print("Error: Invalid input. Please enter the serial number of the engine to continue.")

    # Change the default search engine to the one selected by the user
    is_changed = search_engine.change_default_engine(search_engine_idx)
    # If the search engine is changed successfully, then print the success message
    if is_changed:
        print("Success! Search engine changed to: ", search_engine.get_current_engine())
        process_menu(menu(), search_engine)

    # If the search engine is not changed successfully, then print the error message
    else:
        print("\nError: Invalid input. Please enter the correct serial number to continue.")
        process_menu(menu(), search_engine)

# Function to exit the application
def exit_func():
    print("\nThank you for tryin out the LLM powered Search Engine. Have a nice day! :)")
    exit()

# Function to process the menu option selected by the user
def process_menu(menu_option, search_engine):
    if menu_option == 1:
        initiate_search(search_engine)

    elif menu_option == 2:
        change_search_engine(search_engine)

    elif menu_option == 3:
        exit_func()

# Function to display the menu options to the user
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
    search_engine = Search_engines()
    menu_option = menu()
    process_menu(menu_option, search_engine)

if __name__ == "__main__":
    main()