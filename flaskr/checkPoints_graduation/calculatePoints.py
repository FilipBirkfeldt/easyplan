import pandas as pd 
import numpy as np 

def readInData(): 
    "Reads in the data needed - Currently courses at M"
    courses_df = pd.read_csv('flaskr/checkPoints_graduation/data_Poäng/table2db.csv')
    courses_df.rename(columns={'Kurskod':'Kurskod'}, inplace=True)
    courses_df['Poang'] = courses_df['Poang'].fillna(0)
    courses_df['Poäng'] = courses_df['Poang'].apply(lambda x:float(x))
    return courses_df

def __getPersonDf(courses_df, course_list):
    "Return the point"
    course_list = list(course_list)
    boolean_series = courses_df['Kurskod'].apply(lambda x:x in course_list)
    person_df = courses_df[boolean_series]
    return person_df

def __calculateAllPoints(dfPerson) -> float: 
    "Calculates points for the person"
    return dfPerson['Poang'].sum()

def __calculate_A_points(dfPerson) -> float: 
    "Calculates all A-Points"
    return dfPerson[dfPerson['Niva'].str.contains('A', na=False)]['Poang'].sum()

def __getPoints_specialization(dfPerson, speci)-> float: 
    "Returns the points for the given specialization"
    return dfPerson[dfPerson.Typ == speci]['Poang'].sum()


def getAllPointsDict(progam, specialisering, course_list) -> dict:
    "Returns a dictionary for the specific person, allP, A-P, spec-P"
    courses_df = readInData()
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

def addPointsLeft_toDict(personDict) -> dict: 
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


def getPerson(M:str, courseString:str)->dict: 
    "Bara för att visa er var vi är so far"
    listString = courseString.split(', ')

    personDict = getAllPointsDict('M', 'Mekatronik', listString)
    personDict = addPointsLeft_toDict(personDict)
    return personDict
    

# TODO: 
def addCourses(listCourse:list, df:pd.DataFrame())->pd.DataFrame(): 
    #TODO
    """takes in a list of courses from the user and ads it to the specific study-Plan"""
    return 

# TODO :
def lp_periods(df : pd.DataFrame())->pd.DataFrame(): 
    """Fetches the columns named lp1, lp2 etc to a single column"""
    #nuvarande kolumner, lp1, lp2,lp3,lp4 
    return

#TODO : 
def readDataFromURL(): 
    """Reads in data directly from a URL"""
    return 

# TODO: 
def concatData(): 
    """concatenates all the data to a single dataframe """
    return 
    