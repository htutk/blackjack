from play import play
import sys

def main():
    play()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        #print('\nThanks for playing blackjack!')
        sys.exit('\nThanks for playing blackjack!')
