# pulls data from csv file and extracts time series by country

import numpy as np
import pandas as pd


# creates a dictionary {country_i {sb : [], ns : [], os : []}...}
# sb : state-based
# ns : non-state
# os : out-of-state
def GetTimeSeries():
    
    fatality_df = pd.read_csv('fatalities_1989_2018.csv',delimiter=';')
    
    country_list = list(set(fatality_df['country_name']))
    min_step = fatality_df['month_id'].min()
    num_steps = fatality_df['month_id'].max() - min_step 
    
    fatality_type_list = ['sb_ged_best', 'ns_ged_best', 'os_ged_best']
    
    country_list.sort()
    fatality_type_list.sort()
    
    fatality_dict = {country:{t_type : np.zeros(num_steps) for t_type in fatality_type_list} for country in country_list}
    
    # populate arrays
    for row in range(fatality_df.shape[0]):
            
        t_country = fatality_df.at[row,'country_name']
        t_step = fatality_df.at[row,'month_id'] - min_step - 1
        
        for fatality_type in fatality_type_list:
            fatality_dict[t_country][fatality_type][t_step] = fatality_df.at[row,fatality_type]
            
    return fatality_dict

# filter to include only countries with at least perc_events positive events
# violence type
# returns m x n array where m is number of countries and n is number of time steps
def FilterDict(fatality_dict, perc_events, viol_type):
    
    arr_list = []
    
    c = 0
    tot = len(fatality_dict)
    min_events = int(tot*perc_events)
    
    for country,data in fatality_dict.items():
        if (data[viol_type]>0).sum() > min_events:
            c+=1
            arr_list.append(data[viol_type])
    print(c)
    
    return np.array(arr_list)
        