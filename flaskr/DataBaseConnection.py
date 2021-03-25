#import mysql.connector
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
        "Inserts a new user to userTable, return True if possible, else return False"

        newUser = self.ifNew_UserEmail(userMail)
        if newUser == False: 
            return False
        elif newUser == True: 
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
            return True

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

    def get_Specialization_Data(self, specialisering:str): 
        "Returns the data for a specification"
        tableUsers = 'user_tableTable'
        df = pd.read_sql("SELECT * FROM Courses_M WHERE Typ="+"'"+specialisering+"'" ,self.dbConnection)
        return df

    def get_UserPassword(self, email:str):
        table_name = 'user_tableTable'
        df = pd.read_sql("SELECT userPassWord FROM " + table_name + " WHERE userMail="+"'"+email+"'", self.dbConnection)
        return df.iloc[0][0]

    def getAllUserData_from_email(self, userEmail:str) -> dict: 
        "Returns all the info for the user given the userEmail"
        table_name = 'user_tableTable'
        df = pd.read_sql("SELECT * FROM " + table_name + " WHERE userMail="+"'"+userEmail+"'" ,self.dbConnection)
        return ({
            'userID' : df['userID'].values, 
            'userMail' : df['userMail'].values,
            'userPassWord' : df['userPassWord'].values,
            'firstName' : df['firstName'].values, 
            'program' : df['program'].values, 
            'specialisering' : df['specialisering'].values
        })

class User(DataBaseConnection):
    def __init__(self):
        self.userId = id
        self.email_address : str
        self.password : str
        self.FirstName : str
        #LastName : str
        self.Program : str
        self.Specialization : str
    def create_user(self, df_user):
        self.email_address = df_user['userMail'].iloc[0]
        self.password = df_user['userPassWord'].iloc[0]
        self.FirstName = df_user['firstName'].iloc[0]
        self.Program = df_user['program'].iloc[0]
        self.Specialization = df_user['specialisering'].iloc[0]
        self.authenticated = True

    def is_authenticated(self):
        return self.authenticated
    
    def get_id(self):
        return self.email_address
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
if __name__ == '__main__':
    dbConnection = DataBaseConnection()
    df = dbConnection.getUserData()
    df = df.loc[df['userMail'] == 'test@test.test']
    user_to_create = User()
    user_to_create.create_user(df)
    if not df.empty:
        print(type(user_to_create.password))
    else:
        print("Naah")
    #print(df)

    

