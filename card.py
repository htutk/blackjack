import random as r

# class Card to make a card object
class Card():
    def __init__(self, number, suite):
        self.number = number
        self.suite = suite
        self.face_cards = ['Jack', 'Queen', 'King']
        self.suite_dict = {'Spade': u'\u2660', 'Heart': u'\u2666', \
        'Diamond': u'\u2665', 'Club': u'\u2663'}

    def modify_number(self, number):
        self.number = number

    def modify_suite(self, suite):
        self.suite = suite

    def get_number(self):
        if self.number in self.face_cards:
            return 10
        elif self.number == 'Ace':
            return 1
        else:
            return int(self.number)

    def get_suite(self):
        return self.suite

    def __str__(self):
        return self.number + ' ' + self.suite_dict[self.suite]

    __repr__ = __str__

# make a new deck, and returns as 52 cards
def make_a_deck():
    suites = ['Spade', 'Heart', 'Diamond', 'Club']
    numbers = ['Ace']
    numbers.extend([str(i) for i in range(2, 11)])
    numbers.extend(['Jack', 'Queen', 'King'])

    number_of_cards = 52
    deck = []

    suite_loop = int(number_of_cards / len(suites))
    number_loop = int(number_of_cards / len(numbers))

    for loop in range(number_loop):
        for number in numbers:
            new_card = Card(number, "")
            deck.append(new_card)

    for loop in range(number_loop):
        suite = suites[loop]
        for i in range(len(numbers)):
            card_index = loop * suite_loop + i
            current_card = deck[card_index]
            current_card.modify_suite(suite)
    return deck
