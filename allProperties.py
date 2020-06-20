import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import json


north = 37.811969
south = 37.690347
west =  -122.521954
east =  -122.316967
address = f"https://api.upland.me/map?north={north}&south={south}&east={east}&west={west}&clusters=true"
def ownedOrMinted(address):
    response = requests.get(address)
    properties_response = json.loads(response.text)
    properties = pd.DataFrame.from_dict(properties_response['clusters'])




def pointPairsDistance(north, south, east, west):
    NW = [north, west]
    NE = [north, east]
    SW = [south, west]
    SE = [south,east]


    dx1 = hypot(SW, SE)
    dx2 = hypot(NW, NE)
    dxMax = min(dx1,dx2)

    dy1 = hypot(SE, NE)
    dy2 = hypot(NW, SW)
    dyMax = min(dy1,dy2)
    return dxMax, dyMax

def hypot(xy1, xy2):
    x1 = xy1[0]
    x2 = xy2[0]
    y1 = xy1[1]
    y2 = xy2[1]
    dist = np.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    return dist


# Largest window
north=37.70969060057962
south=37.70838672767222
east=-122.48045963841842
west=-122.49087673947905
dx, dy = pointPairsDistance(north, south, east, west)
#dx=0.009624506232867702
#dy=0.00121743046393874

# SF Bounds
northMax =  37.811969
westMax  = -122.521954
southMax =  37.690347
eastMax  = -122.316967
x, y = pointPairsDistance(northMax, southMax, eastMax, westMax)


def boxFromPoint(south,west,dx,dy):
    east  = west  + dx
    north = south + dy
    return north, south, east, west


def getResponse(north,south,east,west):
    url = f"https://api.upland.me/map?north={north}&south={south}&east={east}&west={west}&marker=false"
    response = requests.get(url)
    return json.loads(response.text)


southMax=37.708049648303785
westMax=-122.49021747327947

# Initialize NSEW & DataFrame
north, south, east, west = boxFromPoint(southMax, westMax, dx, dy)
response0 = getResponse(north,south,east,west)
properties = pd.DataFrame.from_dict(response0)

# Move across bottom
i = 1
j = 0
while south <= northMax-dy:
    while west <= eastMax-dy:
        #north, south, east, west = boxFromPoint(south, east, dx, dy)
        west = east
        east = west+dx

        response = getResponse(north,south,east,west)
        df =  pd.DataFrame.from_dict(response)
        properties = properties.append(df)

        west  = east
        east  = east + dx
        print(i)
        i+=1
    j+=1
    south = north
    north = south + dy
    west = westMax
    east = westMax + dx


    print(f'north:{north} \n south{south} \n  east:{east}\n west:{west}')

import ipdb; ipdb.set_trace()
properties = properties.set_index('prop_id')
properties = dfproperties.groupby(properties.index).first()

numeric_columns = ['prop_id', 'centerlat', 'centerlng']
for col in numeric_columns:
    properties[col] = properties[col].astype('float')

plt.plot(properties['centerlat'], properties['centerlng'], '.')

#https://api.upland.me/map?north=37.771083&south=37.769505&east=-122.443492&west=-122.453889&marker=false
import ipdb; ipdb.set_trace()
