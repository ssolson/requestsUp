import pandas as pd
import numpy as np
import requests
import json

properties = pd.read_json('properties.json',convert_axes=False)   

def getPropertyDetails(id): 
    url = f"https://api.upland.me/properties/{id}"
    response = requests.get(url) 
    return json.loads(response.text)
    #del properties_response['state']
    #df = pd.DataFrame.from_dict(properties_response)

jsonFile="deets3.json"

try:
    with open(jsonFile) as f:
        data = json.load(f)
    NComplete = len(data.keys())
    propDeets=data
    i=NComplete
except IOError:
    NComplete = 0
    propDeets={}
    i=0
    


#import ipdb; ipdb.set_trace()

N = len(properties)
for id in properties.index[i:]:
    try:
        propDeets[str(id)] = getPropertyDetails(id)
    except:
        print(getPropertyDetails(id))
        with open('deets4.json', 'w', encoding='utf-8') as f:
            json.dump(propDeets, f, ensure_ascii=False, indent=4)
        import ipdb; ipdb.set_trace()
    print(f"{i/N}, {i}/{N}")
    i+=1

    with open('deets.json', 'w', encoding='utf-8') as f:
        json.dump(propDeets, f, ensure_ascii=False, indent=4)
import ipdb; ipdb.set_trace()
