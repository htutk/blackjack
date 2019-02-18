from card import Card

class Player():
    def __init__(self, deck, card1, card2, hit_cards):
        self.deck = deck
        self.card1 = card1
        self.card2 = card2
        self.hit_cards = hit_cards
        self.turn_over = False
        self.blackjack = False

    def modify_card1(self, card1):
        self.card1 = card1

    def modify_card2(self, card2):
        self.card2 = card2
        self.check_blackjack()

    def hit(self, new_hit_card):
        self.hit_cards.append(new_hit_card)
        self.check_turn_over(self.total())

    def stand(self):
        self.turn_over = True

    def total(self):
        two_cards_total = self.card1.get_number() + self.card2.get_number()
        hit_cards_total = 0
        for card in self.hit_cards:
            hit_cards_total += card.get_number()
        return two_cards_total + hit_cards_total

    def check_turn_over(self, total):
        if total >= 21:
            self.turn_over = True
        if total == 21:
            self.blackjack = True

    def check_blackjack(self):
        has_ace_card = self.card1.get_number() == 1 or self.card2.get_number() == 1
        if not has_ace_card:
            self.blackjack = False
        else:
            ace = self.card1 if self.card1.get_number() == 1 else self.card2
            other = self.card2 if self.card1.get_number() == 1 else self.card1

            if other.get_number() == 10:
                self.blackjack = True

    def show_one_card(self):
        return str(self.card1)

    def final_answer(self):
        if self.blackjack:
            return 'BlackJack!'
        elif self.total() > 21:
            return 'Busted...'
        else:
            return str(self.total())

    def __eq__(self, other):
        return self.final_answer() == other.final_answer()

    def __gt__(self, other):
        if not self.blackjack and other.blackjack:
            return False
        elif self.blackjack:
            return True
        elif self.total() > 21 and other.total() <= 21:
            return False
        elif self.total() <= 21 and other.total() > 21:
            return True
        else:
            return self.total() > other.total()

    def __lt__(self, other):
        return not __gt__(self, other)

    def __str__(self):
        result = [str(self.card1), str(self.card2)]
        for hit_card in self.hit_cards:
            result.append(str(hit_card))

        return str(result)

    __repr__ = __str__


def deal_cards(deck, number_of_players):
    players = []
    for i in range(number_of_players):
        players.append(Player(deck, Card("", ""), Card("", ""), []))

    # deal first card
    for player in players:
        player.modify_card1(deck.pop())

    # deal second card
    for player in players:
        player.modify_card2(deck.pop())

    return players
