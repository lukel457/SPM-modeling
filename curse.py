from array import *
import sqlite3

database = sqlite3.connect("assign7.db")
cursor = database.cursor()

class user:    

    def availCourses(self):
	print "Show available courses by [P]rofessor, [C]RN, [Y]ear, [D]epartment or [S]emester?"
	choice = raw_input("Choice: ")
	found = 0
	if choice == 'P':
	    id = raw_input("What Professor would you like to search for? (enter employee ID number): ")
	    cursor.execute("SELECT COURSES.CRN, COURSES.TITLE, INSTRUCTOR.SURNAME, COURSES.SPACES FROM COURSES, INSTRUCTOR WHERE COURSES.PROFID == INSTRUCTOR.ID AND COURSES.PROFID == '%s'"% id)
	    query_results = cursor.fetchall()
	    if len(query_results) == 0:
		print "I'm sorry, your search doesn't match any course offered."
		print " "
	    else:
	    	print "===================="
	    	print "CRN:", query_results[0][0]
	    	print "Course:", query_results[0][1]
	    	print "Instructor: Professor", query_results[0][2]
		print "Spaces Taken:", query_results[0][3], "of 8."
	    	print "===================="
	elif choice == 'C':
	    num = input("What CRN would you like to search for?: ")
	    cursor.execute("SELECT COURSES.CRN, COURSES.TITLE, INSTRUCTOR.SURNAME, COURSES.SPACES FROM COURSES, INSTRUCTOR WHERE COURSES.PROFID == INSTRUCTOR.ID AND COURSES.CRN == '%s'"% num)
	    queryResults = cursor.fetchall()
	    if len(queryResults) == 0:
		print "I'm sorry, your search doesnt match any course offered."
		print " "
	    else:
	    	print "===================="
	    	print "CRN:", queryResults[0][0]
	    	print "Course:", queryResults[0][1]
	    	print "Instructor: Professor", queryResults[0][2]
		print "Spaces Taken:", queryResults[0][3], "of 8."
	    	print "===================="
	elif choice == 'Y':
	    year = input("What year would you like to search by? Years corresponds to the year the class is offered: ")
	    cursor.execute("SELECT COURSES.CRN, COURSES.TITLE, INSTRUCTOR.SURNAME, COURSES.SPACES FROM COURSES, INSTRUCTOR WHERE COURSES.PROFID == INSTRUCTOR.ID AND COURSES.YEAR == '%s'"% year)
	    queryResults = cursor.fetchall()
	    if len(queryResults) == 0:
		print "I'm sorry, we do not have a record for that year of classes."
		print " "
	    else:
		for i in range(len(queryResults)):
		    print "===================="
		    print "CRN:", queryResults[i][0]
		    print "Course:", queryResults[i][1]
		    print "Instructor: Professor", queryResults[i][2]
		    print "Spaces Taken:", queryResults[i][3], "of 8."
		print "===================="
	elif choice == 'D':
	    sub = raw_input("What department would you like ot look for, search by 4 character department acronym (i.e. BSCO): ")
	    cursor.execute("SELECT COURSES.CRN, COURSES.TITLE, INSTRUCTOR.SURNAME, COURSES.SPACES FROM COURSES, INSTRUCTOR WHERE COURSES.PROFID == INSTRUCTOR.ID AND COURSES.DEPT == '%s'"% sub)
	    queryResults = cursor.fetchall()
	    if len(queryResults) == 0:
		print "I'm sorry, this department is not offering any courses at the moment or you made a spelling error. Please try again."
		print " "
	    else:
		for i in range(len(queryResults)):
		    print "===================="
		    print "CRN:", queryResults[i][0]
		    print "Course:", queryResults[i][1]
		    print "Instructor: Professor", queryResults[i][2]
		    print "Spaces Taken:", queryResults[i][3], "of 8."
		print "===================="
	elif choice == 'S':
	    sem = raw_input("What semester would you like to look for, [F]all, [S]pring, or Summer[M]: ")
	    if sem == 'F':
		cursor.execute("SELECT COURSES.CRN, COURSES.TITLE, INSTRUCTOR.SURNAME, COURSES.SPACES FROM COURSES, INSTRUCTOR WHERE COURSES.PROFID == INSTRUCTOR.ID AND COURSES.SEMESTER == 'Fall'")
		queryResults = cursr.fetchall()
            	if len(queryResults) == 0:
                    print "I'm sorry, this department is not offering any courses at the moment or you made a spelling error. Please try again."
                    print " "
            	else:
                    for i in range(len(queryResults)):
                    	print "===================="
                    	print "CRN:", queryResults[i][0]
                    	print "Course:", queryResults[i][1]
                    	print "Instructor: Professor", queryResults[i][2]
                    	print "Spaces Taken:", queryResults[i][3], "of 8."
                    print "===================="
	    elif sem == 'S':
                cursor.execute("SELECT COURSES.CRN, COURSES.TITLE, INSTRUCTOR.SURNAME, COURSES.SPACES FROM COURSES, INSTRUCTOR WHERE COURSES.PROFID == INSTRUCTOR.ID AND COURSES.SEMESTER == 'Spring'")
                queryResults = cursr.fetchall()
                if len(queryResults) == 0:
                    print "I'm sorry, this department is not offering any courses at the moment or you made a spelling error. Please try again."
                    print " "
                else:
                    for i in range(len(queryResults)):
                        print "===================="
                        print "CRN:", queryResults[i][0]
                        print "Course:", queryResults[i][1]
                        print "Instructor: Professor", queryResults[i][2]
                        print "Spaces Taken:", queryResults[i][3], "of 8."
                    print "===================="
	    elif sem == 'M':
                cursor.execute("SELECT COURSES.CRN, COURSES.TITLE, INSTRUCTOR.SURNAME, COURSES.SPACES FROM COURSES, INSTRUCTOR WHERE COURSES.PROFID == INSTRUCTOR.ID AND COURSES.SEMESTER == 'Summer'")
                queryResults = cursr.fetchall()
                if len(queryResults) == 0:
                    print "I'm sorry, this department is not offering any courses at the moment or you made a spelling error. Please try again."
                    print " "
                else:
                    for i in range(len(queryResults)):
                        print "===================="
                        print "CRN:", queryResults[i][0]
                        print "Course:", queryResults[i][1]
                        print "Instructor: Professor", queryResults[i][2]
                        print "Spaces Taken:", queryResults[i][3], "of 8."
                    print "===================="



