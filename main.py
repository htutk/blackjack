from play import play
from time import sleep
import sys

def main():
    play()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        #print('\nThanks for playing blackjack!')
        print('\n\nThanks for playing blackjack!')
        input('Press Enter to close the window...\n')
