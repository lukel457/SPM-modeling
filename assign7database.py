import sqlite3


# database file connection
database = sqlite3.connect("assign7.db")

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
cursor = database.cursor()

######################################################################
#sql_command = """DROP TABLE STUDENT"""
#cursor.execute(sql_command)

# SQL command to create a table in the database
sql_command = """CREATE TABLE STUDENT (
ID 		TEXT 	PRIMARY KEY 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
USERNAME	VARCHAR(20)	NOT NULL,
PASSWORD	VARCHAR(20)	NOT NULL,
GRADYEAR	INT 	NOT NULL,
MAJOR		CHAR(4) NOT NULL,
EMAIL		text	NOT NULL,
HOLD		INT	NOT NULL)
;"""

# execute the statement
#cursor.execute(sql_command)
######################################################################
#sql_command = """DROP TABLE INSTRUCTOR"""
#cursor.execute(sql_command)

# SQL command to create a table in the database
sql_command = """CREATE TABLE INSTRUCTOR (
ID 		TEXT	PRIMARY KEY 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
USERNAME	VARCHAR(20)	NOT NULL,
PASSWORD	VARCHAR(20)	NOT NULL,
TITLE		TEXT 	NOT NULL,
HIREYEAR	INT 	NOT NULL,
DEPT		CHAR(4) NOT NULL,
EMAIL		text	NOT NULL)
;"""

# execute the statement
#cursor.execute(sql_command)

######################################################################
#sql_command = """DROP TABLE ADMIN"""
#cursor.execute(sql_command)

# SQL command to create a table in the database
sql_command = """CREATE TABLE ADMIN (
ID 		TEXT	PRIMARY KEY 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
USERNAME	VARCHAR(20)	NOT NULL,
PASSWORD	VARCHAR(20)	NOT NULL,
TITLE		TEXT 	NOT NULL,
OFFICE		TEXT 	NOT NULL,
EMAIL		text	NOT NULL)
;"""

# execute the statement
#cursor.execute(sql_command)

######################################################################
#sql_command = """DROP TABLE COURSES"""
#cursor.execute(sql_command)

# SQL command to create a table for courses
sql_command = """CREATE TABLE COURSES (
CRN     INT     PRIMARY KEY     NOT NULL,
TITLE   VARCHAR(30)     NOT NULL,
PROFID  TEXT     NOT NULL,
DAY1    CHAR(1),
DAY2    CHAR(1),
DAY3    CHAR(1),
BEGIN1  INT,
BEGIN2  INT,
BEGIN3  INT,
END1    INT,
END2    INT,
END3    INT,
DEPT    CHAR(4)     NOT NULL,
SEMESTER VARCHAR(10)    NOT NULL,
CREDITS INT     NOT NULL,
YEAR    INT     NOT NULL,
SPACES	INT	NOT NULL,
FOREIGN KEY (PROFID) REFERENCES INSTRUCTOR(ID))
;"""

#cursor.execute(sql_command)

#####################################################################
#sql_command = """DROP TABLE SCHEDULE"""
#cursor.execute(sql_command)

#SQL command to create table for SCHEDULE
sql_command = """CREATE TABLE SCHEDULE (
STUDID	TEXT	NOT NULL,
CRN1	INT,
CRN2	INT,
CRN3	INT,
CRN4	INT,
CRN5	INT,
CRN6	INT,
CRN7	INT,
FOREIGN KEY (STUDID) REFERENCES STUDENT(ID),
FOREIGN KEY (CRN1) REFERENCES COURSES(CRN),
FOREIGN KEY (CRN2) REFERENCES COURSES(CRN),
FOREIGN KEY (CRN3) REFERENCES COURSES(CRN),
FOREIGN KEY (CRN4) REFERENCES COURSES(CRN),
FOREIGN KEY (CRN5) REFERENCES COURSES(CRN),
FOREIGN KEY (CRN6) REFERENCES COURSES(CRN),
FOREIGN KEY (CRN7) REFERENCES COURSES(CRN))
;"""

#cursor.execute(sql_command)

#####################################################################

