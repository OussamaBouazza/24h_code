#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:18:57 2022

@author: nicolasboisseau
"""

import commande
import time
import json




print(commande.startVaisseau(commande.GetShipID(2), commande.GetMapID(2)))

def CalculRessource(shipNumber, mapNumber):
    distanceX, distanceY = 100, 10
    ressource = commande.GetShip(shipNumber)
    casePlaneteX, casePlaneteY = 0,0
    print("x : {} || y : {}".format(ressource['x'],ressource['y']))
          
    if(ressource['currentRessource']['oxygene'] <= 500):
        print("aled")
        mapJeux = commande.GetShipCarto(shipNumber, mapNumber)
        for case in mapJeux:
            if case['typeCellule'] == 'Planet':
                if ((case['x'] - ressource['x'] <= distanceX)  & (case['y'] - ressource['y'] <= distanceY)):
                    print(case)
                    distanceX = case['x'] - ressource['x']
                    distanceY = case['y'] - ressource['y']
                    print(distanceX)
                    print(distanceY)
                    casePlaneteX = case['x']
                    casePlaneteY = case['y']
        
        
        
        if(ressource['x'] - 2 >= casePlaneteX):
            print(commande.action(commande.GetShipID(shipNumber), -2, 0))
            
        elif(ressource['x'] + 2 <= casePlaneteX):
            print(commande.action(commande.GetShipID(shipNumber), 2, 0))
            
            
        elif(ressource['y'] - 2 >= casePlaneteY):
            print(commande.action(commande.GetShipID(shipNumber), 0, -2))
            
            
        elif((ressource['x'] - 1 >= casePlaneteX) & (ressource['y'] - 1 > casePlaneteY)):
            print(commande.action(commande.GetShipID(shipNumber), -1, -1))
        
        elif((ressource['x'] - 1 >= casePlaneteX)):
            print(commande.action(commande.GetShipID(shipNumber), -1, 0))
            
        elif((ressource['y'] - 1 >= casePlaneteY)):
            print(commande.action(commande.GetShipID(shipNumber), 0, -1))
            
            
        elif(ressource['x'] + 2 <= casePlaneteX):
            print(commande.action(commande.GetShipID(shipNumber), 2, 0))
            
            
        elif(ressource['y'] + 2 <= casePlaneteY):
            print(commande.action(commande.GetShipID(shipNumber), 0, 2))
           
            
        elif((ressource['x'] + 1 <= casePlaneteX) & (ressource['y'] + 1 <= casePlaneteY)):
            print(commande.action(commande.GetShipID(shipNumber), 1, 1))
            
        elif((ressource['x'] + 1 <= casePlaneteX)):
            print(commande.action(commande.GetShipID(shipNumber), 1, 0))
            
        elif((ressource['y'] + 1 <= casePlaneteY)):
            print(commande.action(commande.GetShipID(shipNumber), 0, 1))
            
        elif((ressource['x'] + 1 <= casePlaneteX & (ressource['y'] - 1 >= casePlaneteY))):
            print(commande.action(commande.GetShipID(shipNumber), 1, -1))
            
        elif((ressource['x'] - 1 >= casePlaneteX & (ressource['y'] + 1 <= casePlaneteY))):
            print(commande.action(commande.GetShipID(shipNumber), -1, 1))
        
        
    ressource = commande.GetShip(shipNumber)
    print("x : {} || y : {}".format(ressource['x'],ressource['y']))
                    
         
                    

        
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)
time.sleep(5)
CalculRessource(2,2)

time.sleep(5)


print(commande.GetShip(2))
print(commande.stopVaisseau(commande.GetShipID(2)))
