#Напишите однокарточную версию игры «Война», структура раунда в которой такова: все игроки mянут по одной
#карте, а выигрывает тот, у кого номинал карты оказывается наибольшим.

import cards, games

class War_Card(cards.Card):
    @property
    def value(self):
        if self.is_face_up:
            v = War_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
            if War_Card.RANKS.index(self.rank) == 0:
                v = 11
        else:
            v = None
        return v

class War_Deck(cards.Deck):
    def populate(self):
        for suit in War_Card.SUITS:
            for rank in War_Card.RANKS:
                self.cards.append(War_Card(rank, suit))

class War_Hand(cards.Hand):
    def __init__(self, name):
        super(War_Hand, self).__init__()
        self.name = name
    def __str__(self):
        rep = self.name + ":\t" + super(War_Hand, self).__str__() + str(self.total)
        return rep
    @property
    def total(self):
        t = 0
        for card in self.cards:
            t += card.value
        return t

class War_Player(War_Hand):
    def lose(self):
        print(self.name, "you lose")
    def win(self):
        print(self.name, "you won")
    def push(self):
        print(self.name, "it's a tie")


class War_Game(object):
    def __init__(self, names):
        self.players = []
        self.values = []
        for name in names:
            player = War_Player(name)
            self.players.append(player)
            #self.values.append(player.total)
        #for player in self.players:
            #print(player.total)
        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()
    def play(self):
        self.deck.deal(self.players, per_hand = 1)
        for player in self.players:
            print(player)
            self.values.append(player.total)
            #print(self.values)
        for player in self.players:
            if player.total == max(self.values):
                player.win()
            if player.total < max(self.values):
                player.lose()
    def end(self):
        for player in self.players:
            player.clear()
            self.deck.clear()
            self.deck = War_Deck()
            self.deck.populate()
            self.deck.shuffle()
            self.values = []
        """else:
            player.push()"""


def main():
    print("\t\tThis is WAR!\n")
    names = []
    number = games.ask_number("How many people will play? (1 - 5): ", low = 1, high = 6)
    for i in range(number):
        name = input("Your name: ")
        while name == "":
            name = input("Your name can't be empty. Input smth: ")
        while name in names:
            name = input("Your name can't be the same as someone else's. Input smth else: ")
        names.append(name)
    print()
    game = War_Game(names)
    again = None
    while again != "n":
        game.play()
        game.end()
        again = games.ask_yes_no("\nDo you wanna play again? ")
main()
input("\n\npress Enter to exit")