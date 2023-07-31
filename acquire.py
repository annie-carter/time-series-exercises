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
def get_planets_data():
    # Initialize the URL for the first page
    data = []
    url = 'https://swapi.dev/api/planets/'  
    
    while True:
        # Send a GET request to the SWAPI
        response = requests.get(url)  
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
    # Create a DataFrame using the collected data
    df = pd.DataFrame(data)  
    return df
#STARWARS STARSHIPS  
'''This function gets starwars starships '''
def get_starships_data():
    # Initialize the URL for the first page
    data = []
    url = 'https://swapi.dev/api/starships/'
    
    while True:
        # Send a GET request to the SWAPI
        response = requests.get(url)  
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
    # Create a DataFrame using the collected data
    df = pd.DataFrame(data)  
    return df

#STARWARS CVS  
'''This function joins the above dataframes into one and makes cvs. '''

def get_starwars_data(starwars_df):
    '''This function creates a csv for concat wine csv'''
    # Assuming you have a function 'get_starwars_data()' that retrieves the starwars data and returns a DataFrame
    df_starwars = starwars_df

    # Save the DataFrame to a CSV file
    df_starwars.to_csv("starwars.csv", index=False)  # Specify 'index=False' to exclude the index column in the CSV

    filename = 'starwars.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)