import numpy as np
import pandas as pd
import csv

print('hello {} how are you doing {}'.format('Eugene', 'today'))

class Person:
    department = 'math'

    def set_name(self, name):
        self.name= name
        
    def set_location(self, location):
        self.location = location
        
student1 = Person()
student1.set_location('Brooklyn')

student1.set_name('Eugene')
student1.name

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return [person.split(' ')[0] + person.split(' ')[2]]

list(map(split_title_and_name, people))

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

for person in people:
    print(person.split()[0] + ' ' + person.split()[-1])

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda person: person.split()[0] + ' ' + person.split()[-1]))

#option 2
#list(map(split_title_and_name, people)) == list(map(???))

for x in [1,2,3,4,5,6]:
    print((lambda x: x * x))

  # Outputs: 16

############ NUMPY

a = np.array([1,2,3])
 
z = np.zeros((2,3))

a = np.array([10,20,30,40])
b = np.array([1,2,3, 4])

c = a- b


farenh = np.array([0,-10,-5,-15,0])

celc = (farenh - 31)*(5/9)
celc > -20
celc % 2 == 0

A = np.array([[1,1], [0,1]])
B = np.array([[2,0], [3,4]])

A*B

a = np.array([1,3,5,7])
a =np.array([[1,2], [3,4], [5,6]])
a[2,1]

wines = np.genfromtxt("datasets/winequality-red.csv", delimiter=";", skip_header = 1)
wines[:,0]

wines[:,-1].mean()

admissions = np.genfromtxt("datasets/Admission_Predict.csv", dtype = None, delimiter = ',', skip_header = 1, names = ('Series No', 'GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA', 'Research', 'Chance of Admit'))

admissions['CGPA'][0:20]
admissions['CGPA'] = admissions['CGPA']/10*4

len(admissions[admissions['Research'] == 1]['Research'])/(len(admissions[admissions['Research'] == 1]['Research']) + len(admissions[admissions['Research'] == 0]['Research']))

print(admissions[admissions['Chance_of_Admit'] > 0.8]['GRE_Score'].mean())

##### Regex

import re

text = "Amy works diligently. Amy gets good grades. Our student Amy is succesful."
re.search("^Amy", text)

grades="ACAAAABCBCBAA"

re.findall("^[^A]", grades)

re.findall("A{1,10}B{1,10}C{1,10}", grades)

with open("datasets/ferpa.txt", "r") as file:
    wiki = file.read()

re.findall("[a-zA-Z]{1,100}\[edit\]", wiki)

re.findall("\w{1,100}\[edit\]", wiki)

re.findall("[\w ]*\[edit\]", wiki)

for title in re.findall("[\w ]*\[edit\]", wiki):
    title = title.split("[")[0]
    print(title)
    

re.findall("([\w ]*)(\[edit\])", wiki)

for item in re.finditer("(?P<title>[\w ]+)(?=\[edit\])", wiki):
    print(item.groups())
    
with open('datasets/buddhist.txt', "r") as file:
    wiki = file.read()
    
wiki

pattern = """
(?P<title>.*)   #the uni title
(-\ located\ in\ ) #an indicator of the location
(?P<city>\w*)
(,\ )
(?P<state>\w*)
"""

for item in re.finditer(pattern, wiki, re.VERBOSE):
    print(item.groupdict())
    
text = "www.aBC.com"

re.findall("([a-zA-Z]+\.{1})(\.{1}[A-Za-z]+)", text)

print()

import re
string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
result = re.findall('b[ao]t', string)
print(result)

np.random.rand()
a4= np.arange(1,4,1)
a4

import re
s = 'ACAABAACAAAB'
result = re.findall('A{1,2}', s)
L = len(result)
L

names = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
    
re.findall("[A-Z]+\w+", names)

with open("datasets/grades.txt") as file:
    text = file.read()
    
re.findall("\w+ \w+(?=: B)", text)



with open("datasets/logdata.txt", "r") as file:
    
    logs = file.read()



logs = logs.split("\n")    
logs = logs[:-1]
list_of_dicts = []
for el in logs:
    #print(el)
    #print(re.search("(?<=\[).+(?=\])", el).group())
    sample_dict = {}
    sample_dict["host"] = re.search("(?:\d{1,3}\.){1,3}\d{1,3}", el).group()
    try:
        sample_dict['user_name'] = re.search("(?<=- )\w+", el).group()
    except AttributeError:
        sample_dict['user_name'] = "-"
    sample_dict["time"] = re.search("(?<=\[).+(?=\])", el).group()
    sample_dict["request"] = re.search("(?<=\").+(?=\")", el).group()
    print(sample_dict)
    list_of_dicts.append(sample_dict)

    

