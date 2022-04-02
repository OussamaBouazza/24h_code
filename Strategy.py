#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:18:57 2022

@author: nicolasboisseau
"""

import commande
import time
import json



print(commande.stopVaisseau(commande.GetShipID(2)))
print(commande.startVaisseau(commande.GetShipID(2), commande.GetMapID(2)))

def RecupCoordPlanet(shipNumber, mapNumber):
    mapJeux = commande.GetShipCarto(shipNumber, mapNumber)
    list=[]
    for case in mapJeux:
            #print(case)
        if case['typeCellule'] == 'Planet':
            
            list.append([case['x'],case['y']])

    return list            
            
       
def RechercheCoordPlusProche(list,coorX,coorY):
    indice=0
    indice_plus_proche=0
    plus_proche=200
    for i in list:
        dist= (abs(i[0]-coorX))+(abs(i[1]-coorY))
        if(dist<plus_proche):
            plus_proche=dist
            indice_plus_proche=indice;
        indice=indice+1
    return indice_plus_proche
        
        

def vaisseauFaitSaVie(shipNumber, mapNumber):
    
    casePlaneteX, casePlaneteY = 0,0
    list=RecupCoordPlanet(shipNumber,mapNumber)
    print (list)
    
    x=1
      
    while x<35:
        
        if(commande.GetOxygene(shipNumber) <= 300):
            while(commande.GetOxygene(shipNumber)<=380):
                
                print("aled")
                indice=RechercheCoordPlusProche(list,commande.GetShip(shipNumber)['x'],commande.GetShip(shipNumber)['y'])
                
                casePlaneteX=list[indice][0]
                casePlaneteY=list[indice][1]
                print(casePlaneteX)
                print(casePlaneteY)
                commande.Afficheships(shipNumber)
                time.sleep(5)
                if(commande.DeplacementPlanet(shipNumber,casePlaneteX,casePlaneteY) ):
                    commande.Land(commande.GetShipID(shipNumber))
                    
                    
        else:
            commande.action(commande.GetShipID(shipNumber),1,1)
            commande.Afficheships(shipNumber)
            time.sleep(5)
        x=x+1
    
    
    
         
                    

vaisseauFaitSaVie(2,2)







print(commande.GetShip(2))
print(commande.stopVaisseau(commande.GetShipID(2)))
