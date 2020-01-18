# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17'th 2020

@author: passarod  
David Passaro
"""
import testUtility
import Dominion
import random
from collections import defaultdict

#Get player names CHANGED
player_names = testUtility.GetPlayerNames()

#number of curses and victory cards CHANGED
nV = testUtility.GetCurseCards(player_names)
#changed from origional

nC = testUtility.Get_nC(player_names)

#Define box changed from origional
box = testUtility.GetBoxes(nV)

#changed from origional
supply_order = testUtility.GetSupplyOrder()
#Pick 10 cards from box to be in the supply.
boxlist = testUtility.GetBoxList(box)
#changed from origional

supply = testUtility.GetSupply(box)


#The supply always has these cards ##changed
testUtility.GetCopperSupply(supply)             
testUtility.GetSilverSupply(supply)
testUtility.GetGoldSupply(supply) 
testUtility.GetEstateSupply(supply) 
testUtility.GetDuchySupply(supply) 
testUtility.GetProvinceSupply(supply) 
testUtility.GetCurseSupply(supply) 


#initialize the trash
trash = testUtility.initTrash()

#Costruct the Player objects
players = testUtility.initPlayers()


#Play the game
playGame()
            

#Final score
finalScore()