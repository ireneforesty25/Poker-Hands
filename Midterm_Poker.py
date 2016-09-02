from pokerdeck import*

from random import shuffle, choice



def deal_hand(deck):
    shuffle(deck)
    hand = []
    for _ in range(5):
        card = choice(deck)
        deck.remove(card)
        hand.append(card)
    return hand 
    


    
def find_pairs(ranks):
    pairs = []
    for card in ranks:
        if ranks.count(card) == 2 and card not in pairs:
            pairs.append(card)
    return len (pairs)
                
                

def three_of_a_kind(ranks):
    for card in ranks:
        if ranks.count(card) == 3:
            return True 
        else:
            return False   
        
        
        
def four_of_a_kind(ranks):
    for card in ranks:
        if ranks.count(card) == 4:
            return True
        else:
            return False  
        
        
        
def five_of_a_kind(ranks):
    for card in ranks:
        if ranks.count(card) == 5:
            return True
        else:
            return False  
        
        
    
        
def full_house(ranks):
    if find_pairs(ranks) and three_of_a_kind(ranks):
        return True
    else:
        return False    

        
                         
def straight(ranks):
    
    for i in range(len(ranks)):
        if ranks[i] == "J":
            ranks[i] == 11
        elif ranks[i] == "Q":
            ranks[i] == 12
        elif ranks[i] == "K":
            ranks[i] == 13
        elif ranks[i] == "A":
            ranks[i] == 14
        else:
            ranks[i] = int(ranks[i])
    if(int(ranks[4]) - ranks[0] == 4):
        return True
    else:
        return False
    

def flush(suits):
    if mysuits.count == 5:
        return True
    else:
        return False 
    
def straightflush(suits):
    if flush(suits) and straight(ranks):
        return True
    else: 
        return False
    
    
    
if __name__ == '__main__':
    deck = PokerDeck()
    shuffle(deck)
    hand = []
    hand = deal_hand(deck) 
    ranks = []

