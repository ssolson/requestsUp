import pandas as pd
import numpy as np
import json



def getPropertyDetails(id):
    url = f"https://api.upland.me/properties/{id}"
    response = requests.get(url)
    return json.loads(response.text)




jsonFile="deets.json"

with open(jsonFile) as f:
    data = json.load(f)
propDeets=data


def serializeDict(P):
    #import ipdb; ipdb.set_trace()
    
    if P['on_market'] != None:
        for val in  P['on_market'].keys():
            P[val] = propDeets[idN]['on_market'][val]
        P['on_market'] = True
   
        P['streetID'] = P['street']['id']
        P['streetName'] = P['street']['name']
        del P['street']
        P['city'] = P['city']['name']
        P['state'] = P['state']['name']
   
    return P 


id0 = [* propDeets][0]
P =  propDeets[id0]
P = serializeDict(P)
props = pd.DataFrame(P, index=[id0]) 
 
for idN in propDeets.keys():
    print(idN)
    P =  propDeets[idN]
    P = serializeDict(P)
    df = pd.DataFrame(P, index=[idN]) 
        
    props = props.append(df)
import ipdb; ipdb.set_trace()

