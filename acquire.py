#SWAPI ACQUIRE.PY

import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from env import user, password, hostname, get_connection
import os
import datetime
import requests

def get_connection(db, user=user, host=hostname, password=password):
    '''
    Establishes connection to SQL server
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#-------- SWAPI ---------
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
            url = json_data['next']  

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
    # Specify 'index=False' to exclude the index column in the CSV
    df_starwars.to_csv("starwars.csv", index=False)  

    filename = 'starwars.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    
#-------- TSA -----
def get_store_data():
    '''This function gets store data'''

    filename = 'tsa_store.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else:
        #  SQL code to retrieve data 
        sql = '''
        SELECT *
        FROM sales
        JOIN items USING (item_id)
        JOIN stores USING (store_id)
        LIMIT 10000;
        '''
        df = pd.read_sql(sql, get_connection('tsa_item_demand'))

        # create CSV file
        df.to_csv(filename, index=False)

        return df