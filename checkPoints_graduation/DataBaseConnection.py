import mysql.connector
#from sqlalchemy import create_engine
from sqlalchemy.engine import create_engine
import pandas as pd
import pymysql # pip install PyMySQL 

# Fuckar för mig själv --> Måste köra version 3.8.3 

class DataBaseConnection(): 
    def __init__(self): 
        self.userName = 'easyPlanAdmin'
        self.passWord = 'easyPlan1231!'
        self.url_endPoint = 'dbeasyplan.c9odibtfqcnp.us-east-2.rds.amazonaws.com'
        self.db_name = 'KURSER_M'
        self.table_name = 'Courses_M'
        self.port = '3306'
        self.dbConnection = self.__createEngingeConnection()

    def __createEngingeConnection(self): 
        "Creates the connection to the database"
        url = (
            'mysql+pymysql://'
            +self.userName+':'
            +self.passWord+'@'
            +self.url_endPoint+'/'
            +self.db_name
        )
        sqlEngine = create_engine(url)
        dbConnection = sqlEngine.connect()
        return dbConnection

    def readAllData(self): 
        "Reades in all of the data from Courses_M"
        df = pd.read_sql("SELECT * FROM "+self.table_name, self.dbConnection)
        return df

    def getUserData(self): 
        "Reades in all of the data from Courses_M"
        tableUsers = 'user_tableTable'
        df = pd.read_sql("SELECT * FROM "+tableUsers, self.dbConnection)
        return df

    def insertNewUser(self, userID, userMail, userPassWord, firstName, program, specialisering):
        "Inserts a new user to userTable"
        table_name = 'user_tableTable'
        table_cols = [
            'userID', 
            'userMail', 
            'userPassWord', 
            'firstName', 
            'program', 
            'specialisering'
        ]
        data_array = [userID, userMail, userPassWord, firstName, program, specialisering]
        df_insert = pd.DataFrame(columns=table_cols, data = [data_array])

        df_insert.to_sql(
            table_name, con=self.dbConnection, if_exists='append', index=False, method=None
        )

    def get_Specialization_Data(self, specialisering:str): 
        "Returns the data for a specification"
        tableUsers = 'user_tableTable'
        df = pd.read_sql("SELECT * FROM Courses_M WHERE Typ="+"'"+specialisering+"'" ,self.dbConnection)
        return df

    def ifNew_UserEmail(self, email:str) -> bool: 
        "Checks if the userMail is a new user. Returns True if new user,   else False"
        table_name = 'user_tableTable'
        df = pd.read_sql("SELECT userMail FROM " + table_name + " WHERE userMail="+"'"+email+"'" ,self.dbConnection)
        if pd.read_sql(
            "SELECT userMail FROM " + table_name + " WHERE userMail="+"'"+email+"'" ,self.dbConnection
            ).empty: 
            return True
        else:
            return False