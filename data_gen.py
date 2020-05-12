import pandas as pd
import json
from datetime import datetime




#state- cities dict
with open('state_cities.json', 'r') as fp:
    state_cities_dict = json.load(fp)

final_df = pd.read_csv('demo_data.csv')

metrics =['Visitors Count', 'Bounce Count'] #metrics options for metrics markdown
page_names = ['/contact','/','/pricing','/aboutus','/products']    #demo page list used for pagewise visitor graph

def tolst(x):
    return x.replace(' ','').split(',')

def get_page_visitor_count(pages):
    pg_cnt = []
    contact_cnt = 0
    home_cnt = 0
    price_cnt  =0
    about_cnt = 0
    product_cnt = 0
    bounce_cnt = 0
    temp_df = final_df['pages'].apply(lambda x: tolst(x)) #convert pages string to list

    for i in temp_df:
        contact_cnt += (i.count(pages[0]))
        home_cnt+= (i.count(pages[1]))
        price_cnt += (i.count(pages[2]))
        about_cnt+= (i.count(pages[3]))
        product_cnt+= (i.count(pages[4]))
        if(len(i) == 1):
            bounce_cnt+=1

    pg_cnt = [contact_cnt,home_cnt,price_cnt,about_cnt,product_cnt]
    return pg_cnt,bounce_cnt






#dropdown dict generator 

def get_dropdown_dict(valueLst): #original attributes
    dropdown_options = []
    for i in valueLst:
        tmp = {}
        tmp['label'] = i
        tmp['value'] =i
        dropdown_options.append(tmp)
    return dropdown_options



def get_cities_count(state):
        cities = state_cities_dict[state]
        cities_cnt = []
        for i in cities:
            cities_cnt.append(list(final_df.city).count(i))
        return {'cities': cities, 'cities_cnt' : cities_cnt }



def get_date_range_date(start_date,end_date):        #returns the required data in given date range #format(mm-dd-yy)

    start_date = (list(map(lambda x: x.replace('0','') if x[0]=='0'else x,start_date.split('-'))))
    end_date  = (list(map(lambda x: x.replace('0','') if x[0]=='0'else x,end_date.split('-'))))
    start_date = start_date[1]+'/'+start_date[2]+'/'+start_date[0]
    end_date = end_date[1]+'/'+end_date[2]+'/'+end_date[0]
    
    date_lst = list(final_df.date)
    start_index = min([index for index in range(len(date_lst)) if date_lst[index] == start_date])
    end_index = max([index for index in range(len(date_lst)) if date_lst[index] == end_date])
    return   start_index,end_index 


def get_datewise_visitor_count(start_date,end_date):
    i,j= get_date_range_date(start_date,end_date)
    local_df = final_df.iloc[i:j+1,:].reset_index()
    dates = local_df.date.unique()
    date_cnt = [list(local_df.date).count(dates[i]) for i in range(len(dates))]
    return {'dates' :dates,'date_cnt': date_cnt}


def get_start_end_date():    #returns max and min date for graph boundries
    start_date = final_df.date[0]
    end_date = final_df.date[final_df.shape[0]-1]
    start_date = (list(map(lambda x: '0'+x if len(x)==1 else x,start_date.split('/'))))
    end_date  = (list(map(lambda x: '0'+x if len(x)==1 else x,end_date.split('/'))))
    start_date = start_date[2]+'-'+start_date[0]+'-'+start_date[1]
    end_date = end_date[2]+'-'+end_date[0]+'-'+end_date[1]
    return {'start_date':start_date,'end_date':end_date}



   


   
        

 


state_names = final_df.state.unique()    #gives unique state list
state_visitor_count = [list(final_df.state).count(state_names[i]) for i in range(len(state_names))]    #gives the statewise visitor count used in pie chart


    


page_visitor_count,bounce_cnt = get_page_visitor_count(page_names)
bounce_rate = (bounce_cnt/final_df.shape[0])*100
total_page_views = sum([len(x) for x in final_df['pages'].apply(lambda x: tolst(x))])  #total page count used in top metrics
total_visitor_count = final_df.shape[0]


dates = final_df.date.unique()     #gives unique dates present in database
date_cnt = [list(final_df.date).count(dates[i]) for i in range(len(dates))] #datewise total visiters used in total visitors line graph


#Dropdown data
state_dropdown_options = get_dropdown_dict(state_names)  #used in statewise count dropdown
metrics_dropdown_options = get_dropdown_dict(metrics)   #used in metrics selection dropdown


# page wise graph min, max metrics
min_visit_page = page_names[ page_visitor_count.index( min(page_visitor_count))]
max_visit_page = page_names[ page_visitor_count.index( max(page_visitor_count))]

# # state wise graph min, max metrics
min_visit_state = state_names[ state_visitor_count.index( min(state_visitor_count))]
max_visit_state = state_names[ state_visitor_count.index( max(state_visitor_count))]


