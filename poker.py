# -----------
# User Instructions
# 
# Write a function, allmax(iterable, key=None), that returns
# a list of all items equal to the max of the iterable, 
# according to the function specified by key. 


import random # this will be a useful library for shuffling

import itertools #for combination 

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

playerNames = {1:"James Bond", 2: "Naruto Uzumaki", 3: "Monkey D. Luffy", 4: "Sherlock Holmes", 5: "Bruce Wayne"}

def best_hand(hand,bestOf):
    "From a 7-card hand, return the best 5 card hand."
    comb = list(itertools.combinations(hand,bestOf))
    
    return max(comb,key=hand_rank)


def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    # Your code here.    
    hand_ranks =[hand_rank(hand) for hand in iterable]
    maxHand = max(hand_ranks,key=lambda hand_ranks: hand_ranks[:-1])
    return [(hand,maxHand[-1]) for hand in iterable if maxHand == hand_rank(hand)] 
    

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks),'Straight Flush')
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks),'Four of a Kind')
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks),'Full House')
    elif flush(hand):
        return (5, ranks,'Flush')
    elif straight(ranks):
        return (4, max(ranks),'Straight')
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks,'Three of a Kind')
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks,'Two Pair')
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks,'One Pair')
    else:
        return (0, ranks,'High Card')

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has exactly n-of-a-kind of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    "If there are two pair here, return the two ranks of the two pairs, else None."
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

def deal(numhands, n=5, deck=mydeck):
    # Your code here.
    hands =  []
    for i in range(0,numhands):
        hands.append(random.sample(mydeck,n))
    return hands

def test():
    "Test cases for the functions in poker program."
    sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
    sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2] 
    return 'tests pass'


if __name__ == "__main__":
    numberOfPlayers = int(raw_input("Enter number of players: "))
    cardsEachHand = int(raw_input("Enter number of cards per hand: "))
    bestOf = int(raw_input("Enter best of number of cards per hand: "))
    hands = deal(numberOfPlayers,cardsEachHand)
    playerHands = {} 
    for num,hand in zip(random.sample([x for x in range(1,6)],numberOfPlayers),hands):
        playerHands[num] = best_hand(hand,bestOf)
    winners =  poker(playerHands.values())
    print [ playerNames[name]+ " won with " + winner[-1] for winner in winners for name,hand in playerHands.iteritems() if hand == winner[0] ]



