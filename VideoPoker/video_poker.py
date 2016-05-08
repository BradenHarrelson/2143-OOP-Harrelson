"""
Braden Harrelson
2143-OOP
Dr.Griffin
"""

import os
import random
import time        
  
"""
@Class Card 
@Description:
    Creates each instance of a card that is put into a deck and then
    put into hands    
"""
class Card(object):
    
    suits = ['spades','hearts','diamonds','clubs']

    def __init__(self, suit='', rank=0):
        pass
        
        # If user passes in an int between 0-3, then convert it to string
        # otherwise keep the string 
        if type(suit) is int:
            self.suit = self.suits[suit]
        else:
            self.suit = suit
            
        self.rank = rank
        #self.card_image = self.get_card_face(self.suit,self.rank)

    def __str__(self):
        return ("(suit:%s, rank:%s)") % (self.suit, self.rank)
           
    def __cmp__(self,other):
        t1 = self.suit,self.rank
        t2 = other.suit,other.rank
        return int(t1[1])<int(t2[1])
   
    # Python3 wasn't liking the __cmp__ to sort the cards, so 
    # documentation told me to use the __lt__ (less than) 
    # method.
    def __lt__(self,other):
        return self.__cmp__(other)
        
"""
@Class Deck 
@Description:
    This class represents a deck of cards. 
@Methods:
    pop_cards() - removes a card from top of deck
    add_card(card) - adds a card to bottom of deck
    shuffle() - shuffles deck
    sort() - sorts the deck based on value, not suit (could probaly be improved based on need)
"""       
class Deck(object):
    def __init__(self):
        #assume top of deck = 0th element
        self.cards = []
        for suit in range(4):
            for rank in range(2,15):
                self.cards.append(Card(suit,rank))
                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return " ".join(res)
    
    def pop_card(self):
        return self.cards.pop(0)
        
    def add_card(self,card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards = sorted(self.cards)
        
        
       
"""
@Class: Hand 
@Extends: Deck
@Description:
    This class represents a hand of cards 
@Methods:
""" 
class Hand(Deck):
    def __init__(self,label=''):
        self.cards = []
        self.label = label
        self.rankCount = {}     # Used to calculate pairs, three of a kind, etc.
        self.suitCount = {}     # Used to calculate flush
        
    def addCard(self,card):
        
        if not card.suit in self.suitCount:
            self.suitCount[card.suit] = 1
        else:
            self.suitCount[card.suit] += 1
            
        if not card.rank in self.rankCount:
            self.rankCount[card.rank] = 1
        else:
            self.rankCount[card.rank] += 1  
        if len(self.cards) < 5:  
            self.cards.append(card)
        
    def getCards(self):

        return self.cards
   
    def sortHand(self):
        self.cards = sorted(self.cards)
        
    def replaceCard(self,id,card):
        p = self.cards[id]
        self.addCard(card)
        self.cards[id] = card
        if self.rankCount[p.rank] > 1:
            self.rankCount[p.rank] -= 1
        else:
            self.rankCount.pop(p.rank,None)
        if self.suitCount[p.suit] > 1:
            self.suitCount[p.suit] -= 1
        else:
            self.suitCount.pop(p.suit,None)
        
    def getPosition(self,card):
        return self.cards.index(card)
        
        
    def trashHand(self):
        self.cards = []
        self.rankCount = {}     # Used to calculate pairs, three of a kind, etc.
        self.suitCount = {}     # Used to calculate flush        
       

"""
@Class video_poker
@Description:
    This is where the game deals with dealing cards and determining
    winning hands.  
@Methods:
    def __init__(self): -constructor for class
    def deal(self,number=5): -creates a deck
    def getCard(self): -gets a card off the top of the deck      
    def checkHand(self,hand): -checks the hand for winning hands
    def pair(self,hand): -checks for a pair
    def twoPair(self,hand): -checks for two pair
    def threeOfAKind(self,hand): -checks for three of a kind
    def straight(self,hand): -checks for a straight
    def flush(self,hand): -checks for a flush
    def fourOfAKind(self,hand): -checks for four of a kind
    def fourSevens(self,hand): -checks for four sevens         
    def fourEightsOrAces(self,hand): -checks for four eights or aces             
    def aceStraight(self,hand): -checks for a ace high straight
"""  
        
class video_poker(object):
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand()
        
    def deal(self,number=5):
        self.deck.shuffle()

        for i in range(0,number):
            self.hand.addCard(self.deck.pop_card())  
        print(self.hand)
        print('')
        return self.hand
        
    def getCard(self):
        return self.deck.pop_card()
            
    def checkHand(self,hand):
        hand.sortHand()
        if self.flush(hand) and aceStraight(hand):
            return 800
        if self.fourEightsOrAces(hand):
            return 80
        if self.straight(hand) and self.flush(hand):
            return 50
        if self.fourSevens(hand):
            return 50
        if self.fourOfAKind(hand):
            return 25
        if self.threeOfAKind(hand) and self.pair(hand):
            return 8
        if self.flush(hand):
            return 5
        if self.straight(hand):
            return 4
        if self.threeOfAKind(hand):
            return 3
        if self.twoPair(hand):
            return 2
        if self.pair(hand):
            return 1
        return 0

    def pair(self,hand):
        if len(hand.rankCount) == 4:
            for c in hand.rankCount:
                if c > 10 and hand.rankCount[c] == 2:
                    return True
        
    def twoPair(self,hand):
        if len(hand.rankCount) == 3:
            return True
    
    def threeOfAKind(self,hand):
        for c in hand.rankCount:
            if hand.rankCount[c] == 3:
                return True
                
    def straight(self,hand):
        return (hand.cards[4].rank - hand.cards[0].rank) == 4 and len(hand.rankCount) == 5
    
    def flush(self,hand):
        if len(hand.suitCount) == 1:
            return True
            
    def fourOfAKind(self,hand):
        for c in hand.rankCount:
            if hand.rankCount[c] == 4:
                return True
                
    def fourSevens(self,hand):
        if 7 in hand.rankCount:
            if hand.rankCount[7] == 4:
                return True
                
    def fourEightsOrAces(self,hand):
        if 8 in hand.rankCount:
            if hand.rankCount[8] == 4:
                return True
        if 14 in hand.rankCount:
            if hand.rankCount[14] == 4:
                return True
                
    def aceStraight(self,hand):
        if hand.cards[4].rank == 14:
            if hand.cards[4].rank - hand.cards[0] == 4:
                if len(hand.rankCount) == 5:
                    return True
"""
@Class game_driver
@Description:
    This is the class that drives the game and run everything together.  
@Methods:
    def __init__(self): -constructor
    def print_menu(self): -main method to run game, prompts the game 
""" 

class game_driver(video_poker):
    def __init__(self):
        super().__init__()
        
    def print_menu(self):
        print("1: New Game")
        print("2: Play Again(same deck)")
        print("3: Quit")
        x = int(input(''))
        print('')
        if x == 1 or x == 2:
            if x == 1:
                self.deck = Deck()
            self.deal()
            num = input("Enter the indices of up to 5 numbers separated by commas of the cards you wish to remove(1-5). 0 to keep your cards.(ex.'1,3,5'): ")
            if num != '0': 
                num_list = num.split(',')
                numbers = [int(x.strip()) for x in num_list]
                for i in numbers:
                    i = i - 1
                    y = self.deck.pop_card()
                    #print(self.hand.rankCount)
                    self.hand.replaceCard(i,y)
            print('')
            print(self.hand)
            s = video_poker().checkHand(self.hand)
            print(('Your hand is worth %d points.') % (s))
            print('')
            self.hand.trashHand()
            self.print_menu()
            
        else:
            print("Maybe next time!")
            
    

        
if __name__=='__main__':

    g = game_driver()  #creating an instance of the game
    g.print_menu()     #starting the game
    