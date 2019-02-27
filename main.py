from play import play
from time import sleep
import sys

def main():
	try:
		play()
	except KeyboardInterrupt:
		print('\n\nThanks for playing blackjack!')
		input('Press Enter to close the window...\n')


if __name__ == '__main__':
	main()