class admin(user):
    
    def __init__(self):
	self.adminID = 0
	self.username = " "
	self.password = " "
	self.fName = " "
	self.lName = " "
	self.title = " "
	self.office = " "
	self.email = " "

    def verifyAdmin(self):
        sql_command = ("SELECT * FROM ADMIN WHERE ((USERNAME == ?) and (PASSWORD == ?))")
        cursor.execute(sql_command, (self.username, self.password))
        query_results = cursor.fetchall()
        if len(query_results) == 0:
            return 0
        else:	
	    self.adminID = query_results[0][0]
	    self.fName = query_results[0][1]
	    self.lName = query_results[0][2]
	    self.title = query_results[0][5]
	    self.office = query_results[0][6]
	    self.email = query_results[0][7]
	    return 1	

    def editStudent(self):
	print "If you would like to delete a student, press 1."
	print "If you would like to add a student, press 2."
	print "If you would like to edit an existing student, press 3."
	choice = input("Choice: ")
	if choice == 1:
	    id = raw_input("What is the ID of the student you want to delete?: ")
	    cursor.execute("DELETE FROM STUDENT WHERE ID == '%s'"% id)
	    cursor.execute("DELETE FROM SCHEDULE WHERE STUDID == '%s'"% id)
	    print "The student with ID number", id, "has been removed."
	elif choice == 2:
	    fName = raw_input("Student's First Name: ")
	    lName = raw_input("Student's Last Name: ")
	    id = raw_input("Student's ID: ")
	    user = raw_input("Student's Username: ")
	    password = raw_input("Student's Password: ")
	    gradYear = input("Student's Grad Year: ")
	    major = raw_input("Student's Major: ")
	    email = raw_input("Student's Email: ")
	    holds = input("Student Holds? Yes[1]/No[0]: ")
	    sqlCommand = ("INSERT INTO STUDENT VALUES(?,?,?,?,?,?,?,?,?)")
	    cursor.execute(sqlCommand, (id, fName, lName, user, password, gradYear, major, email, holds))
	    cursor.execute("INSERT INTO SCHEDULE VALUES('%s', NULL, NULL, NULL, NULL, NULL, NULL, NULL)"% id)
	elif choice == 3:
	    id = raw_input("What is the ID of the student you wish to change?:")
	    print "If you would like to change their graduation year, press 1."
	    print "If you would like to change their major, press 2."
	    print "If you would like to change their hold status, press 3."
	    choice2 = input("Choice: ")
	    if choice2 == 1:
		newYear = input("What would you like the new year to be?:")
		sqlCommand = ("UPDATE STUDENT SET GRADYEAR = ? WHERE ID == ?")	    
		cursor.execute(sqlCommand, (newYear, id))
	    elif choice2 == 2:
		maj = raw_input("What would you like the new major to be (please use 4 letter department abbreviation):")
		sqlCommand = ("UPDATE STUDENT SET MAJOR = ? WHERE ID == ?")
		cursor.execute(sqlCommand, (maj, id))
	    elif choice2 == 3:
		ans = input("Would you like to add or remove a hold. Press 1 to add and 2 to remove: ")
		if ans == 1:
		    cursor.execute("UPDATE STUDENT SET HOLDS = 1 WHERE ID = '%s'"% id)
		elif ans == 2:
		    cursor.execute("UPDATE STUDENT SET HOLDS = 0 WHERE ID = '%s'"% id)
	    else:
		print "Invalid entry, please try again."
	else:
	    print "Invalid entry, please try again."

    def checkRosters(self):
	profName = raw_input("What professor would you like to search by (use profesor last name): ")
	cursor.execute("SELECT ID FROM INSTRUCTOR WHERE SURNAME == '%s'"% profName)
	query = cursor.fetchall()
	if len(query) == 0:
	    print "That professor could not be found. Please make sure your search was accurate."
	else:
	    profID = query[0][0]
            cursor.execute("SELECT COURSES.CRN FROM COURSES WHERE PROFID == '%s'"% profID)
            queryCRN = cursor.fetchall()
            for i in range(len(queryCRN)):
            	print queryCRN[i][0]
            	cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN1 == '%s'"% queryCRN[i][0])
            	queryResults = cursor.fetchall()
            	for j in queryResults:
                    print j[0], j[1]
            	cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN2 == '%s'"% queryCRN[i][0])
            	queryResults = cursor.fetchall()
            	for j in queryResults:
                    print j[0], j[1]
            	cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN3 == '%s'"% queryCRN[i][0])
            	queryResults = cursor.fetchall()
            	for j in queryResults:
                    print j[0], j[1]
            	cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN4 == '%s'"% queryCRN[i][0])
            	queryResults = cursor.fetchall()
            	for j in queryResults:
                    print j[0], j[1]
            	cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN5 == '%s'"% queryCRN[i][0])
            	queryResults = cursor.fetchall()
            	for j in queryResults:
                    print j[0], j[1]
            	cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN6 == '%s'"% queryCRN[i][0])
            	queryResults = cursor.fetchall()
            	for j in queryResults:
                    print j[0], j[1]
            	cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN6 == '%s'"% queryCRN[i][0])
            	queryResults = cursor.fetchall()
            	for j in queryResults:
                    print j[0], j[1]
            	cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN7 == '%s'"% queryCRN[i][0])
            	queryResults = cursor.fetchall()
            	for j in queryResults:
                    print j[0], j[1]

    def printMenu(self):
        print "To see available courses, press 1."
        print "To edit a student, press 2."
        print "To view rosters, press 3."
        print "To log out, press 4."

