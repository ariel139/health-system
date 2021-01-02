import pandas as pd
import numpy as np
import time
import random
print('dsf')
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
}



# splits the symptoms to list
def split_symptoms():
    for sym in range(0, len(symptoms) ):
        if ',' in symptoms[sym][0]:
            symptoms[sym][0] = symptoms[sym][0].split(',')
    return symptoms

split_symptoms()



# returning the value1 a part
big_list = []
def symptoms_data(slist,count_number_data1 = 0, count_number_data2 = 0):
    count_number_data1 = 0
    while count_number_data1 != len(symptoms):
        for sym1 in range(0, len(symptoms)):
            count_number_data1 +=1
            if type(symptoms[sym1][0]) != list:
               slist.append(symptoms[sym1][0])
        break
    count_number_data2 = 0
    while count_number_data2 != len(symptoms):
        count_number_data2 +=1
        for sym1 in range(0, len(symptoms)):
            count_number_data2 +=1
            if type(symptoms[sym1][0]) == list:
                for s in range(0,len(symptoms[sym1][0])):
                    slist.append(symptoms[sym1][0][s])
        break

    return slist


sym_data= symptoms_data(big_list)

def final_list(sym_data):
    for i in range(0, len(sym_data)):
        if sym_data.count(sym_data[i]) ==1:
            sym_data.remove(sym_data[i])
    
    return sym_data

datalist = final_list(sym_data)
# adding the symptoms into a dict
def compere_symptoms():
    global count_number
    for s in range(0, len(symptoms)):
        # lists if statment
        if symptoms[s][0][0] in datalist and len(symptoms[s][0]) >=2 and type(symptoms[s][0]) == list :

            problems_dectinery[f'problem{count_number}'] = []

            problems_dectinery[f'problem{count_number}'].append(symptoms[s][0])
            count_number = count_number + 1

         # one value if statment       
        if symptoms[s][0] in datalist and len(symptoms[s])==1 and type(symptoms[s][0]) != list:
            problems_dectinery[f'problem{count_number}'] = [[]]
            problems_dectinery[f'problem{count_number}'][0].append(symptoms[s][0])
            count_number = count_number + 1



# Random disses func only for test
def random_disses_func():
    return random.choice(random_disses)




# chking for dup do not using it for now!
def chking_dup():
    dupl = set()
    for i in problems_dectinery[f'problem{count_number}']:
        if problems_dectinery[f'problem{count_number}'].count(i) > 1:
            dupl.add(i)
        dupl = [* dupl]
        for i in range(0, len(dupl)):
            problems_dectinery[f'problem{count_number}'].remove(dupl[i])
            pass
flipped = {} 
# TODO add chcking dups
def chking_dup1():
    for key, value in problems_dectinery.items(): 
        if value not in flipped: 
            flipped[value] = [key] 
        else: 
            flipped[value].append(key) 
print('dsdfasdfs')
print(datalist)