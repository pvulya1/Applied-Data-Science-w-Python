import numpy as np
import pandas as pd

from scipy import stats

df = pd.read_csv('datasets/grades.csv')
df.head()

df.shape

early_finishers=df[pd.to_datetime(df['assignment1_submission']) < '2016']
early_finishers.head()

late_finishers= df[pd.to_datetime(df['assignment1_submission']) > '2016']
late_finishers.head()

early_finishers['assignment1_grade'].mean()
late_finishers['assignment1_grade'].mean()

from scipy.stats import ttest_ind

ttest_ind(early_finishers['assignment1_grade'], late_finishers['assignment1_grade'])

## Asg 4

import pandas as pd
import numpy as np
import scipy.stats as stats
import re

mlb_df=pd.read_csv("datasets/mlb.csv")
cities=pd.read_html("datasets/wikipedia_data.html")[1]

mlb_df['team'] = [x.replace('*', '') for x in mlb_df['team']] 
mlb_df['team'] = mlb_df['team'].replace('\(\d+\)',"", regex = True)

cities.rename(columns = {'Metropolitan area':'Metropolitan area', 'Country': 'Country', 'Pop. rank':'Pop. rank', 'Population (2016 est.)[8]':'Population', 'B4':'B4', 'NFL':'NFL', 'MLB':'MLB', 'NBA':'NBA', 'NHL':'NHL', 'B6':'B6', 'MLS':'MLS', 'CFL':'CFL'}, inplace = True)

cities = cities.apply(lambda x: x.replace('\[.*\]', '', regex = True), axis=1)

cities=cities.iloc[:-1,[0,3,5,6,7,8]]
mlb_df.reset_index(inplace = True)
mlb_df.rename(columns = {'team':'MLB'}, inplace = True)
mlb_df.drop('index', axis = 1,inplace =True)
mlb_df = mlb_df[mlb_df['year'] == 2018]

# indeces_to_drop = []
# for el in mlb_df['W']:
#     if len(re.findall('\d+', el)) < 1:
#         indeces_to_drop.extend(list(mlb_df[mlb_df['W'] == el].index))
#         mlb_df.drop(list(mlb_df[mlb_df['W'] == el].index),axis = 0, inplace = True)          
                    
for el in cities['MLB']:

    if len(re.findall('[a-zA-Z]+', el)) == 0:
        
        cities = cities[cities['MLB'] != el]
    
collection = []
count = 0
for el in cities['MLB']:

    for team in mlb_df['MLB']:

        if el in team:
            
            count +=1
            
            temp = {'Team': cities[cities['MLB'] == el]['MLB'].iloc[0],
                'City':cities[cities['MLB'] == el]['Metropolitan area'].iloc[0],
                    'Population':cities[cities['MLB'] == el]['Population'].iloc[0],
                    'W/L': np.mean([int(val) for val in mlb_df[mlb_df['MLB'] == team]['W'].values])/(np.mean([int(val) for val in mlb_df[mlb_df['MLB'] == team]['W'].values])+np.mean([int(val) for val in mlb_df[mlb_df['MLB'] == team]['L'].values]))}
            
            collection.append(temp)
            
        if count == 0:
            
            for element in el.split(" "):
                
                if element in team:
                    
                    temp = {'Team': cities[cities['MLB'] == el]['MLB'].iloc[0],
                        'City':cities[cities['MLB'] == el]['Metropolitan area'].iloc[0],
                    'Population':cities[cities['MLB'] == el]['Population'].iloc[0],
                    'W/L': np.mean([int(val) for val in mlb_df[mlb_df['MLB'] == team]['W'].values])/(np.mean([int(val) for val in mlb_df[mlb_df['MLB'] == team]['W'].values])+np.mean([int(val) for val in mlb_df[mlb_df['MLB'] == team]['L'].values]))}
                    
                    collection.append(temp)
                    #print(collection)
            


new_df = pd.DataFrame(collection)
new_df = new_df.drop_duplicates()

for el in new_df['City']:
    
    if sum(new_df['City'].values == el) > 1:
        temp_city = el
        temp_wl = new_df[new_df['City'] == el]['W/L'].mean()
        temp_pop = new_df[new_df['City'] == el]['Population'].values[0]
        temp_index = new_df[new_df['City'] == el].index
        temp_team = new_df[new_df['City'] == el]['Team'].values[0]
        
        #new_df[new_df['City'] == el].drop(axis = 0, inplace = True)
        new_df = new_df[~(new_df['City'] == el)]
        print(list(temp_index))
        new_row = pd.DataFrame({'index':list(temp_index),'Team':temp_team,'City':temp_city, 'Population':temp_pop, 'W/L':temp_wl})
        #print(new_row)
        new_df = pd.concat([new_df, new_row], ignore_index= True)

new_df = new_df.drop('index', axis = 1)
new_df = new_df.drop_duplicates()
new_df.reset_index(inplace = True)

# new_df.loc[new_df['City'] == 'Chicago', 'W/L'] = 62/(62+100)
# new_df.loc[new_df['City'] == 'Los Angeles', 'W/L'] = 92/(92+71)
# new_df.loc[new_df['City'] == 'San Francisco', 'W/L'] = 73/(73+89)

a= np.arange(8)

b = a[4:6]
b[:] = 40
c = a[4] + a[6]

s = 'ABCAC'

bool(re.match('A', s)) == True

S = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])

S[S <= 3][S > 0]