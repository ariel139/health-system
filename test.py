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
        print(symptoms[sym1][0][0]) 
# returning the value1 a part

# def symptoms_data1(count_number_data0 = 0, symptoms_list_small):
#     count_number_data0 = 0
#     while count_number_data != len(symptoms):
#         for sym1 in range(0, len(symptoms)):
#             count_number_data +=1
#             if  type(symptoms[sym1][1]) == list:
#                symptoms_list_small.append(symptoms[sym1][1])
#     return symptoms_list_small



def symptoms_data2(symptoms_list_small, count_number_data1 = 0):
    count_number_data1 = 0
    while count_number_data1 != len(symptoms):
        for sym1 in range(0, len(symptoms)):
            count_number_data1 +=1
            if  type(symptoms[sym1][0]) == list:
               symptoms_list_small.append(symptoms[sym1][0][0])
               symptoms_list_small.append(symptoms[sym1][0][1])
    return symptoms_list_small



# if len(symptoms[0][0]) == 1:
#     print('goof')
# else:
#     print('shit')
list1 = []
sy = symptoms_data2(list1)
print(sy)
