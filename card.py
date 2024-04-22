class Card:
    suit = ("Hearts \u2665", "Diamonds \u2666", "Spades \u2660", "Clubs \u2663")
    value  = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    
    def __init__(this, suit, value):
        if suit not in Card.suit or value not in Card.value:
            raise ValueError("Invalid card suit or value")
        this.suit = suit
        this.value = value
    def getValue(this):
        if this.value in ("J", "Q", "K"):
            return 10
        elif this.value == "A":
            return 11
        else:
            return int(this.value)
        
    def __str__(this):
        return f"{this.value} of {this.suit}"
            