class student(user):

    def __init__(self):
	self.fName = " "
	self.lName = " "
	self.username = " "
	self.password = " "
	self.studentID = 0
	self.gradeYear = 0
	self.major = " "
	self.email = " "
	self.holds = 0

    def verifyStudent(self):
	sql_command = ("SELECT * FROM STUDENT WHERE ((USERNAME == ?) and (PASSWORD == ?))")
	cursor.execute(sql_command, (self.username, self.password)) 
	query_results = cursor.fetchall()
	if len(query_results) == 0:
	    print '0'
	    return 0
	else:
	    self.studentID = query_results[0][0]
	    self.fName = query_results[0][1]
	    self.lName = query_results[0][2]
	    self.gradeYear = query_results[0][5]
	    self.major = query_results[0][6]
	    self.email = query_results[0][7]
	    self.holds = query_results[0][8]
	    return 1

    def printMenu(self):
        print "To see available courses, press 1."
        print "To check your schedule, press 2."
        print "To register for classes, press 3."
        print "To log out, press 4."

    def printStudent(self):
	print "Name:", self.fName, " ", self.lName
	print "Student ID:", self.studentID
	print "Year of Graduation", self.gradeYear
	print "Major:", self.major
	print "Email:", self.email, "@wit.edu"

    def checkScheddy(self):
	cursor.execute("SELECT COURSES.TITLE, COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM SCHEDULE, COURSES WHERE COURSES.CRN == SCHEDULE.CRN1 AND SCHEDULE.STUDID == '%s'"% self.studentID)
	queryResults = cursor.fetchall()
	if queryResults:
            print "Class", 1
            print "Title:", queryResults[0][0]
            print "Day 1:", queryResults[0][1]
            print "Start Time:", queryResults[0][2], "End Time:", queryResults[0][3]
            print "Day 2:", queryResults[0][4]
            print "Start Time:", queryResults[0][5], "End Time:", queryResults[0][6]
            if queryResults[0][7] != 'N':
                print "Day 3:", queryResults[0][7]
                print "Start Time:", queryResults[0][8], "End Time:", queryResults[0][9]
	cursor.execute("SELECT COURSES.TITLE, COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM SCHEDULE, COURSES WHERE COURSES.CRN == SCHEDULE.CRN2 AND SCHEDULE.STUDID == '%s'"% self.studentID)
	queryResults = cursor.fetchall()
        if queryResults:
            print "Class", 1
            print "Title:", queryResults[0][0]
            print "Day 1:", queryResults[0][1]
            print "Start Time:", queryResults[0][2], "End Time:", queryResults[0][3]
            print "Day 2:", queryResults[0][4]
            print "Start Time:", queryResults[0][5], "End Time:", queryResults[0][6]
            if queryResults[0][7] != 'N':
                print "Day 3:", queryResults[0][7]
                print "Start Time:", queryResults[0][8], "End Time:", queryResults[0][9]
	cursor.execute("SELECT COURSES.TITLE, COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM SCHEDULE, COURSES WHERE COURSES.CRN == SCHEDULE.CRN3 AND SCHEDULE.STUDID == '%s'"% self.studentID)
	queryResults = cursor.fetchall()
        if queryResults:
            print "Class", 1
            print "Title:", queryResults[0][0]
            print "Day 1:", queryResults[0][1]
            print "Start Time:", queryResults[0][2], "End Time:", queryResults[0][3]
            print "Day 2:", queryResults[0][4]
            print "Start Time:", queryResults[0][5], "End Time:", queryResults[0][6]
            if queryResults[0][7] != 'N':
                print "Day 3:", queryResults[0][7]
                print "Start Time:", queryResults[0][8], "End Time:", queryResults[0][9]
	cursor.execute("SELECT COURSES.TITLE, COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM SCHEDULE, COURSES WHERE COURSES.CRN == SCHEDULE.CRN4 AND SCHEDULE.STUDID == '%s'"% self.studentID)
	queryResults = cursor.fetchall()
        if queryResults:
            print "Class", 1
            print "Title:", queryResults[0][0]
            print "Day 1:", queryResults[0][1]
            print "Start Time:", queryResults[0][2], "End Time:", queryResults[0][3]
            print "Day 2:", queryResults[0][4]
            print "Start Time:", queryResults[0][5], "End Time:", queryResults[0][6]
            if queryResults[0][7] != 'N':
                print "Day 3:", queryResults[0][7]
                print "Start Time:", queryResults[0][8], "End Time:", queryResults[0][9]
	cursor.execute("SELECT COURSES.TITLE, COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM SCHEDULE, COURSES WHERE COURSES.CRN == SCHEDULE.CRN5 AND SCHEDULE.STUDID == '%s'"% self.studentID)
	queryResults = cursor.fetchall()
        if queryResults:
            print "Class", 1
            print "Title:", queryResults[0][0]
            print "Day 1:", queryResults[0][1]
            print "Start Time:", queryResults[0][2], "End Time:", queryResults[0][3]
            print "Day 2:", queryResults[0][4]
            print "Start Time:", queryResults[0][5], "End Time:", queryResults[0][6]
            if queryResults[0][7] != 'N':
                print "Day 3:", queryResults[0][7]
                print "Start Time:", queryResults[0][8], "End Time:", queryResults[0][9]
	cursor.execute("SELECT COURSES.TITLE, COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM SCHEDULE, COURSES WHERE COURSES.CRN == SCHEDULE.CRN6 AND SCHEDULE.STUDID == '%s'"% self.studentID)
	queryResults = cursor.fetchall()
        if queryResults:
            print "Class", 1
            print "Title:", queryResults[0][0]
            print "Day 1:", queryResults[0][1]
            print "Start Time:", queryResults[0][2], "End Time:", queryResults[0][3]
            print "Day 2:", queryResults[0][4]
            print "Start Time:", queryResults[0][5], "End Time:", queryResults[0][6]
            if queryResults[0][7] != 'N':
                print "Day 3:", queryResults[0][7]
                print "Start Time:", queryResults[0][8], "End Time:", queryResults[0][9]
	cursor.execute("SELECT COURSES.TITLE, COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM SCHEDULE, COURSES WHERE COURSES.CRN == SCHEDULE.CRN7 AND SCHEDULE.STUDID == '%s'"% self.studentID)
	queryResults = cursor.fetchall()
        if queryResults:
            print "Class", 1
            print "Title:", queryResults[0][0]
            print "Day 1:", queryResults[0][1]
            print "Start Time:", queryResults[0][2], "End Time:", queryResults[0][3]
            print "Day 2:", queryResults[0][4]
            print "Start Time:", queryResults[0][5], "End Time:", queryResults[0][6]
            if queryResults[0][7] != 'N':
                print "Day 3:", queryResults[0][7]
                print "Start Time:", queryResults[0][8], "End Time:", queryResults[0][9]
	print "===================="

    def register(self): #will need to add bounds for time conflicts
	print "To register for a class, type in the 6-digit CRN. When you are done, type 1."
	done = 0
	while done != 1:
	    error = 0
	    num = input("CRN: ")
	    if num == 1:
		done = 1
		break
	    else:
	    	# start by checking schedule to see if already registered
	    	cursor.execute("SELECT SCHEDULE.CRN1, SCHEDULE.CRN2, SCHEDULE.CRN3, SCHEDULE.CRN4, SCHEDULE.CRN5, SCHEDULE.CRN6, SCHEDULE.CRN7 FROM SCHEDULE WHERE SCHEDULE.STUDID == '%s'"% self.studentID)
	    	queryResults = cursor.fetchall()
		for i in range(7):
		    if queryResults[0][i] == num:
			error = 1
		    	print "You have already registered for this class."
		# check for space in the class
		cursor.execute("SELECT SPACES FROM COURSES WHERE CRN == '%s'"% num)
		queryResults = cursor.fetchall()
		if queryResults[0][0] > 7:
		    print "I'm sorry, this class is already full."
		    break 
	    	# check for timing conflicts with current schedule
	    	cursor.execute("SELECT COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM COURSES WHERE COURSES.CRN == '%s'"% num)
	    	query1 = cursor.fetchall()
	    	cursor.execute("SELECT COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM COURSES, SCHEDULE WHERE SCHEDULE.CRN1 == COURSES.CRN AND SCHEDULE.STUDID == '%s'"% self.studentID)
	    	queryClass1 = cursor.fetchall()
            	cursor.execute("SELECT COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM COURSES, SCHEDULE WHERE SCHEDULE.CRN2 == COURSES.CRN AND SCHEDULE.STUDID == '%s'"% self.studentID)
	   	queryClass2 = cursor.fetchall()
            	cursor.execute("SELECT COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM COURSES, SCHEDULE WHERE SCHEDULE.CRN3 == COURSES.CRN AND SCHEDULE.STUDID == '%s'"% self.studentID)
	    	queryClass3 = cursor.fetchall()
            	cursor.execute("SELECT COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM COURSES, SCHEDULE WHERE SCHEDULE.CRN4 == COURSES.CRN AND SCHEDULE.STUDID == '%s'"% self.studentID)
	    	queryClass4 = cursor.fetchall()
            	cursor.execute("SELECT COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM COURSES, SCHEDULE WHERE SCHEDULE.CRN5 == COURSES.CRN AND SCHEDULE.STUDID == '%s'"% self.studentID)
	    	queryClass5 = cursor.fetchall()
            	cursor.execute("SELECT COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM COURSES, SCHEDULE WHERE SCHEDULE.CRN6 == COURSES.CRN AND SCHEDULE.STUDID == '%s'"% self.studentID)
	    	queryClass6 = cursor.fetchall()
            	cursor.execute("SELECT COURSES.DAY1, COURSES.BEGIN1, COURSES.END1, COURSES.DAY2, COURSES.BEGIN2, COURSES.END2, COURSES.DAY3, COURSES.BEGIN3, COURSES.END3 FROM COURSES, SCHEDULE WHERE SCHEDULE.CRN7 == COURSES.CRN AND SCHEDULE.STUDID == '%s'"% self.studentID)
	    	queryClass7 = cursor.fetchall()
	    	queryResults = [queryClass1, queryClass2, queryClass3, queryClass4, queryClass5, queryClass6, queryClass7]
	    	if queryClass1:
		    if query1[0][0] == queryClass1[0][0]: #compare days of desired class with each returned class
		    	if ((query1[0][1] >= queryClass1[0][1]) and (query1[0][1] < queryClass1[0][2])) or ((query1[0][2] > queryClass1[0][1]) and (query1[0][2] <= queryClass1[0][2])): #if desired begins between the start and end of the registered class or ends between hte start and end
			    error = 1
			    print "This class overlaps with your first class."
		    if query1[0][3] == queryClass1[0][3]:
                    	if ((query1[0][4] >= queryClass1[0][4]) and (query1[0][4] < queryClass1[0][5])) or ((query1[0][5] > queryClass1[0][4]) and (query1[0][5] <= queryClass1[0][5])):
			    error = 1
			    print "This class overlaps with your first class."
		    if (query1[0][6] == queryClass1[0][6]) and (query1[0][6] != 'N'):
                    	if ((query1[0][7] >= queryClass1[0][7]) and (query1[0][7] < queryClass1[0][8])) or ((query1[0][8] > queryClass1[0][7]) and (query1[0][8] <= queryClass1[0][8])):
			    error = 1
			    print "This class overlaps with your first class"
            	elif queryClass2:
                    if query1[0][0] == queryClass2[0][0]: #compare days of desired class with each returned class
                    	if ((query1[0][1] >= queryClass2[0][1]) and (query1[0][1] < queryClass2[0][2])) or ((query1[0][2] > queryClass2[0][1]) and (query1[0][2] <= queryClass2[0][2])): #if desired begins between the st$
                            error = 1
			    print "This class overlaps with your first class."
                    if query1[0][3] == queryClass2[0][3]:
                    	if ((query1[0][4] >= queryClass2[0][4]) and (query1[0][4] < queryClass2[0][5])) or ((query1[0][5] > queryClass2[0][4]) and (query1[0][5] <= queryClass2[0][5])):
                            error = 1
			    print "This class overlaps with your first class."
                    if (query1[0][6] == queryClass2[0][6]) and (query1[0][6] != 'N'):
                    	if ((query1[0][7] >= queryClass2[0][7]) and (query1[0][7] < queryClass2[0][8])) or ((query1[0][8] > queryClass2[0][7]) and (query1[0][8] <= queryClass2[0][8])):
                            error = 1
			    print "This class overlaps with your first class"
                elif queryClass3:
                    if query1[0][0] == queryClass3[0][0]: #compare days of desired class with each returned class
                    	if ((query1[0][1] >= queryClass3[0][1]) and (query1[0][1] < queryClass3[0][2])) or ((query1[0][2] > queryClass3[0][1]) and (query1[0][2] <= queryClass3[0][2])): #if desired begins between the st$
                            error = 1
			    print "This class overlaps with your first class."
                    if query1[0][3] == queryClass3[0][3]:
                    	if ((query1[0][4] >= queryClass3[0][4]) and (query1[0][4] < queryClass3[0][5])) or ((query1[0][5] > queryClass3[0][4]) and (query1[0][5] <= queryClass3[0][5])):
                            error = 1
			    print "This class overlaps with your first class."
                    if (query1[0][6] == queryClass3[0][6]) and (query1[0][6] != 'N'):
                    	if ((query1[0][7] >= queryClass3[0][7]) and (query1[0][7] < queryClass3[0][8])) or ((query1[0][8] > queryClass3[0][7]) and (query1[0][8] <= queryClass3[0][8])):
                            error = 1
			    print "This class overlaps with your first class"
            	elif queryClass4:
                    if query1[0][0] == queryClass4[0][0]: #compare days of desired class with each returned class
                    	if ((query1[0][1] >= queryClass4[0][1]) and (query1[0][1] < queryClass4[0][2])) or ((query1[0][2] > queryClass4[0][1]) and (query1[0][2] <= queryClass4[0][2])): #if desired begins between the st$
                            error = 1
			    print "This class overlaps with your first class."
                    if query1[0][3] == queryClass4[0][3]:
                    	if ((query1[0][4] >= queryClass4[0][4]) and (query1[0][4] < queryClass4[0][5])) or ((query1[0][5] > queryClass4[0][4]) and (query1[0][5] <= queryClass4[0][5])):
                            error = 1
			    print "This class overlaps with your first class."
                    if (query1[0][6] == queryClass4[0][6]) and (query1[0][6] != 'N'):
                    	if ((query1[0][7] >= queryClass4[0][7]) and (query1[0][7] < queryClass4[0][8])) or ((query1[0][8] > queryClass4[0][7]) and (query1[0][8] <= queryClass4[0][8])):
                            error = 1
			    print "This class overlaps with your first class"
            	elif queryClass5:
                    if query1[0][0] == queryClass5[0][0]: #compare days of desired class with each returned class
                    	if ((query1[0][1] >= queryClass5[0][1]) and (query1[0][1] < queryClass5[0][2])) or ((query1[0][2] > queryClass5[0][1]) and (query1[0][2] <= queryClass5[0][2])): #if desired begins between the st$
                            error = 1
			    print "This class overlaps with your first class."
                    if query1[0][3] == queryClass5[0][3]:
                    	if ((query1[0][4] >= queryClass5[0][4]) and (query1[0][4] < queryClass5[0][5])) or ((query1[0][5] > queryClass5[0][4]) and (query1[5] <= queryClass5[0][5])):
                            error = 1
			    print "This class overlaps with your first class."
                    if (query1[0][6] == queryClass5[0][6]) and (query1[0][6] != 'N'):
                    	if ((query1[0][7] >= queryClass5[0][7]) and (query1[0][7] < queryClass5[0][8])) or ((query1[0][8] > queryClass5[0][7]) and (query1[0][8] <= queryClass5[0][8])):
                            error = 1
			    print "This class overlaps with your first class"
            	elif queryClass6:
                    if query1[0][0] == queryClass6[0][0]: #compare days of desired class with each returned class
                    	if ((query1[0][1] >= queryClass6[0][1]) and (query1[0][1] < queryClass6[0][2])) or ((query1[0][2] > queryClass6[0][1]) and (query1[0][2] <= queryClass6[0][2])): #if desired begins between the st$
                            error = 1
			    print "This class overlaps with your first class."
                    if query1[0][3] == queryClass6[0][3]:
                    	if ((query1[0][4] >= queryClass6[0][4]) and (query1[0][4] < queryClass6[0][5])) or ((query1[0][5] > queryClass6[0][4]) and (query1[0][5] <= queryClass6[0][5])):
                            error = 1
			    print "This class overlaps with your first class."
                    if (query1[0][6] == queryClass6[0][6]) and (query1[0][6] != 'N'):
                    	if ((query1[0][7] >= queryClass6[0][7]) and (query1[0][7] < queryClass6[0][8])) or ((query1[0][8] > queryClass6[0][7]) and (query1[0][8] <= queryClass6[0][8])):
                            error = 1
			    print "This class overlaps with your first class"
            	elif queryClass7: #if class 7 returned a value, then all of the classes have been fille already
                    error = 1
		    print "Your schedule is already full. You cannot take another class."
	    # append it to their schedule		    
	    if error != 1:
		if len(queryResults[0]) == 0:
		    sqlCommand = ("UPDATE SCHEDULE SET CRN1 = ? WHERE SCHEDULE.STUDID == ?")
		    cursor.execute(sqlCommand, (num, self.studentID))
		    cursor.execute("SELECT SPACES FROM COURSES WHERE COURSES.CRN == '%s'"% num)
		    query = cursor.fetchall()
		    newSpace = query[0][0]
		    newSpace += 1
		    sqlCommand = ("UPDATE COURSES SET SPACES = ? WHERE COURSES.CRN == ?")
		    cursor.execute(sqlCommand, (newSpace, num))
		elif len(queryResults[1]) == 0:
		    sqlCommand = ("UPDATE SCHEDULE SET CRN2 = ? WHERE SCHEDULE.STUDID == ?")
		    cursor.execute(sqlCommand, (num, self.studentID))
                    cursor.execute("SELECT SPACES FROM COURSES WHERE COURSES.CRN == '%s'"% num)
                    query = cursor.fetchall()
                    newSpace = query[0][0]
                    newSpace += 1
                    sqlCommand = ("UPDATE COURSES SET SPACES = ? WHERE COURSES.CRN == ?")
		elif len(queryResults[2]) == 0:
		    sqlCommand = ("UPDATE SCHEDULE SET CRN3 = ? WHERE SCHEDULE.STUDID == ?")
		    cursor.execute(sqlCommand, (num, self.studentID))
                    cursor.execute("SELECT SPACES FROM COURSES WHERE COURSES.CRN == '%s'"% num)
                    query = cursor.fetchall()
                    newSpace = query[0][0]
                    newSpace += 1
                    sqlCommand = ("UPDATE COURSES SET SPACES = ? WHERE COURSES.CRN == ?")
		elif len(queryResults[3]) == 0:
		    sqlCommand = ("UPDATE SCHEDULE SET CRN4 = ? WHERE SCHEDULE.STUDID == ?")
		    cursor.execute(sqlCommand, (num, self.studentID))
                    cursor.execute("SELECT SPACES FROM COURSES WHERE COURSES.CRN == '%s'"% num)
                    query = cursor.fetchall()
                    newSpace = query[0][0]
                    newSpace += 1
                    sqlCommand = ("UPDATE COURSES SET SPACES = ? WHERE COURSES.CRN == ?")
		elif len(queryResults[4]) == 0:
		    sqlCommand = ("UPDATE SCHEDULE SET CRN5 = ? WHERE SCHEDULE.STUDID == ?")
		    cursor.execute(sqlCommand, (num, self.studentID))
                    cursor.execute("SELECT SPACES FROM COURSES WHERE COURSES.CRN == '%s'"% num)
                    query = cursor.fetchall()
                    newSpace = query[0][0]
                    newSpace += 1
                    sqlCommand = ("UPDATE COURSES SET SPACES = ? WHERE COURSES.CRN == ?")
		elif len(queryResults[5]) == 0:
		    sqlCommand = ("UPDATE SCHEDULE SET CRN6 = ? WHERE SCHEDULE.STUDID == ?")
		    cursor.execute(sqlCommand, (num, self.studentID))
                    cursor.execute("SELECT SPACES FROM COURSES WHERE COURSES.CRN == '%s'"% num)
                    query = cursor.fetchall()
                    newSpace = query[0][0]
                    newSpace += 1
                    sqlCommand = ("UPDATE COURSES SET SPACES = ? WHERE COURSES.CRN == ?")
		else:
		    sqlCommand = ("UPDATE SCHEDULE SET CRN7 = ? WHERE SCHEDULE.STUDID == ?")
		    cursor.execute(sqlCommand, (num, self.studentID))
                    cursor.execute("SELECT SPACES FROM COURSES WHERE COURSES.CRN == '%s'"% num)
                    query = cursor.fetchall()
                    newSpace = query[0][0]
                    newSpace += 1
                    sqlCommand = ("UPDATE COURSES SET SPACES = ? WHERE COURSES.CRN == ?")
	    error = 0
	    self.checkScheddy()

