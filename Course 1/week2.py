import pandas as pd
import numpy as np
import re

students = ['Alice', 'Jack', 'Molly']

# Now we just call the Series function in pandas and pass in the students
pd.Series(students)

numbers = [1,2,3]

numbers = pd.Series(numbers)
numbers

students = ['Jack', 'Alice', None]
pd.Series(students)

numbers = [1,2, None]
pd.Series(numbers)

students_score = {'Alice':'Physics',
                  'Jack':'Chemistry',
                  'Molly': 'English'}

s = pd.Series(students_score)
s.index

students= [('Alice', 'Brown'), ('Jack', 'White'), ('Molly', 'Green')]
students= pd.Series(['Physics', 'Chemistry', 'English'], index = ['Alice', 'Jack', 'Molly'])

students

students_scores = {'Jack':'Physics',
                   'Alice':'Chemistry',
                   'Molly':'English'}

pd.Series(students_scores, index = ['Jack', 'Alice', 'Paul'])


students_classes = {'Alice': 'Physics',
                   'Jack': 'Chemistry',
                   'Molly': 'English',
                   'Sam': 'History'}

s= pd.Series(students_classes)
s

s[3]
s.loc['Molly']

class_code = {99: 'Physics',
              100: 'Chemistry',
              101: 'English',
              102: 'History'}

s= pd.Series(class_code)
s.iloc[0]

grades = pd.Series([90,70,60])
total= 0

for el in grades:
    total += el
    
total/len(grades)

grades.mean()

grades.head()

for label, value in grades.items():
    
    grades.at[label] = value+2
    
############ data frames

record1 = pd.Series({'Name': 'Alice',
                        'Class': 'Physics',
                        'Score': 85})
record2 = pd.Series({'Name': 'Jack',
                        'Class': 'Chemistry',
                        'Score': 82})
record3 = pd.Series({'Name': 'Helen',
                        'Class': 'Biology',
                        'Score': 90})
record4 = pd.Series({'Name':None,
                     'Class': None,
                     'Score':None})

df = pd.DataFrame([record1, record2, record3, record4], index = ['school1', 'school2', 'school3', 'school4'])
df.loc[:,['Name', 'Score']]

df.dropna(inplace=True)
df

df = pd.read_csv("datasets/Admission_Predict.csv", index_col = 0)
df.head()

new_df=df.rename(columns={'GRE Score':'GRE Score', 'TOEFL Score':'TOEFL Score',
                   'University Rating':'University Rating', 
                   'SOP': 'Statement of Purpose','LOR': 'Letter of Recommendation',
                   'CGPA':'CGPA', 'Research':'Research',
                   'Chance of Admit':'Chance of Admit'})
new_df.head()

new_df.columns = [x.strip() for x in new_df.columns]
new_df.columns = [x.lower().strip() for x in new_df.columns]

####### Querying DataFrame

df = pd.read_csv("datasets/Admission_Predict.csv", index_col = 0)
df.head()

df.columns = [x.lower().strip() for x in df.columns]
df.head()

df[df['chance of admit'] > 0.7].head()


df[(df['chance of admit'] > 0.7) & (df['gre score']>330)].head()


df = pd.read_csv("datasets/Admission_Predict.csv", index_col = 0)
df.head()

df['Serial Number'] = df.index
df = df.set_index('Chance of Admit ')
df.head()

df = df.reset_index()
df.head()

df = pd.read_csv("datasets/census.csv")
df.head()

df['SUMLEV'].unique()

df = df[df["SUMLEV"] == 50]
df.head()

columns_to_keep = ['STNAME','CTYNAME','BIRTHS2010','BIRTHS2011','BIRTHS2012','BIRTHS2013',
                   'BIRTHS2014','BIRTHS2015','POPESTIMATE2010','POPESTIMATE2011',
                   'POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']

df = df[columns_to_keep]
df.head()

df = df.set_index(['STNAME', 'CTYNAME'])
df.head()

