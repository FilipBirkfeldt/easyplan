import pandas as pd 
import numpy as np 

def readInData(): 
    "Reads in the data needed - Currently courses at M"
    df_13 = pd.read_excel('checkPoints_graduation/data_Poäng/dataM.xlsx', sheet_name='1-3')
    df_specialiseringar = pd.read_excel('checkPoints_graduation/data_Poäng/dataM.xlsx', sheet_name='Specialiseringar')
    df_ValfriaM = pd.read_excel('checkPoints_graduation/data_Poäng/dataM.xlsx', sheet_name='Valfria_M')

    courses_df = df_13.append(df_specialiseringar)
    courses_df = courses_df.append(df_ValfriaM)

    courses_df.rename(columns={'Kurskod':'Kurskod'}, inplace=True)
    courses_df['Poäng'] = courses_df['Poäng'].fillna(0)
    courses_df['Poäng'] = courses_df['Poäng'].apply(lambda x:float(x))
    return courses_df

def __getPersonDf(courses_df, course_list):
    "Return the point"
    course_list = list(course_list)
    boolean_series = courses_df['Kurskod'].apply(lambda x:x in course_list)
    person_df = courses_df[boolean_series]
    return person_df

def __calculateAllPoints(dfPerson) -> float: 
    "Calculates points for the person"
    return dfPerson['Poäng'].sum()

def __calculate_A_points(dfPerson) -> float: 
    "Calculates all A-Points"
    return dfPerson[dfPerson['Nivå'].str.contains('A', na=False)]['Poäng'].sum()

def __getPoints_specialization(dfPerson, speci)-> float: 
    "Returns the points for the given specialization"
    return dfPerson[dfPerson.Typ == speci]['Poäng'].sum()


def __getAllPointsDict(progam, specialisering, course_list) -> dict:
    "Returns a dictionary for the specific person, allP, A-P, spec-P"
    courses_df = readInData()
    course_list = courses_df.Kurskod.values
    person_df = __getPersonDf(courses_df, course_list)

    all_points = __calculateAllPoints(person_df)
    a_points = __calculate_A_points(person_df)
    spec_points = __getPoints_specialization(person_df, 'Mekatronik')

    #Creates the dictionary for the student 
    personDict = {
        'Total_Points' : all_points, 
        'A_Points' : a_points,
        'Spec_Points' : spec_points
    }
    return personDict

def __addPointsLeft_toDict(personDict) -> dict: 
    "Adds points left to graduation"
    aPoints_req = 45
    totalPoints_req = 300
    specPoints_req = 45

    # Lägger till keys (_left) som visar hur många poäng personen behöver för Graduation
    keys_dict = list(personDict.keys())
    for key in keys_dict: 
        if 'Spec' in key: 
            points_left = specPoints_req - personDict.get(key)
        elif 'Total' in key: 
            points_left = totalPoints_req - personDict.get(key)
        if 'A' in key: 
            points_left = aPoints_req - personDict.get(key)

        personDict.update({(key+'_left'): points_left})
    
    return personDict


def presentPerson(): 
    "Bara för att visa er var vi är so far"
    personDict = __getAllPointsDict('M', 'Mekatronik', ['kommer va chill när den här fungerar'])
    personDict = __addPointsLeft_toDict(personDict)
    print()
    for key in personDict.keys(): 
        if 'left' in key: 
            continue
        print('\n', key, ' - ', personDict.get(key), '  left: ', personDict.get(key+'_left'))

#presentPerson()

def testSidde(word:str, ord:int) ->str:
    return str(word)+' world ' + str(ord)

string =  testSidde(7, 5)

print(string)
