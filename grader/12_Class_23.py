class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return '(' + self.value+' '+self.suit+')'
    def next1(self):
        v = self.value
        s = ''
        if self.suit == 'club':
            s = 'diamond'
        elif self.suit == 'diamond':
            s = 'heart'
        elif self.suit == 'heart':
            s = 'spade'
        else:
            s = 'club'
            if v=='J':
                v ='Q'
            elif v=='Q':
                v ='K'
            elif v=='K':
                v ='A'
            elif v=='A':
                v ='2'
            elif v=='10':
                v = 'J'
            else:
                v = str(int(v)+1)
        return Card(v,s)
    def next2(self):
        v = self.value
        s = ''
        if self.suit == 'club':
            s = 'diamond'
        elif self.suit == 'diamond':
            s = 'heart'
        elif self.suit == 'heart':
            s = 'spade'
        else:
            s = 'club'
            if v=='J':
                v ='Q'
            elif v=='Q':
                v ='K'
            elif v=='K':
                v ='A'
            elif v=='A':
                v ='2'
            elif v=='10':
                v = 'J'
            else:
                v = str(int(v)+1)
        self.value = v
        self.suit = s
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
