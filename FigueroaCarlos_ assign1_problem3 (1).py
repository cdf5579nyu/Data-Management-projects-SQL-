# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 18:05:37 2022

@author: carlo
"""

#given class
import random

class RandomCard:
    '''
    Class that creates objects that are random cards drawn from a deck
    with replacement
    '''
    def __init__(self):
        '''draw a card by pulling a random suit and value in that suit'''
        suits = ("Hearts","Diamonds","Spades","Clubs")
        values = ("Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King")
        self.suit = random.choice(suits)
        self.value = random.choice(values)

    def __str__(self):
        '''printing method'''
        return self.value+" of "+self.suit

    def same_suit(self,other):
        '''checks if two cards have the same suit'''
        return self.suit == other.suit
    
    def same_val(self,other):
        '''checks if two cards have the same value'''
        return self.value == other.value

    def __eq__(self,other):
        '''checks if two cards are the same'''
        return (self.suit==other.suit) and (self.value==other.value)
    
class Hand:
    '''deal a hand of n cards'''
    def __init__(self,n):
        '''pull n cards at random'''
        self.cards = []
        i = 1
        while i <= n:
            card = RandomCard()
            # make sure you don't add the same card twice
            if card not in self.cards:
                self.cards.append(card)
                i += 1
                
                
    def __str__(self):    
        '''print a hand; relies on str method from random_card class'''
        s = "("
        for i in range(len(self.cards)):
            s += self.cards[i].__str__()
            if i < len(self.cards)-1:
                s += ', '
            else:
                s += ")"
        return s

    def flush(self):
        '''check for flush'''
        res = True
        for card in self.cards[1:]:
            # all cards must be the same suit as the first card
            if not(RandomCard.same_suit(self.cards[0],card)):
                res = False
        return res
                
    def singlepair(self):  
        
        res=False
        valuecounts = {}
        
        for card in self.cards:
            if card.value not in valuecounts.keys():
                valuecounts[card.value]=1
                
            else:
                valuecounts[card.value]+=1
                
        if(list(valuecounts.values()).count(2)==1):
                res = True
                
        return res
    
    def doublepair(self):  
        
        res=False
        valuecounts = {}
        
        for card in self.cards:
            if card.value not in valuecounts.keys():
                valuecounts[card.value]=1
                
            else:
                valuecounts[card.value]+=1
                
        if(list(valuecounts.values()).count(2)==2):
                res = True
                
        return res
    
    def triple(self):  
        
        res=False
        valuecounts = {}
        
        for card in self.cards:
            if card.value not in valuecounts.keys():
                valuecounts[card.value]=1
                
            else:
                valuecounts[card.value]+=1
                
        if(list(valuecounts.values()).count(3)==1):
                res = True
                
        return res
    
    def fullhouse(self):  
        
        res=False
        valuecounts = {}
        
        for card in self.cards:
            if card.value not in valuecounts.keys():
                valuecounts[card.value]=1
                
            else:
                valuecounts[card.value]+=1
                
        if(list(valuecounts.values()).count(3)==1 and list(valuecounts.values()).count(2)==1):
                res = True
                
        return res
    
    def four(self):  
        
        res=False
        valuecounts = {}
        
        for card in self.cards:
            if card.value not in valuecounts.keys():
                valuecounts[card.value]=1
                
            else:
                valuecounts[card.value]+=1
                
        if(list(valuecounts.values()).count(4)==1):
                res = True
                
        return res
    
    def notany(self):  
        
        res=False
        valuecounts = {}
        
        for card in self.cards:
            if card.value not in valuecounts.keys():
                valuecounts[card.value]=1
                
            else:
                valuecounts[card.value]+=1
                
        if(list(valuecounts.values()).count(1)==5):
                res = True
                
        return res
    
    
    
    def straight(self):
        res = False
        order = {"Ace": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":11, "Queen":12, "King":13 }
        
        iterableSet = set()
        #since cards can come from the same suit, we will only care about the numeric value and count them
        for card in self.cards:
            iterableSet.add(order[card.value])
            
        #this is a mathematical formula: since a straight happens when there is a sequence followed in the 5 cards
        #we can say that for any sequence of 5 cards, the max-min will yield 5, which is the number of cards in deck
        #we could program it to ==5 but we are setting it so it can work for different hands
        if(max(iterableSet)-min(iterableSet)+1 == len(self.cards) and len(self.cards)==len(iterableSet)):
            res = True
            
        return res
    
    
# count the number of flushes in 100,000 hands
num_flush = 0
for i in range(100000):
    h = Hand(5)
    if h.flush(): num_flush += 1

print("Frequency of flushes:",num_flush / 100000)

num_singlePair = 0
for i in range(100000):
    h = Hand(5)
    if h.singlepair(): num_singlePair += 1

print("Frequency of single pairs:",num_singlePair / 100000)

num_doublepair = 0
for i in range(100000):
    h = Hand(5)
    if h.doublepair(): num_doublepair += 1

print("Frequency of double pairs:",num_doublepair / 100000)

num_triple = 0
for i in range(100000):
    h = Hand(5)
    if h.triple(): num_triple += 1

print("Frequency of triples:",num_triple / 100000)


num_fullhouse = 0
for i in range(100000):
    h = Hand(5)
    if h.fullhouse(): num_fullhouse += 1

print("Frequency of full house:",num_fullhouse / 100000)

num_four = 0
for i in range(100000):
    h = Hand(5)
    if h.four(): num_four += 1

print("Frequency of four of a kind:",num_four / 100000)


num_straight = 0
for i in range(100000):
    h = Hand(5)
    if h.straight(): num_straight += 1

print("Frequency of straights:",num_straight / 100000)

num_nonany = 0
for i in range(100000):
    h = Hand(5)
    if h.notany(): num_nonany += 1

print("Frequency of having none of these:",num_nonany / 100000)


