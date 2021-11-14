class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit   
    def __str__(self):
        return '(' + self.value+' '+self.suit+')'
    def getScore(self):
        if self.value == 'A':
            return 1
        elif self.value in ['J','Q','K']:
            return 10
        else:
            return int(self.value)
    def sum(self, other):
        return (self.getScore() + other.getScore() )%10
    def __lt__(self, rhs):
        D = dict()
        D['club'] = 1
        D['diamond']=2
        D['heart']=3
        D['spade']=4
        scoreA = self.getScore()
        if self.value == 'J':
            scoreA  =11
        elif self.value == 'Q':
            scoreA  =12
        elif self.value == 'K':
            scoreA  =13
        
        if scoreA <= 2 :
            scoreA +=13
        scoreB = rhs.getScore()
        if rhs.value == 'J':
            scoreB  =11
        elif rhs.value == 'Q':
            scoreB  =12
        elif rhs.value == 'K':
            scoreB  =13
        if scoreB <= 2:
            scoreB += 13
        scoreA = scoreA * 5 + D[self.suit]
        scoreB = scoreB * 5 + D[rhs.suit]
        return scoreA < scoreB
        
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])