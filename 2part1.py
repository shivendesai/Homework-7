#Written by Shiven Desai
import random

card_values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11
}

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def hit(self, card):
        self.hand.append(card)
        self.score += card_values[card[0]]

        # If the player busts, check for aces and adjust the score accordingly
        while self.score > 21:
            for card in self.hand:
                if card[0] == "A" and card_values["A"] == 11:
                    self.score -= 10
                    break
            else:
                break

    def show_hand(self, reveal=False):
        print(f"{self.name}'s hand:")
        if reveal:
            for card in self.hand:
                print(f"    {card}")
        else:
            print(f"    {self.hand[0]}")
            print("    [hidden card]")

    def get_score(self):
        return self.score

def main():
    # Initialize the deck
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = list(card_values.keys())
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)

    # Initialize the players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Deal the cards
    while len(deck) > 0:
        player1.hit(deck.pop())
        player2.hit(deck.pop())

        # Show the players' hands
        player1.show_hand()
        player2.show_hand()

        # Check for a winner
        if player1.get_score() > 21:
            print(f"{player2.name} wins!")
            break
        elif player2.get_score() > 21:
            print(f"{player1.name} wins!")
            break
        elif len(deck) == 0:
            if player1.get_score() > player2.get_score():
                print(f"{player1.name} wins!")
            elif player2.get_score() > player1.get_score():
                print(f"{player2.name} wins!")
            else:
                print("It's a tie!")
            break

if __name__ == "__main__":
    main()
