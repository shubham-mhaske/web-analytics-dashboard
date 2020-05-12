
import pymysql
import pandas as pd

import pandas as pd
import math

def cnt(x):
            x = str(x)
            x = x[0:4]
            return float(x)


def convert_state(x,df):
    
    lat = x[2]
    lng = x[3]
        
    #df  = pd.read_excel("C:\\Users\\shubham\\Documents\\dash_board\\in.xlsx")
        
    lat = cnt(lat)
    lng = cnt(lng)

    for i in range(df.shape[0]):
        if abs(cnt(df['lat'][i]- lat))<=0.1 and abs(cnt(df['lng'][i] -lng))<=0.1 :
            return  df['state'][i]

def convert_city(x,df):
    
    lat = x[2]
    lng = x[3]
        
    
        
    lat = cnt(lat)
    lng = cnt(lng)

    for i in range(df.shape[0]):
        if abs(cnt(df['lat'][i]- lat))<=0.1 and abs(cnt(df['lng'][i] -lng))<=0.1 :
            return  df['city'][i]
def split_pages(x):
    return x.split(',')

def get_data():

    df1  = pd.read_excel("C:\\Users\\shubham\\Documents\\dash_board\\in.xlsx")

    conn = pymysql.connect("localhost","root","1234","visiters")
    SQL_Query = pd.read_sql_query('''select * from info''', conn)
    df = pd.DataFrame(SQL_Query, columns=['sno','uid','lat','lng','pages','date','count'])

    a =  df.apply(lambda x: convert_state(x,df1), axis=1)
    b =  df.apply(lambda x: convert_city(x,df1), axis=1)

    df.rename(columns = {'lat':'state', 'lng':'city'}, inplace = True)

    df['state'] = a
    df['city'] = b

    df['pages'] = df['pages'].apply(lambda x: split_pages(x))


    
    conn.close()
    return df
