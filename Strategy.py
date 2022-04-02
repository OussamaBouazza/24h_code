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
    casePlaneteX, casePlaneteY = 15,15
    isLand=0
    
          
    if(ressource['currentRessource']['oxygene'] <= 500):
        print("aled")
        """
        mapJeux = commande.GetShipCarto(shipNumber, mapNumber)
        for case in mapJeux:
            if case['typeCellule'] == 'Planet':
                if ((case['x'] - ressource['x'] <= distanceX)  & (case['y'] - ressource['y'] <= distanceY)):
                    #print(case)
                    distanceX = case['x'] - ressource['x']
                    distanceY = case['y'] - ressource['y']
                    print(distanceX)
                    print(distanceY)
                    casePlaneteX = case['x']
                    casePlaneteY = case['y']
                    if(distanceX==distanceY==0 and isLand==0):
                        commande.Land(commande.GetShipID(shipNumber))
                        isLand=1
        
        """
        
        commande.DeplacementPlanet(shipNumber,casePlaneteX,casePlaneteY)
        
    
    commande.AfficheRessources(shipNumber)
    
         
                    

CalculRessource(2,2)
time.sleep(2)
CalculRessource(2,2)
time.sleep(2)
CalculRessource(2,2)
time.sleep(2)
CalculRessource(2,2)
time.sleep(2)
CalculRessource(2,2)
time.sleep(2)
CalculRessource(2,2)
time.sleep(2)
CalculRessource(2,2)
time.sleep(2)
CalculRessource(2,2)
time.sleep(2)
CalculRessource(2,2)
time.sleep(2)
CalculRessource(2,2)
time.sleep(2)
CalculRessource(2,2)
time.sleep(2)
CalculRessource(2,2)
time.sleep(2)



print(commande.GetShip(2))
print(commande.stopVaisseau(commande.GetShipID(2)))
