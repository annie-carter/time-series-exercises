#SWAPI ACQUIRE.PY

import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

import os
import datetime
import requests


#STARWARS PEOPLE 
'''This function gets starwars people '''
#Worked to integrated the code steps for one clean code will use this version for acquire.py 
def get_swpeople_data():
    data = []
    url = 'https://swapi.dev/api/people/'  # Initialize the URL for the first page
    
    while True:
        response = requests.get(url)  # Send a GET request to the SWAPI
        if response.status_code == 200:
            json_data = response.json()
            results = json_data['results']
            data.extend(results)
            url = json_data['next']  # Update the URL with the next page URL

            if url is None:
                break
        else:
            print(f"Error: {response.status_code}")
            break
    
    df = pd.DataFrame(data)  # Create a DataFrame using the collected data
    return df
#STARWARS PLANETS 
'''This function gets starwars planets '''
