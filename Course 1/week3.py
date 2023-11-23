import pandas as pd 
import numpy as np

# First we create two DataFrames, staff and students.
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
# And lets index these staff by name
staff_df = staff_df.set_index('Name')
# Now we'll create a student dataframe
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
# And we'll index this by name too
student_df = student_df.set_index('Name')

staff_df.head()
student_df.head()

pd.merge(staff_df, student_df, how = 'inner', left_index= True, right_index = True)

pd.merge(staff_df, student_df, how = 'right', left_index = True, right_index = True)

staff_df = staff_df.reset_index()
student_df = student_df.reset_index()

pd.merge(staff_df, student_df, how = 'right', on = 'Name')

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 
                          'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 
                          'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 
                          'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 
                            'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 
                            'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 
                            'Location': '512 Wilson Crescent'}])

pd.merge(staff_df, student_df, how = 'left', on = 'Name')

df_2013= pd.read_csv("datasets/MERGED2012_13_PP.csv")
df_2014= pd.read_csv("datasets/MERGED2013_14_PP.csv")

len(df_2013)

new_df = pd.concat([df_2013, df_2014])
len(new_df)

import timeit

########## IDIOMS

df = pd.read_csv('datasets/census.csv')
df.head()


(df[df['SUMLEV'] == 50]
    .dropna()
    .set_index(['STNAME', 'CTYNAME'])
    .rename(columns = {'ESTIMATESBASE2010':'Estimates Base 2010'}))


df = pd.read_csv("datasets/census.csv")
df.head()

df.set_index('STNAME', inplace = True)


df = pd.read_csv('datasets/listings.csv')
df.head()

df.reset_index(inplace = True)

df.set_index('cancellation_policy', inplace = True)

df.groupby(level = 0).head()

df.reset_index(inplace = True)

df.groupby('cancellation_policy').agg({"review_scores_value":np.nanmean}) 

df = pd.read_csv('datasets/listings.csv')
df.head()

df = df[['cancellation_policy', 'review_scores_value']]

df.head()

def calc_mean_rev_scores(group):
    
    # group is a dataframe just of whatever we have grouped by, e.g. cancellation policy, so we can treat
    # this as the complete dataframe
    avg=np.nanmean(group["review_scores_value"])
    # now broadcast our formula and create a new column
    group["review_scores_mean"]=np.abs(avg-group["review_scores_value"])
    return group

df.groupby('cancellation_policy').apply(calc_mean_rev_scores).head()


df=pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 
                       'ok', 'ok', 'ok', 'poor', 'poor'],
               columns=["Grades"])

df['Grades'].astype('category').head()

my_categories=pd.CategoricalDtype(categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'], 
                           ordered=True)

grades=df["Grades"].astype(my_categories)

grades[grades>"C"]

df = pd.read_csv("datasets/census.csv")
df.head()

df = df[df["SUMLEV"] == 50]

df = df.set_index('STNAME').groupby(level = 0)['CENSUS2010POP'].agg(np.average)

pd.cut(df, 10)

#### Pivot tables

df = pd.read_csv('datasets/cwurData.csv')
df.head()

def uni_tiers(rank):
    
    if rank >= 1 and rank <=100:
        return 'first tier'
    elif rank > 100 and rank <= 200:
        return 'second tier'
    elif rank >200 and rank <=300:
        return 'third tier'
    else:
        return 'other top universities'

df["Rank_Level"] = df['world_rank'].apply(uni_tiers)

df.head()

df.pivot_table(values= 'score', index = 'country', columns = 'Rank_Level', aggfunc = [np.mean, np.max], margins = True).head()

new_df = df.pivot_table(values= 'score', index = 'country', columns = 'Rank_Level', aggfunc = [np.mean, np.max], margins = True) 

pd.Period('1/2016') 

import pandas as pd
(pd.Timestamp('11/29/2019') + pd.offsets.MonthEnd()).weekday()

#### Asg week 3

import pandas as pd
import numpy as np

# Filter all warnings. If you would like to see the warnings, please comment the two lines below.
import warnings
warnings.filterwarnings('ignore')

Energy = pd.read_excel('datasets/Energy Indicators.xls', skiprows=17, skipfooter=39)

Energy.drop(['Unnamed: 0', 'Unnamed: 1'], axis = 1, inplace=True)

Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

Energy['Country'].replace('\(.*\)', '', regex = True, inplace=True)
Energy['Country'].replace('\d+', '', regex = True, inplace=True)

Energy['Energy Supply'] = Energy['Energy Supply'].apply(lambda x: x*100000)

Energy['Energy Supply per Capita'] = Energy['Energy Supply per Capita'].apply(lambda x: np.NaN if x == '...' else x)

Energy['Country'].replace({"Republic of Korea": "South Korea", "United States of America": "United States", "United Kingdom of Great Britain and Northern Ireland": "United Kingdom", "China, Hong Kong Special Administrative Region": "Hong Kong"}, inplace = True)

Energy['Country'] = Energy['Country'].apply(lambda x: x.strip())

GDP = pd.read_csv('datasets/world_bank.csv', skiprows=4)
GDP.head()

GDP['Country Name'].replace({"Korea, Rep.": "South Korea",  "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"},inplace=True)

GDP['Country Name'] = GDP['Country Name'].apply(lambda x: x.strip())

ScimEn = pd.read_excel('datasets/scimagojr-3.xlsx')
ScimEn.head()

GDP = GDP.rename(columns = {'Country Name':'Country'})

GDP = GDP.loc[:, ['Country', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]

ScimEn = ScimEn[ScimEn['Rank'] <=15]
initially = len(GDP) + len(ScimEn) + len(Energy)
new_df = ScimEn.merge(Energy, how = 'left', on  = 'Country')
new_df = new_df.merge(GDP , how = 'left', on = 'Country')
after = len(new_df)
new_df.set_index('Country', inplace = True)

new_df['AVG'] = new_df.apply(lambda x: np.nanmean(x), axis = 1)

GDP.set_index('Country', inplace = True)

GDP['AVG'] = GDP.apply(lambda x: np.nanmean(x), axis = 1)
GDP.sort_values(by = 'AVG', ascending=False, inplace = True)

#GDP.reset_index(inplace = True)

avgGDP = GDP.head(15).loc[:, 'AVG']

GDP.iloc[2]


df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9],
    'D': [10, 11, 12]
})

grouping_dict = {
    'X': ['A', 'B'],
    'Y': ['C', 'D']
}

grouped = df.groupby(grouping_dict, axis=1)
grouped.head()