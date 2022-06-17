import random

class Card:
    """ drawers a card from the deck of cards with a value of 1 to 13
    The responsibility of the card is to keep track of the value of the current card and to drawer a new card when needed.

    Attributes:
        value (int): the value of the current card
        points (int): the number of points in the current card
    """

    def __init__(self):
        self.value = 0
        # self.points = 0

    def drawer(self):
        self.value = random.randint(1,13)

    def show(self):
        print(f"The card is: {self.value}")

        