class teacher(user):

    def __init__(self):
	self.fName = " "
	self.lName = " "
	self.username = " "
	self.password = " "
	self.employeeID = 0
	self.title = " "
	self.hireYear = 0
	self.department = " "
	self.email = " "

    def verifyTeacher(self):
	sql_command = ("SELECT * FROM INSTRUCTOR WHERE ((USERNAME == ?) AND (PASSWORD == ?))")	
	cursor.execute(sql_command, (self.username, self.password))
	query_results = cursor.fetchall()
	if len(query_results) == 0:
	    return 0
	else:
	    self.employeeID = query_results[0][0]
	    self.fName = query_results[0][1]
	    self.lName = query_results[0][2]
	    self.title = query_results[0][5]
	    self.hireYear = query_results[0][6]
	    self.department = query_results[0][7]
	    self.email = query_results[0][8]
	    return 1

    def printMenu(self):
        print "To view available courses, press 1."
        print "To view your rosters, press 2."
        print "To log out, press 3."

    def checkRosters(self):
	cursor.execute("SELECT COURSES.CRN FROM COURSES WHERE PROFID == '%s'"% self.employeeID)
	queryCRN = cursor.fetchall()
	for i in range(len(queryCRN)):
	    print queryCRN[i][0]
	    cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN1 == '%s'"% queryCRN[i][0])
	    queryResults = cursor.fetchall()
	    for j in queryResults:
		print j[0], j[1]
            cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN2 == '%s'"% queryCRN[i][0])
            queryResults = cursor.fetchall()
            for j in queryResults:
                print j[0], j[1]
            cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN3 == '%s'"% queryCRN[i][0])
            queryResults = cursor.fetchall()
            for j in queryResults:
                print j[0], j[1]
            cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN4 == '%s'"% queryCRN[i][0])
            queryResults = cursor.fetchall()
            for j in queryResults:
                print j[0], j[1]
            cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN5 == '%s'"% queryCRN[i][0])
            queryResults = cursor.fetchall()
            for j in queryResults:
                print j[0], j[1]
            cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN6 == '%s'"% queryCRN[i][0])
            queryResults = cursor.fetchall()
            for j in queryResults:
                print j[0], j[1]
            cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN6 == '%s'"% queryCRN[i][0])
            queryResults = cursor.fetchall()
            for j in queryResults:
                print j[0], j[1]
            cursor.execute("SELECT STUDENT.NAME, STUDENT.SURNAME FROM STUDENT, SCHEDULE WHERE STUDENT.ID == SCHEDULE.STUDID AND SCHEDULE.CRN7 == '%s'"% queryCRN[i][0])
            queryResults = cursor.fetchall()
            for j in queryResults:
                print j[0], j[1]

