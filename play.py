from card import make_a_deck
from player import deal_cards
import random as r
import time

# shuffles the deck after each round
def new_round(deck):
    # shuffle for 10 times
    for i in range(10):
        r.shuffle(deck)

# player takes turn finalizing the house
def play_players(deck, players, dealer):
    dealer = dealer[0]
    print()

    # let each player finalize their house
    for i in range(len(players)):
        player = players[i]
        player_no = i + 1
        print('Dealer has {}'.format(dealer.show_one_card()))
        print('Player{} has {}'.format(player_no, player))
        print(player.final_answer())

        while not player.turn_over and not player.blackjack:
            action = input('Hit (H) or Stand (S): ').lower()
            while True:
                # hit
                if action.startswith('h'):
                    player.hit(deck.pop())
                    break
                # stand
                elif action.startswith('s'):
                    player.stand()
                    break
                else:
                    action = input('Hit (H) or Stand (S): ').lower()
            print(player)
            print(player.final_answer())
        print()

# dealer hits until the house hand is 17
def play_dealer(deck, players, dealer):
    dealer = dealer[0]
    print()
    print('Dealer has {}'.format(dealer))

    while not dealer.turn_over and not dealer.blackjack:
        # stand since the hosue is at least 17
        if dealer.total() >= 17:
            dealer.stand()
        else:
            print(dealer.final_answer())
            dealer.hit(deck.pop())
            print('Hitting', end='')
            for i in range(3):
                time.sleep(0.5)
                print('.', end='')
            print('\nDealer has {}'.format(dealer))

    print(dealer.final_answer())

# determines each player's winning condiiton
def final_play(deck, players, dealer):
    print()
    dealer = dealer[0]
    dealer_final = dealer.total()

    for i in range(len(players)):
        print()
        player = players[i]
        player_no = i + 1
        player_final = player.total()
        print('Player{} final: '.format(player_no) + player.final_answer())

        if (dealer == player):
            print('Player{}: '.format(player_no) + 'ties with the dealer.')
        elif (dealer > player):
            print('Player{}: '.format(player_no) + 'loses to the dealer.')
        else:
            print('Player{}: '.format(player_no) + 'beats the dealer.')
    print()


# prints out introductory prompts
def intro():
    print(r'''
Welcome to Blackjack game! Make your choices carefully.

    ''')

# main function to initialize a game
def play():
    intro()
    # make a new deck
    keep_playing = True

    while keep_playing:
        deck = make_a_deck()
        new_round(deck)

        # get the number of players from the user
        # 10 players allowed
        number_of_players = ''
        while not number_of_players.isdigit() or int(number_of_players) > 10:
            number_of_players = input('Enter the number of players (allowed 10): ')
        number_of_players = int(number_of_players)

        # +1 is to include the dealer
        players = deal_cards(deck, number_of_players + 1)

        # dealer is defined as a list since it will be referenced in other methods
        dealer = [players.pop()]
        play_players(deck, players, dealer)
        play_dealer(deck, players, dealer)
        final_play(deck, players, dealer)

        # ask whether to keep playing
        keep_playing_answer = input('Keep playing(Y/N)? ').lower()
        while True:
            if keep_playing_answer.startswith('y'):
                break
            elif keep_playing_answer.startswith('n'):
                keep_playing = False
                print('\n\nThanks for playing blackjack!')
                input('Press Enter close the window...\n')
                break
            else:
                keep_playing_answer = input('Keep playing(Y/N)? ').lower()
