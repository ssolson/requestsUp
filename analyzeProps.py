import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json



def getPropertyDetails(id):
    url = f"https://api.upland.me/properties/{id}"
    response = requests.get(url)
    return json.loads(response.text)

df = pd.read_pickle("propertyDeets.pkl")


#properties = pd.DataFram.to_pickle('propertyDeets.pkl')




import ipdb; ipdb.set_trace()

