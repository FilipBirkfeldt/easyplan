userName = 'easyPlanAdmin'
passWord = 'easyPlan1231!'
url_endPoint = 'dbeasyplan.c9odibtfqcnp.us-east-2.rds.amazonaws.com'
db_name = 'KURSER_M'
table_name = 'Courses_M'

import mysql.connector
from sqlalchemy import create_engine 

connection = mysql.connector.connect(
    host = url_endPoint, 
    user = userName,
    passwd = passWord,
    db = db_name,
) # i framtiden db-proxy för detta. Stressful att anropa lambda i AWS varje gång

def handler(): 
    cursor = connection.cursor()
    cursor.execute('SELECT * from '+table_name)
    rows = cursor.fetchall() 
    print(rows)

    for row in rows: 
        print(row)


handler()

def readInDF(): 
    host = url_endPoint, 
    user = userName,
    passwd = passWord,
    db = db_name,
    cnx = create_engine('').connect() 