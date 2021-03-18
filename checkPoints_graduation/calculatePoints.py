import pandas as pd 
import numpy as np 

courses_df = pd.read_excel('checkPoints_graduation/coursesM.xlsx')

#list_courses = courses_df['Kurskod']
course_list = list(courses_df['Kurs­kod'].iloc[0:5])
print(course_list)