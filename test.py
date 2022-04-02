# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json
from json import JSONEncoder
import pygame



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
    chemin="{}/map/{}/infos".format(url,GetMapID(1))
    r = requests.get(chemin,headers=head).json()
    return r


def GetExplorations(mapNumber):
    chemin="/team/OUNGA OUNGA/map/{}/explorations".format(GetMapID(mapNumber))
    r = requests.get(chemin,headers=head).json()
    return r

def GetBestScore(mapNumber):
    chemin="/team/OUNGA OUNGA/map/{}/explorations/max".format(GetMapID(mapNumber))
    r = requests.get(chemin,headers=head).json()
    return r

def GetShip(shipNumber):
    chemin="/team/OUNGA OUNGA/ships/"+GetShipID(shipNumber)
    r = requests.get(chemin,headers=head).json()
    return r

def GetShipCarto(shipNumber,mapNumber):
    chemin="{}/team/OUNGA OUNGA/ships/{}/map/{}/carto".format(url,GetShipID(shipNumber),GetMapID(mapNumber))
    r = requests.get(chemin,headers=head).json()
    return r
    


def action(shipID, x, y):
    link = "{}/team/{}/ships/{}/actions".format(url,teamName,shipID)
    aList = [{'actions':{'move:0,0'}}]
    jsonData = setEncoder().encode(aList)
    response = requests.put(link,headers = head, json = jsonData)
    return response



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


print(startVaisseau(GetShipID(1), GetMapID(1)))
r = GetShipCarto(1,1)

for data in r:
    print(data)
#print(stopVaisseau(GetShipID(1)))


    
    



    
    
    





