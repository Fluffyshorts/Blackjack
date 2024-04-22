from card import Card
from deck import Deck

class Hand:
    def __init__(this):
        this.Card = []

    def hit(this, Card):
        this.Card.append(Card)

    def total(this):
        total = 0
        ace = False
        for Card in this.Card:
            total += Card.getValue() 
            if Card.value == "A":
                ace = True
        if ace and total > 21:
            total -= 10
        return total

class Game:
    def __init__(this):
        this.deck = Deck()
        this.player = Hand()
        this.dealer = Hand()

    def deal(this):
        for _ in range(2):
            this.player.hit(this.deck.deal())
            this.dealer.hit(this.deck.deal())

    def playerTurn(this):
        while True:
            print(f"DEALER'S SHOW CARD:\n{this.dealer.Card[0]}")
            print(f"\nYOUR CARDS:\n{' '.join([str(Card) for Card in this.player.Card])}")
            action = input("\nHit or stand? (hit/stand): ").lower()
            if action not in ("hit", "stand"):
                print("Invalid input. Please enter 'hit' or 'stand'.")
                continue
            if action == "stand":
                break
            this.player.hit(this.deck.deal())
            if this.player.total() > 21:
                print("You busted!")
                break

    def dealerTurn(this):
        while this.dealer.total() < 17:
            this.dealer.hit(this.deck.deal())

    def play(this):
        this.deck.shuffle()
        this.deal()
        this.playerTurn()
        this.dealerTurn()

        print(f"\nDEALER'S SHOW CARD:\n {' '.join([str(Card) for Card in this.dealer.Card])}")
        playerTotal = this.player.total()
        dealerTotal = this.dealer.total()

        if playerTotal > 21:
            print("\nYou lose.")
        elif dealerTotal > 21:
            print("\nDealer busted! You win!")
        elif playerTotal > dealerTotal:
            print("\nYou win!")
        elif playerTotal == dealerTotal:
            print("\nPush (tie).")
        else:
            print("\nYou lose.")

        while True:
            playAgain = input("Play again? (y/n): ").lower()
            if playAgain in ("y", "n"):
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        if playAgain == "y":
            this.play() 
        else:
            print("Bye!")


def main():
    print("Blackjack \n ----------------")
    game = Game()
    game.play()


if __name__ == "__main__":
    main()