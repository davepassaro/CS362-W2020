# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17'th 2020

@author: passarod  
David Passaro
"""
import testUtility
#import Dominion
import random
from collections import defaultdict

#Get player names CHANGED
player_names = testUtility.GetPlayerNames()

#number of curses and victory cards CHANGED
nV = testUtility.Get_nV(player_names)
#changed from origional

nC = testUtility.Get_nC(player_names)

#Define box changed from origional
box = testUtility.GetBoxes(nV)

#changed from origional
supply_order = testUtility.GetSupplyOrder()
#Pick 10 cards from box to be in the supply.
boxlist = testUtility.GetBoxList(box)
#changed from origional
random10 = testUtility.GetRandom10(boxlist)
supply = testUtility.GetSupply(box, random10)


#The supply always has these cards ##changed
testUtility.SetCopperSupply(supply, player_names)
testUtility.SetSilverSupply(supply)
testUtility.SetGoldSupply(supply)
testUtility.SetEstateSupply(supply, nV)
testUtility.SetDuchySupply(supply, nV)
testUtility.SetProvinceSupply(supply, nV)
testUtility.SetCurseSupply(supply, nC)


#initialize the trash
trash = testUtility.initTrash()

#Costruct the Player objects
players = testUtility.initPlayers(player_names)


#Play the game
testUtility.playGame(supply, supply_order,players,trash)
#winners bug    
winners = []
winners.append(player_names[2])
#Final score
testUtility.finalScore(players, winners)