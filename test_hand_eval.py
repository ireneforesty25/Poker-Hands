from Midterm_Poker import *
from pokerdeck import *

def test_deal_hand():
    assert(len(deal_hand())) == 5
    
def test_pairs():
    pair_hand = [Card(rank='9', suit='♥'), Card(rank='9', suit='♦'), Card(rank='10', suit='♦'), Card(rank='K', suit='♣'), Card(rank='J', suit='♦')]
    two_pair_hands = [Card(rank='9', suit='♥'), Card(rank='9', suit='♦'), Card(rank='10', suit='♦'), Card(rank='10', suit='♣'), Card(rank='J', suit='♦')]
    ranks = ['2', '3', '4', '5', '6']
    assert find_pairs(ranks) == 0
    ranks = ['2', '2', '4', '5', '6']
    assert find_pairs(ranks) == 1
    ranks = ['4', '5', '4', '5', '6']
    assert find_pairs(ranks) == 2
    
def test_three_of_a_kind():
    hand = [Card(rank='10', suit='♦'), Card(rank='K', suit='♦'), Card(rank='K', suit='♥'), Card(rank='K', suit='♠'),
             Card(rank='4', suit='♠')]    
    assert three_of_a_kind(hand) == 3
    
def test_four_of_a_kind():
    hand = [Card(rank='5', suit='♦'), Card(rank='5', suit='♦'), Card(rank='5', suit='♥'), Card(rank='5', suit='♠'),
             Card(rank='5', suit='2')]
    assert four_of_a_kind(hand) == 4
    
def test_five_of_a_kind():
    hand = [Card(rank='3', suit='♦'), Card(rank='3', suit='♦'), Card(rank='3', suit='♥'), Card(rank='3', suit='♠'),
             Card(rank='3', suit='♠')]
    assert five_of_a_kind(hand) == 5
    
def test_straight():
    hand = [Card(rank='A', suit='♦'), Card(rank='K', suit='♦'), Card(rank='Q', suit='♦'), Card(rank='J', suit='♦'), Card(rank='10', suit='♦')]
    assert straight(hand) == 1
    
    
    

    