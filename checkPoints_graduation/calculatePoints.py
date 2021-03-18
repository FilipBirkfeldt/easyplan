import pandas as pd 
import numpy as np 

def readInData(): 
    "Reads in the data needed - Currently courses at M"
    courses_df = pd.read_excel('checkPoints_graduation/coursesM.xlsx')
    courses_df.rename(columns={'Kurskod':'Kurskod'}, inplace=True)
    courses_df['Poäng'] = courses_df['Poäng'].fillna(0)
    courses_df['Poäng'] = courses_df['Poäng'].apply(lambda x:float(x))
    return courses_df

def getActualDf(courses_df, course_list):
    "Return the point"
    course_list = list(course_list)
    boolean_series = courses_df['Kurskod'].apply(lambda x:x in course_list)
    person_df = courses_df[boolean_series]
    return person_df

def calculateAllPoints(dfPerson) -> float: 
    "Calculates points for the person"
    return dfPerson['Poäng'].sum()

def calculate_A_points(dfPerson) -> float: 
    "Calculates all A-Points"
    return dfPerson[dfPerson['Nivå'].str.contains('A')]['Poäng'].sum()

def getPoints_specialization(dfPerson, speci)-> float: 
    print('RÖV')


courses_df = readInData()
course_list = courses_df.Kurskod.iloc[0:20]
person_df = getActualDf(courses_df, course_list)
all_points = calculateAllPoints(person_df)
a_points = calculate_A_points(person_df)
