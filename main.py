import os, sys, platform
from src.query import Query

if platform.system() == 'Windows':
    clear = lambda: os.system('cls')

else:
    clear = lambda: os.system('clear')

def main(link):
    clear()
    while True:
        print('''
\033[1;36;40m=============
Made by SKane
=============

1. Firefox
2. Chrome
3. Exit
            ''')
        try:
            option = int(input('Option: '))
        except:
            print('The option must be an integer!')
            input('Press enter to continue...')
        if option > 3 or option < 1:
            print('Option must be either 1, 2, or 3!')
            input('Press enter to continue...')
        elif option == 3:
            break
        else:
            if option == 1:
                Query.ff(link)
            elif option == 2:
                Query.ch(link)

if __name__ == "__main__":
    main(sys.argv[1])
