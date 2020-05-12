# function used to convert lat,lang to location
def convert(lat,lng):
    import pandas as pd
    import math
    loc = {}
    df  = pd.read_excel("C:\\Users\\shubham\\Documents\\dash_board\\in.xlsx")
    def cnt(x):
        x = str(x)
        x = x[0:4]
        return float(x)
    lat = cnt(lat)
    lng = cnt(lng)

    for i in range(df.shape[0]):
        if abs(cnt(df['lat'][i]- lat))<=0.1 and abs(cnt(df['lng'][i] -lng))<=0.1 :
            loc['state'] = df['state'][i]
            loc['city'] = df['city'][i]
            return loc
