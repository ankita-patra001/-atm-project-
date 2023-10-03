import os

def main():
    """
    Main function that checks if accounts file exists, 
    creates it if not, and launches the main menu.
    """
    
    # Check if accounts file exists, create it if not
    if not os.path.exists('accounts.txt'):
        print('Accounts file not found. Creating new file.')
        with open('accounts.txt', 'w') as accounts_file:
            pass
            
    # Import and launch the main menu function 
    import menu
    os.system('clear')
    print('Launching main menu...')
    menu.main_menu()


if __name__ == '__main__':
    main()