# Student list
#cursor.execute("""INSERT INTO STUDENT VALUES('00010001', 'Isaac', 'Newton', 'newtoni', 'Newtonian1', 1668, 'BSAS', 'newtoni', 0);""")
#cursor.execute("""INSERT INTO STUDENT VALUES('00010002', 'Marie', 'Curie', 'curiem', 'radioActive', 1903, 'BSAS', 'curiem', 0);""")
#cursor.execute("""INSERT INTO STUDENT VALUES('00010003', 'Nikola', 'Tesla', 'teslan', 'sparky77', 1878, 'BSEE', 'telsan', 0);""")
#cursor.execute("""INSERT INTO STUDENT VALUES('00010004', 'Thomas', 'Edison', 'edisont', 'likeAlightbulb', 1879, 'BSEE', 'notcool', 0);""")
#cursor.execute("""INSERT INTO STUDENT VALUES('00010005', 'John', 'von Neumann', 'vonneumannj', 'vonNew', 1923, 'BSCO', 'vonneumannj', 0);""")
#cursor.execute("""INSERT INTO STUDENT VALUES('00010006', 'Grace', 'Hopper', 'hopperg', 'hops99', 1928, 'BCOS', 'hopperg', 0);""")
#cursor.execute("""INSERT INTO STUDENT VALUES('00010007', 'Mae', 'Jemison', 'jemisonm', 'prof22', 1981, 'BSCH', 'jemisonm', 0);""")
#cursor.execute("""INSERT INTO STUDENT VALUES('00010008', 'Mark', 'Dean', 'deanm', 'deanTheMachine', 1979, 'BSCO', 'deanm', 0);""")
#cursor.execute("""INSERT INTO STUDENT VALUES('00010009', 'Michael', 'Faraday', 'faradaym', '1cage1', 1812, 'BSAS', 'faradaym', 0);""")
#cursor.execute("""INSERT INTO STUDENT VALUES('00010010', 'Ada', 'Lovelace', 'lovelacea', 'lovelyAda', 1832, 'BCOS', 'lovelacea', 0);""")
#cursor.execute("""INSERT INTO STUDENT VALUES('00010011', 'Luke', 'Lavallee', 'lavalleel', 'cursesucks', 2019, 'BSCE', 'lavalleel', 0);""") ### student 1 added
#cursor.execute("""INSERT INTO STUDENT VALUES('00010012', 'Nick', 'Pondish', 'pondishn', 'goes2Massart', 2019, 'BSCE', 'pondishn', 1);""")  ### student 2 added

# Student Schedule (when a student is made, a schedule must be made)
#cursor.execute("""INSERT INTO SCHEDULE VALUES('00010001', NULL, NULL, NULL, NULL, NULL, NULL, NULL);""")
#cursor.execute("""INSERT INTO SCHEDULE VALUES('00010002', NULL, NULL, NULL, NULL, NULL, NULL, NULL);""")
#cursor.execute("""INSERT INTO SCHEDULE VALUES('00010003', NULL, NULL, NULL, NULL, NULL, NULL, NULL);""")
#cursor.execute("""INSERT INTO SCHEDULE VALUES('00010004', NULL, NULL, NULL, NULL, NULL, NULL, NULL);""")
#cursor.execute("""INSERT INTO SCHEDULE VALUES('00010005', NULL, NULL, NULL, NULL, NULL, NULL, NULL);""")
#cursor.execute("""INSERT INTO SCHEDULE VALUES('00010006', NULL, NULL, NULL, NULL, NULL, NULL, NULL);""")
#cursor.execute("""INSERT INTO SCHEDULE VALUES('00010007', NULL, NULL, NULL, NULL, NULL, NULL, NULL);""")
#cursor.execute("""INSERT INTO SCHEDULE VALUES('00010008', NULL, NULL, NULL, NULL, NULL, NULL, NULL);""")
#cursor.execute("""INSERT INTO SCHEDULE VALUES('00010009', NULL, NULL, NULL, NULL, NULL, NULL, NULL);""")
#cursor.execute("""INSERT INTO SCHEDULE VALUES('00010010', NULL, NULL, NULL, NULL, NULL, NULL, NULL);""")
#cursor.execute("""INSERT INTO SCHEDULE VALUES('00010011', NULL, NULL, NULL, NULL, NULL, NULL, NULL);""")
#cursor.execute("""INSERT INTO SCHEDULE VALUES('00010012', NULL, NULL, NULL, NULL, NULL, NULL, NULL);""")

