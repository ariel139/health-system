import pandas as pd
import numpy as np
import time
import random

#random disses for test
random_disses = ['Abscess', "Alzheimer's disease","Anthrax", "Appendicitis","Allergy","Arthritis","Aseptic meningitis","Asthma", "Astigmatism","Atherosclerosis"]

# Data Frame
df = pd.read_csv('data.csv')
#count number for dictionery
count_number = 0
# Lists
time_symptoms = df.iloc[:, :1].values
background_diseases = df.iloc[:, 1:2].values
Location = df.iloc[:, 2:3].values
age = df.iloc[:, 3:4].values
symptoms = df.iloc[:, 4:5].values

# problems dictionery
problems_dectinery = {
    'problems' : []
}
problems_list = problems_dectinery['problems']
duplicates = set()



# splits the symptoms to list
def split_symptoms():
    for sym in range(0, len(symptoms) ):
        if ',' in symptoms[sym][0]:
            symptoms[sym][0] = symptoms[sym][0].split(',')
    return symptoms

split_symptoms()

# returning the value0 a part
def symptoms_data0():
    for sym1 in range(0, len(symptoms)):
        return symptoms[sym1][0][0]
# returning the value1 a part

def symptoms_data1():
    for sym1 in range(0, len(symptoms)):
        return symptoms[sym1]

symptoms_data3 = symptoms_data0()
symptoms_data2 = symptoms_data1()

# adding the symptoms into a dict
def compere_symptoms():
    for s in range(0, len(symptoms)):
        if symptoms[s][0][0] or symptoms[s][0][0] == symptoms_data3 or symptoms_data2 :
            if len(symptoms[s][0]) >= 2:
                problems_dectinery[f'problem{count_number}'] = []
                problems_dectinery[f'problem{count_number}'].append(symptoms[s][0])
                problems_dectinery[f'problem{count_number}'].append(symptoms[s][0])
                # problems_list.append(symptoms[s][0][0])
                # problems_list.append(symptoms[s][0][1])
                # print(problems_dectinery[f'problem{count_number}'])
                
        if symptoms[s] == symptoms_data2 or symptoms_data3:
            if len(symptoms[s])==1 and type(symptoms[s][0]) != list:
                problems_dectinery[f'problem{count_number}'].append(symptoms[s][0])

# Random disses func only for test
def random_disses_func():
    return random.choice(random_disses)





def chking_dup():
    dupl = set()
    for i in problems_dectinery[f'problem{count_number}']:
        if problems_dectinery[f'problem{count_number}'].count(i) > 1:
            dupl.add(i)
        dupl = [* dupl]
        for i in range(0, len(dupl)):
            problems_dectinery[f'problem{count_number}'].remove(dupl[i])
        print(problems_list)


compere_symptoms()
print(problems_dectinery['problem0'])


