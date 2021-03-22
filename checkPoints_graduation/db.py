userName = 'easyPlanAdmin'
passWord = 'easyPlan1231!'
url_endPoint = 'dbeasyplan.c9odibtfqcnp.us-east-2.rds.amazonaws.com'
db_name = 'KURSER_M'

import mysql.connector

connection = mysql.connector.connect(
    host = url_endPoint, 
    user = userName,
    passwd = passWord,
    db = db_name,
) # i framtiden db-proxy för detta. Stressful att anropa lambda i AWS varje gång

def lambda_handler(event, contrext): 
    cursor = connection.cursor()
    cursor.execute('SELECT * from Kurser_M')
    rows = cursor.fetchall() 

    for row in rows: 
        print(row)
