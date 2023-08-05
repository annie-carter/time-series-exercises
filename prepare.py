import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

from acquire import get_store_data


def prep_sales_data(df):
    '''This function changes sale_item''' 
        
    sales_df.sale_date = sales_df.sale_date.astype('datetime64')
    sales_df = sales_df.set_index('sale_date')
    sales_df['month'] = sales_df.index.month
    sales_df['day_of_week'] = sales_df.index.day_of_week
    sales_df['sales_total'] = sales_df.sale_amount * sales_df.item_price
    features = ['sale_amount', 'item_price']

    for feature in feature:
        sales_df[feature].hist()
        plt.title([feature])
        plt.show()

    return sales_df


#------------- OPS----
def prepare_ops_data(): 
    '''prepares data from OPSD _germany'''
    # this reads in red wine dataframe from csv
    ops_df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')   
    # Convert the "Date" column to datetime format
    ops_df["Date"] = pd.to_datetime(ops_df["Date"])
    # Set the "Date" column as the index
    ops_df = ops_df.set_index("Date")
    cols = ops_df.columns
    for i in cols:
        ops_df[i] = ops_df[i].fillna(ops_df[i].mean())
    
    ops_df["Year"] = ops_df.index.year
    ops_df["Month"] = ops_df.index.month
    ops_df["Month Name"] = ops_df.index.month_name()
    # Fill missing values using forward fill (filling missing values with the previous valid value)
    ops_df_ffill = ops_df.fillna(method='ffill')  
    return ops_df