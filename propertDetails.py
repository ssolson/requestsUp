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


#import ipdb; ipdb.set_trace()

propDeets={}
for id in properties.index:
    propDeets[str(id)] = getPropertyDetails(id)

import ipdb; ipdb.set_trace()

#pd.read_json()