df.loc['Michigan', 'Washtenaw County']

df = pd.read_csv("datasets/class_grades.csv")
df.dropna().head()

df.fillna(0)

df =pd.read_csv('datasets/log.csv')
df.head()

df = df.set_index('time')
df = df.sort_index()
df.head()
df.reset_index(inplace=True)

df = df.set_index(['time', 'user'])
df.head()

df.fillna(method = 'ffill', inplace=True)
df.head()

df = pd.DataFrame({'A': [1, 1, 2, 3, 4],
                   'B': [3, 6, 3, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})

df.replace([1,3], [100,300])

df = pd.read_csv('datasets/log.csv')
df.head(200)

df['video'] = df['video'].replace("\w*\.html$", "webpage", regex = True)
df.head()

df = pd.read_csv("datasets/presidents.csv")

df.head()

df['First'] = df["President"].replace("[ ].*", "", regex = True)

del(df["First"])
df.head()

def splitname(row):
    
    row['First'] = row['President'].split(" ")[0]
    row['Last'] = row['President'].split(" ")[-1]
    
    return row

df = df.apply(splitname, axis = 'columns')

df.drop(["First", "Last"], axis = 'columns', inplace =True)

df.head()

df['Born'] = df['Born'].str.extract("([\w]{3} [\w]{1,2}, [\w]{4})")
df.head()

df["Born"] = pd.to_datetime(df["Born"])
df.head()

import pandas as pd
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj1 = pd.Series(sdata)
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj2 = pd.Series(sdata, index=states)
obj3 = pd.isnull(obj2)

obj2['California'] == None

s2 = pd.Series({'Alice': 1, 'Jack': 2, 'Molly': 3})
s2[1]

##### Asgn week 2

df = pd.read_csv("datasets/NISPUF17.csv")
df.drop('Unnamed: 0', axis = 1, inplace = True)
df.head()
np.sum(df['EDUC1'].isna() == True)

len(df[df['EDUC1'] == 1]['EDUC1'])/len(df['EDUC1'])

df.columns = [x.strip().upper() for x in df.columns]

df.head()

def proportion_of_education():
    
    df = pd.read_csv("datasets/NISPUF17.csv")
    df.drop('Unnamed: 0', axis = 1, inplace = True)
    
    dict_prop = {}
    
    dict_prop["less than high school"] = len(df[df['EDUC1'] == 1]['EDUC1'])/len(df['EDUC1'])
    dict_prop["high school"] = len(df[df['EDUC1'] == 2]['EDUC1'])/len(df['EDUC1'])
    dict_prop["more than highschool but not college"] = len(df[df['EDUC1'] == 3]['EDUC1'])/len(df['EDUC1'])
    dict_prop["college"] = len(df[df['EDUC1'] == 4]['EDUC1'])/len(df['EDUC1'])
    
    return dict_prop
    
    
proportion_of_education()

df[df['CBF_01'] == 1]['P_NUMFLU'].mean()
df[df['CBF_01'] == 2]['P_NUMFLU'].mean()

df['P_NUMVRC'] = df['P_NUMVRC'].dropna()

len(df[(df['P_NUMVRC'] >= 1) & (df['SEX'] == 2) & (df['HAD_CPOX'] == 1)])/len(df[(df['P_NUMVRC'] >= 1) & (df['SEX'] == 2) & (df['HAD_CPOX'] == 2)])

df[(df['P_NUMVRC'] > 0) & (df['SEX'] == 2)]

df['P_NUMVRC'].unique()


df= pd.read_csv("datasets/NISPUF17.csv")
df['had_chickenpox_column'] = df[(df['HAD_CPOX'] == 1) | (df['HAD_CPOX'] == 2)]['HAD_CPOX']
df['had_chickenpox_column'] = df['had_chickenpox_column'].dropna()

df = df[np.isnan(df['had_chickenpox_column']) == False]

df['had_chickenpox_column'].unique()

print(df['had_chickenpox_column'].unique())

df[df['P_NUMVRC']]