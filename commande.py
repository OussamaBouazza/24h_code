# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json
from json import JSONEncoder




myToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJPVU5HQSBPVU5HQSIsImlzcyI6IlNwYWNlT2Rpc3NleUF1dGgifQ.OoCNHe710Cgg65ZdkpImaq0siT8n7pG5ByfKaga-2ro"
url = "http://37.187.28.218:8080"
head = {'content-type': 'application/json','access-token': myToken }
teamName = "OUNGA OUNGA"


# subclass JSONEncoder
class setEncoder(JSONEncoder):
    def default(self, obj):
        return list(obj)
    




def GetShipID(shipNumber):
    chemin="{}/team/OUNGA OUNGA/".format(url)
    r = requests.get(chemin,headers=head).json()
    return r['ship_'+str(shipNumber)]['id']
    
    
    
def GetMapID(mapNumber):
    chemin="{}/map".format(url)
    r = requests.get(chemin,headers=head).json()
    for i in r:
        if mapNumber==i['mapNumber']:
            return i['id']
    
    
def GetMap(mapNumber):
    chemin="{}/map/{}/infos".format(url,GetMapID(mapNumber))
    r = requests.get(chemin,headers=head).json()
    return r


def GetExplorations(mapNumber):
    chemin="{}/team/OUNGA OUNGA/map/{}/explorations".format(url,GetMapID(mapNumber))
    r = requests.get(chemin,headers=head).json()
    return r

def GetBestScore(mapNumber):
    chemin="/team/OUNGA OUNGA/map/{}/explorations/max".format(GetMapID(mapNumber))
    r = requests.get(chemin,headers=head).json()
    return r

def GetShip(shipNumber):
    chemin="{}/team/OUNGA OUNGA/ships/{}".format(url, GetShipID(shipNumber))
    r = requests.get(chemin,headers=head).json()
    return r

def GetShipCarto(shipNumber,mapNumber):
    chemin="{}/team/OUNGA OUNGA/ships/{}/map/{}/carto".format(url,GetShipID(shipNumber),GetMapID(mapNumber))
    r = requests.get(chemin,headers=head).json()
    return r
    

def action(shipID, x, y):
    link = "{}/team/{}/ships/{}/actions".format(url,teamName,shipID)
    
    json_data = {
        'actions': [
            'move:{},{}'.format(x, y),
        ],
    }
    
    response = requests.put(link,headers = head, json = json_data)
    return response

def Land(shipID):
    link = "{}/team/{}/ships/{}/actions".format(url,teamName,shipID)
    
    json_data = {
        'actions': [
            'land',
        ],
    }
    
    response = requests.put(link,headers = head, json = json_data)
    return response

def DeplacementPlanet(shipNumber,casePlaneteX,casePlaneteY):
    ship = GetShip(shipNumber)
    
    if(ship['x']<casePlaneteX and ship['y']<casePlaneteY):
        action(GetShipID(shipNumber), 1, 1)
        return 0
        
    elif(ship['x']<casePlaneteX and ship['y']>casePlaneteY):
        action(GetShipID(shipNumber), 1, -1)
        return 0
        
    elif(ship['x']>casePlaneteX and ship['y']>casePlaneteY):
        
        action(GetShipID(shipNumber), -1, -1)
        return 0
        
    elif(ship['x']>casePlaneteX and ship['y']<casePlaneteY):
        action(GetShipID(shipNumber), -1, 1)
        return 0
        
    elif(ship['x']==casePlaneteX and ship['y']<casePlaneteY-1):
        action(GetShipID(shipNumber), 0, 2)
        return 0
        
    elif(ship['x']==casePlaneteX and ship['y']>casePlaneteY+1):
        action(GetShipID(shipNumber), 0, -2)
        return 0
        
    elif(ship['x']==casePlaneteX and ship['y']<casePlaneteY):
        action(GetShipID(shipNumber), 0, 1)
        return 0
        
    elif(ship['x']==casePlaneteX and ship['y']>casePlaneteY):
        action(GetShipID(shipNumber), 0, -1)
        return 0
        
    elif(ship['x']<casePlaneteX-1 and ship['y']==casePlaneteY):
        action(GetShipID(shipNumber), 2, 0)
        return 0
        
    elif(ship['x']>casePlaneteX+1 and ship['y']==casePlaneteY):
        
        action(GetShipID(shipNumber), -2, 0)
        return 0
        
    elif(ship['x']>casePlaneteX and ship['y']==casePlaneteY):
        action(GetShipID(shipNumber), -1, 0)
        return 0
        
    elif(ship['x']<casePlaneteX and ship['y']==casePlaneteY):
        action(GetShipID(shipNumber), 1, 0)
        return 0
    else:
        print("FREREEE")
        return 1
        
     

def Afficheships(shipNumber):
     
    ship = GetShip(shipNumber)
    print("x : {} || y : {}".format(ship['x'],ship['y']))
    print("Material : " + str(GetMaterial(shipNumber)))
    print("Oxygene : " + str(GetOxygene(shipNumber)))
    print("Fuel : " + str(GetFuel(shipNumber)))
    print("Food : " + str(GetFood(shipNumber)))
    print("Water : " + str(GetWater(shipNumber)))
    print("Temperature : " + str(GetTemperature(shipNumber)))
    print("Crew : " + str(GetCrew(shipNumber)))
    
def startVaisseau(shipID, mapID):
    headers = {
        'access-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJPVU5HQSBPVU5HQSIsImlzcyI6IlNwYWNlT2Rpc3NleUF1dGgifQ.OoCNHe710Cgg65ZdkpImaq0siT8n7pG5ByfKaga-2ro'
    }
    
    json_data = {
        'actions': [
            'move:0,0',
        ],
    }
    
    response = requests.post('{}/team/{}/ships/{}/start/{}'.format(url,teamName,shipID,mapID), headers=headers, json=json_data)
    return response



def stopVaisseau(shipID):
    headers = {
        'access-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJPVU5HQSBPVU5HQSIsImlzcyI6IlNwYWNlT2Rpc3NleUF1dGgifQ.OoCNHe710Cgg65ZdkpImaq0siT8n7pG5ByfKaga-2ro'
    }
    json_data = {
        'actions': [
            'move:0,0',
        ],
    }
    response = requests.post('{}/team/{}/ships/{}/end/'.format(url,teamName,shipID), headers=headers, json=json_data)
    return response

def GetMaterial(shipNumber):
    return GetShip(shipNumber)['currentRessource']['material']

def GetOxygene(shipNumber):
    return GetShip(shipNumber)['currentRessource']['oxygene']

def GetFuel(shipNumber):
    return GetShip(shipNumber)['currentRessource']['fuel']

def GetFood(shipNumber):
    return GetShip(shipNumber)['currentRessource']['food']

def GetWater(shipNumber):
    return GetShip(shipNumber)['currentRessource']['water']

def GetTemperature(shipNumber):
    return GetShip(shipNumber)['currentRessource']['temperature']

def GetCrew(shipNumber):
    return GetShip(shipNumber)['currentRessource']['crew']

#print(stopVaisseau(GetShipID(1)))
#print(startVaisseau(GetShipID(1), GetMapID(1)))
#r = GetShipCarto(1,1)

#for data in r:
    #print(data)
    
#print(GetMap(1))
#print(action(GetShipID(1), 1, 1))

#print(GetShip(1))

#print(stopVaisseau(GetShipID(1)))


    
    



    
    
    