# Instructor list
#cursor.execute("""INSERT INTO INSTRUCTOR VALUES('00020001', 'Joseph', 'Fourier', 'fourierj', 'ProfJ1', 'Full Prof.', 1820, 'BSEE', 'fourierj');""")
#cursor.execute("""INSERT INTO INSTRUCTOR VALUES('00020002', 'Nelson', 'Mandela', 'mandelan', 'invictusRugby', 'Full Prof.', 1994, 'HUSS', 'mandelan');""")
#cursor.execute("""INSERT INTO INSTRUCTOR VALUES('00020003', 'Galileo', 'Galilei', 'galileig', 'physics4fun', 'Full Prof.', 1600, 'BSAS', 'galileig');""")
#cursor.execute("""INSERT INTO INSTRUCTOR VALUES('00020004', 'Alan', 'Turing', 'turinga', 'humandComputer', 'Associate Prof.', 1940, 'BSCO', 'turinga');""")
#cursor.execute("""INSERT INTO INSTRUCTOR VALUES('00020005', 'Katie', 'Bouman', 'boumank', 'boomtownbouman', 'Assistant Prof.', 2019, 'BCOS', 'boumank');""")
#cursor.execute("""INSERT INTO INSTRUCTOR VALUES('00020006', 'Daniel', 'Bernoulli', 'bernoullid', 'feelTheBern', 'Associate Prof.', 1760, 'BSME', 'bernoullid');""")
#cursor.execute("""DELETE FROM INSTRUCTOR WHERE (NAME == 'Katie' and SURNAME == 'Bouman');""") ### delete one professor
#cursor.execute("""INSERT INTO INSTRUCTOR VALUES('00020007', 'Aaron', 'Carpenter', 'carpentera', 'apcCap', 'Full Prof.', 1980, 'BSCE', 'carpentera1');""")

# Admin list
#cursor.execute("""INSERT INTO ADMIN VALUES('00030001', 'Barack', 'Obama', 'obamab', 'bama4prez', 'President', 'Dobbs 1600', 'obamab');""")
#cursor.execute("""INSERT INTO ADMIN VALUES('00030002', 'Malala', 'Yousafzai', 'yousafzaim', 'regMaster', 'Registrar', 'Wentworth 101', 'yousafzaim');""")
#cursor.execute("""UPDATE ADMIN SET TITLE = 'Past President' WHERE (NAME == 'Barack' and SURNAME == 'Obama');""") ### updates Obama as the former president

# Course list
#cursor.execute("""INSERT INTO COURSES VALUES(111111, 'Advanced Programming Concepts', '00020006', 'M', 'T', 'R', 1300, 1300, 1300, 1350, 1450, 1450, 'BSEE', 'Summer', 4, 2019, 0);""")
#cursor.execute("""INSERT INTO COURSES VALUES(212121, 'English II', '00020002', 'W', 'F', 'N', 800, 1100, 0, 920, 1230, 0, 'HUSS', 'Fall', 3, 2019, 0);""")
#cursor.execute("""INSERT INTO COURSES VALUES(313131, 'Computer Architecture', '00020004', 'T', 'R', 'N', 930, 930, 0, 1050, 1050, 0, 'BSCO', 'Summer', 4, 2019, 0);""")
#cursor.execute("""INSERT INTO COURSES VALUES(414141, 'Adv. Digital Circuit Design', '00020001', 'W', 'F', 'F', 800, 800, 1000, 920, 920, 1150, 'BSEE', 'Summer', 4, 2019, 0);""")
#cursor.execute("""INSERT INTO COURSES VALUES(515151, 'Computer Networks', '00020007', 'T', 'R', 'F', 800, 800, 1300, 920, 920, 1450, 'BSCE', 'Summer', 4, 2019, 0);""")
#cursor.execute("""INSERT INTO COURSES VALUES(616161, 'Signals and Systems', '00020003', 'M', 'W', 'N', 1000, 1000, 0, 1150, 1150, 0, 'BSAS', 'Summer', 4, 2019, 0);""")
#cursor.execute("""INSERT INTO COURSES VALUES(717171, 'Multivariable Calc', '00020004', 'M', 'W', 'N', 930, 930, 0, 1100, 1100, 0, 'BSCO', 'Spring', 4, 2020, 0);""")


# QUERY FOR ALL

print("All Students")
cursor.execute("""SELECT * FROM STUDENT""")
query_result = cursor.fetchall()

for i in query_result:
	print(i)

# QUERY FOR ALL
def printInstructors(self):
	print("All Instructors")
	cursor.execute("""SELECT * FROM INSTRUCTOR""")
	query_result = cursor.fetchall()

	for i in query_result:
		print(i)

# QUERY FOR ALL
print("Entire table")
cursor.execute("""SELECT * FROM ADMIN""")
query_result = cursor.fetchall()

for i in query_result:
	print(i)

#QUERY FOR ALL
print("Entire Table")
cursor.execute("""SELECT * FROM COURSES""")
query_result = cursor.fetchall()

for i in query_result:
    print(i)

#qUERY FOR INSTRUCTORS FROM COURSES
print("Courses and their Instructors")
cursor.execute("""SELECT COURSES.CRN, COURSES.TITLE, INSTRUCTOR.NAME, INSTRUCTOR.SURNAME FROM COURSES, INSTRUCTOR WHERE (COURSES.PROFID == INSTRUCTOR.ID);""")
query_result = cursor.fetchall()

for i in query_result:
	print(i)




# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
database.commit()

# close the connection
database.close()
