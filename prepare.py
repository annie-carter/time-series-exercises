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