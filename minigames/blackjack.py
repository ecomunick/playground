import random

cards = []
suits = ['spades', 'clubs', 'hearts', 'diamonds']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

for s in suits:
    for r in ranks:
        #print([s, r])
        cards.append([s, r])

def shuffle():
    random.shuffle(cards)
    print("Deck shuffled!")  # Debugging: Confirm shuffle is called

#print(len(cards))

def deal(number):
    cards_dealt = []
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt

shuffle()  # Shuffle the deck before dealing
cards_dealt = deal(2)  # Deal 2 cards
card = cards_dealt[0]  # Get the first card
rank = card[1]  # Get the rank of the card

if rank == 'A':
    value = 11
elif rank in ['J', 'Q', 'K']:
    value = 10
else:
    value = int(rank)
    
rank_dict = {'rank': rank, 'value': value}


print(rank_dict['rank'], rank_dict['value'])
 

shuffle()
print(cards)  # Debugging: Check the shuffled deck
cards_dealt = deal(2)

""" # suit = suits[2]
# rank = 'K'
# value = 10
# print('Your card is: ' + rank + ' of ' + suit)
# suits.append('snakes')
# for suit in suits:
#     print(suit) """