#main

quit = 0
done = 0
valid = 0
while valid != 1 and done != 1:
    print "Welcome to Curse!"
    userType = raw_input("To log in as a student, press 1. \nTo log in as a teacher, press 2. \nTo log in as an administrator, press 3. \nTo quit, press Q. \n")
    if userType == '1':
        newStudent = student()
        newStudent.username = raw_input("Username: ")
        newStudent.password = raw_input("Password: ")
        valid = newStudent.verifyStudent() #make this equation, simply verifies creds in DB with 0 or 1
        if valid != 1:
            print "Those credentials are invalid. Try again or speak with an administrator for more details."
        else:
            print "You are now logged in,", newStudent.fName

    elif userType == '2':
        newTeacher = teacher()
        newTeacher.username = raw_input("Username: ")
        newTeacher.password = raw_input("Password: ")
        valid = newTeacher.verifyTeacher()
        if valid != 1:
            print "Those credentials are invalid. try again or speak with an administrator for more details."
        else:
            print "You are now logged in, Prof.", newTeacher.lName

    elif userType == '3':
        newAdmin = admin()
        newAdmin.username = raw_input("Username: ")
        newAdmin.password = raw_input("Password: ")
        valid = newAdmin.verifyAdmin()
        if valid != 1:
            print "Those credentials are invalid. Please try again."
        else:
            print "You are now logged in,", newAdmin.fName

    elif userType == 'Q':
	done = 1
    else: #user put in invalid choice
	print "Invalid entry. Please try again."

    quit = 0
    while quit != 1 and done != 1 and valid == 1:
        choice = 0
        if userType == '1':
            newStudent.printMenu()
        elif userType == '2':
            newTeacher.printMenu()
        else:
	    newAdmin.printMenu()
        choice = raw_input("Choice: ")
        if choice == '1':
	    if userType == '1':
                newStudent.availCourses() #this will have filter options built into it, just meant to make main look clean
	    elif userType == '2':
	        newTeacher.availCourses()
	    elif userType == '3':
	        newAdmin.availCourses()
        elif choice == '2':
            if userType == '1':
                newStudent.checkScheddy() #will print the student schedule, finds it by student ID
            elif userType == '2':
                newTeacher.checkRosters() #will print teacher roster, find it by employee ID
            else:
                newAdmin.editStudent() #accepts no args because this function will hold deleteStudent(), addStudent(), and the ability to edit aspects of a student
        elif choice == '3':
            if userType == '1':
		if newStudent.holds == 1:
		    print "I'm sorry, there is a hold on your account. You cannot register at this time."
		else:
                    newStudent.register() #enters registration mode
            elif userType == '2':
	        print "You have logged out."
                quit = 1
		valid = 0
            else:
                newAdmin.checkRosters() #will reveal all rosters by class or can look by teacherID
        elif choice == '4':
            if userType == '2':
                print "Invalid entry. Please try again. \n"
            else:
	        print "You have logged out."
                quit = 1
		valid = 0
        else:
            print "Invalid entry. Please try again. \n"

database.commit()
database.close()
