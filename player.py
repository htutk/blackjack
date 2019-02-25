from card import Card

# Player class keeps track of a player's house
class Player():
    def __init__(self, deck, card1, card2, hit_cards):
        self.deck = deck
        self.card1 = card1
        self.card2 = card2
        self.hit_cards = hit_cards
        self.turn_over = False
        self.busted = False
        self.blackjack = False
        self.has_ace_card = False

    def modify_card1(self, card1):
        self.card1 = card1

    # second card is dealt, check for blackjack
    def modify_card2(self, card2):
        self.card2 = card2
        self.check_one_ace()
        self.check_blackjack()

    def hit(self, new_hit_card):
        self.hit_cards.append(new_hit_card)
        self.check_one_ace()
        self.check_turn_over(self.total())

    def stand(self):
        self.turn_over = True

    # tallies up the total of the house
    def total(self):
        if not self.has_ace_card:
            two_cards_total = self.card1.get_number() + self.card2.get_number()
            hit_cards_total = 0
            for card in self.hit_cards:
                hit_cards_total += card.get_number()
            return two_cards_total + hit_cards_total
        else:
            return self.total_with_ace()

    def total_with_ace(self):
        temp_house = [self.card1, self.card2]
        temp_house.extend(self.hit_cards)

        total = 0;
        ace_count = 0;

        for card in temp_house:
            if card.get_number() == 1:
                ace_count += 1

        # 1, 11 for 1 Ace
        # 2, 12 for 2 Ace's
        # 3, 13 for 3 Ace's
        # 4, 14 for 4 Ace's
        amplifiers = [ace_count, ace_count + 10]

        total_not_ace = 0
        for card in temp_house:
            if card.get_number() != 1:
                total_not_ace += card.get_number()

        temp_total = []
        for amplifier in amplifiers:
             temp_total.append(total_not_ace + amplifier)

        if not self.blackjack and not self.busted:
            for t in temp_total:
                if t > 21:
                    temp_total.remove(t)
            total = max(temp_total)
        elif self.busted:
            total = min(temp_total)

        return total

    # turn is over if the house >= 21
    def check_turn_over(self, total):
        if total >= 21:
            self.turn_over = True
        if total == 21:
            self.blackjack = True
        if total > 21:
            self.busted = True

    def check_one_ace(self):
        self.has_ace_card = self.card1.get_number() == 1 or self.card2.get_number() == 1
        for hit_card in self.hit_cards:
            if hit_card.get_number() == 1:
                self.has_ace_card = True


    # internal function to check if a house is 21
    def check_blackjack(self):
        if self.has_ace_card:
            ace = self.card1 if self.card1.get_number() == 1 else self.card2
            other = self.card2 if self.card1.get_number() == 1 else self.card1

            if other.get_number() == 10:
                self.blackjack = True

    # for dealer to show the first card
    def show_one_card(self):
        return str(self.card1)

    # final condiiton of a house
    def final_answer(self):
        if self.blackjack:
            return 'BlackJack!'
        elif self.total() > 21:
            return str(self.total()) + ', Busted...'
        else:
            return str(self.total())

    # check if a player is tied with other player
    def __eq__(self, other):
        return self.final_answer() == other.final_answer()

    # check if a player's hand beats the other
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


# deal cards to all players including the dealer
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
