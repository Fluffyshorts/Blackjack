from card import Card
import random

class Deck:
    def __init__(this):
        this.Card = []
        for suit in Card.suit:
            for value in Card.value:
                this.Card.append(Card(suit, value))
    def shuffle(this):
        random.shuffle(this.Card)

    def deal(this):
        if len(this.Card) == 0:
            raise IndexError("Deck is empty")
        return this. Card.pop()
    
    def __str__(this):
        cardList = []
        for card in this.Card:
            cardList.append(str(Card))
            return "\n".join(cardList)