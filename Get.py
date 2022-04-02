# -*- coding: utf-8 -*-
import requests


token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJPVU5HQSBPVU5HQSIsImlzcyI6IlNwYWNlT2Rpc3NleUF1dGgifQ.OoCNHe710Cgg65ZdkpImaq0siT8n7pG5ByfKaga-2ro"
url="http://37.187.28.218:8080"
headers={'content-type': 'application/json','access-token': token}

r = requests.get(url,headers=headers).json()




def GetShipID(shipNumber):
    chemin="/team/OUNGA OUNGA/"
    headers={'content-type': 'application/json','access-token': token}
    r = requests.get(url+chemin,headers=headers).json()
    
    return r['ship_'+str(shipNumber)]['id']
    
    
    
def GetMapID(mapNumber):
    chemin="/map"
    headers={'content-type': 'application/json','access-token': token}
    r = requests.get(url+chemin,headers=headers).json()
    
    for i in r:
        
        if mapNumber==i['mapNumber']:
            return i['id']
    
 
#-----------------------
def GetMap(mapNumber):
    chemin="/map/"+GetMapID(mapNumber)+"/infos"
    r = requests.get(url+chemin,headers=headers).json()
    return r

def GetMap_xstart(r):
    return r['xstart']
    
    

#-----------------------
def GetExplorations(mapNumber):
    chemin="/team/OUNGA OUNGA/map/"+GetMapID(mapNumber)+"/explorations"
    r = requests.get(url+chemin,headers=headers).json()
    return r

def GetBestScore(mapNumber):
    chemin="/team/OUNGA OUNGA/map/"+GetMapID(mapNumber)+"/explorations/max"
    r = requests.get(url+chemin,headers=headers).json()
    return r

def GetShip(shipNumber):
    chemin="/team/OUNGA OUNGA/ships/"+GetShipID(shipNumber)
    r = requests.get(url+chemin,headers=headers).json()
    return r

def GetShipCarto(shipNumber,mapNumber):
    chemin="/team/OUNGA OUNGA/ships/"+GetShipID(shipNumber)+"/map/"+GetMapID(mapNumber)+"/carto"
    r = requests.get(url+chemin,headers=headers).json()
    return r


def StartVaisseau(shipNumber,mapNumber):
    chemin="/team/OUNGA OUNGA/ships/"+GetShipID(shipNumber)+"/start/"+GetMapID(mapNumber)
    r = requests.post(url+chemin,headers=headers)
    return r
    



#print(StartVaisseau(1,1))
#print(GetShipCarto(1,1))
print(GetMap_xstart(GetMap(1)))
print(GetMap(1))



    


