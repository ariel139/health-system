import pandas as pd
import numpy as np

main_map_df = {'symptoms range time': None, 'Age range': None, 'Location':None, "background_diseases":[], 'symptoms':None, 'Number of pepole how complaind':None}

func_count_number = 0
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


for sym in range(0, len(symptoms)):
    if ',' in symptoms[sym][0]:
        symptoms[sym][0] = symptoms[sym][0].split(',')

data_list = []
def list_data(data_list):
    for i in range(len(symptoms)):
        if type(symptoms[i][0]) == list:
            data_list.append(symptoms[i][0])
    return data_list

known_data_list = []

def known_list_data(known_data_list):
    for i in range(len(symptoms)):
        if type(symptoms[i][0]) == str:
             known_data_list.append(symptoms[i][0])
    return known_data_list

known_list_data(known_data_list)
list_data(data_list)

symptoms_count_number = 0
pepole_Symptos_List = []
def detect_dissess(wanted_number,Symlist = pepole_Symptos_List):
    global main_df
    main_df = pd.DataFrame(data=main_map_df)

    for i in range(len(data_list)):
        if data_list.count(data_list[i]) >= int(wanted_number):
            data_count = data_list.count(data_list[i])
            for s in range(len(known_data_list)):
                data_count = known_data_list.count(known_data_list[s]) + data_count
        main_df = main_df.append({'Number of pepole how complaind': data_count}, ignore_index=True)
detect_dissess(2)
print(main_df)