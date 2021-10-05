from collections import Counter
#create lists of all possible combinatoric moves
#for each player, check all possible hands, pick the one in common to both players

#rank from low to high:
#High Card: Highest value card.~
#One Pair: Two cards of the same value. ~
#Two Pairs: Two different pairs. ~
#Three of a Kind: Three cards of the same value. ~
#Straight: All cards are consecutive values.
#Flush: All cards of the same suit. ~
#Full House: Three of a kind and a pair. ~
#Four of a Kind: Four cards of the same value. ~
#Straight Flush: All cards are consecutive values of same suit. ~
#Royal Flush: Ten, Jack, Queen, King, Ace, in same suit. ~


def poker():
    n = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    moves = ['HC', 'OP', 'TP', 'TK', 'S', 'F', 'FH', 'FK', 'SF', 'RF']
    count = 0
    with open('p054_poker.txt') as file:
        for line in file:
            hand1 = line[:14].split(' ')
            hand2 = line[15:].rstrip().split(' ')
            hand1 = sorted(hand1, key=lambda x: n.index(x[0]))
            hand2 = sorted(hand2, key=lambda x: n.index(x[0]))
            move1 = add_moves(hand1, n)
            move2 = add_moves(hand2, n)
            if move1 != move2:
                if moves.index(move1) > moves.index(move2):
                    count += 1
            else:
                if check_moves(hand1, hand2, move1, n):
                    count +=1
    return count


def check_moves(hand1, hand2, move, n):
    if move !='HC' and move != 'F':
        h1 = [h[0] for h in hand1]
        h2 = [h[0] for h in hand2]
        h1 = sorted(h1, key=lambda x: h1.count(x))
        h2 = sorted(h2, key=lambda x: h2.count(x))
        if n.index(h1[-1][0]) > n.index(h2[-1][0]):
            return True
        if n.index(h1[-1][0]) < n.index(h2[-1][0]):
            return False
    while True:
        if n.index(hand1[-1][0]) > n.index(hand2[-1][0]):
            return True
        if n.index(hand1[-1][0]) < n.index(hand2[-1][0]):
            return False
        else:
            hand1=hand1[:-1]
            hand2=hand2[:-1]


def add_moves(hand, n):
    if all(n.index(hand[i][0])-n.index(hand[i-1][0])==1 for i in range(1, len(hand))):
        if len(set([h[1] for h in hand]))==1:
            if set(['T', 'J', 'Q','K', 'A']).difference([h[1] for h in hand])==set():
                move='RF'
            else:
                move = 'SF'
        else:
            move = 'S'
    elif len(set([h[1] for h in hand]))==1:
        move='F'
    elif len(set(h[0] for h in hand))==4:
        move='OP'
    elif len(set(h[0] for h in hand))==3:
        if 3 in list(Counter([h[0] for h in hand]).values()):
            move='TK'
        elif 2 in list(Counter([h[0] for h in hand]).values()):
            move='TP'
    elif len(set([h[0] for h in hand]))==2:
        if 4 in list(Counter([h[0] for h in hand]).values()):
            move='FK'
        elif 3 in list(Counter([h[0] for h in hand]).values()):
            move='FH'
    else:
        move = 'HC'
    return move


print(poker())
