
USE KURSER_M; 

create table Courses_M (
Kurskod VARCHAR, 
Poang FLOAT, 
Niva VARCHAR,
InAk VARCHAR,
FromYear TINYINT, 	
Kursnamn VARCHAR, 
Obl_val VARCHAR, 
lp1 TINYINT, 
lp2 TINYINT, 
lp3 TINYINT, 
lp4 TINYINT, 
Typ VARCHAR
);

CREATE TABLE user_tableTable ( 
userID MEDIUMINT PRIMARY KEY, 
userMail TINYTEXT, 
userPassWord TINYTEXT,
firstName TINYTEXT, 
program TINYTEXT, 
specialisering TINYTEXT, 
);
