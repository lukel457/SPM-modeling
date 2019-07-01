from array import *

class user:
    username = ""
    password = ""

    def verifyUser(self, name, password, user):
        for users in Users:
            if users.username == name: #if one of the users has a matching username
                if users.password == password: #then check password for match
		    if users.userLevel == user:
                	return 1 #creds are valid if both password and username match a user
        return 0 #if the function gets here the creds didnt match a user, therefore they are invalid

    def availCourses(self):
	print "Show available courses by [P]rofessor, [C]RN, [L]evel, or [S]ubject?"
	choice = raw_input("Choice: ")
	found = 0
	if choice == 'P':
	    print "What Professor would you like to search for? (enter employee ID number)"
	    choice2 = raw_input("Employee ID: ")
	    for classes in Classes:
		if classes.professor.employeeID == choice2:
		    classes.printClass()
		    found = 1
	    if found == 0:
    	        print "I'm sorry, we could not find that professor. Make sure the employee ID was typed correct."
	elif choice == 'C':
	    print "What class are you looking for?"
	    num = raw_input("CRN: ")
	    for classes in Classes:
		if classes.CRN == num:
		    classes.printClass()
		    found == 1
	    if found == 0:
 	        print "I'm sorry, we could not find a class with that CRN. Make sure you are searching the proper CRN."
	elif choice == 'L':
	    print "What level would you like to search through? [1 (freshman) <-> 5 (fifth-year)]"
	    lev = raw_input("Level: ")
	    for classes in Classes:
		if classes.level == lev:
		    classes.printClass()
		    found = 1
	    if found == 0:
		print "I'm sorry, we could not find any classes offered at that level at this time."
	elif choice == 'S':
	    print "What subject would you like to search through?, {Electrical, CompSci, English, Math, Science(dud class)}"
	    sub = raw_input("Subject: ")
	    for classes in Classes:
		if classes.subject == sub:
		    classes.printClass()
		    found = 1
	    if found == 0:
		print "I'm sorry, there are no classes under that subject. Please choose from the ones provided."
	else: 
	    print "Invalid input. Try again."

class admin(user):
    userLevel = 3

    def __init__(self, name, password):
	self.username = name
	self.password = password
	self.userLevel = 3

    def printMenu(self):
        print "To see available courses, press 1."
        print "To edit a student, press 2."
        print "To view rosters, press 3."
        print "To log out, press 4."

class student(user):
    userLevel = 1
    studentID = 0
    holds = 0 # will find in DB
    level = " " # represents grade i.e. 1-5 (fifth years potentially)
    schedule = [] #will be a list of courses

    def __init__(self, name, password, sID, hold, level):
	self.username = name
	self.password = password
	self.studentID = sID
	self.userLevel = 1
	self.holds = hold
	self.level = level

    def printMenu(self):
        print "To see available courses, press 1."
        print "To check your schedule, press 2."
        print "To register for classes, press 3."
        print "To log out, press 4."

    def getStudentID(self, name, password):
	for users in Users:
	    if users.username == name:
		if users.password == password:
		    return users.studentID

    def getStudentHolds(self, name, password):
	for users in Users:
	    if users.username == name:
		if users.password == password:
		    return users.holds

    def getStudentLevel(self, name, password):
	for users in Users:
	    if users.username == name:
		if users.password == password:
		    return users.level

    def checkScheddy(self, name, ID):
	for users in Users:
	    if users.username == name:
		if users.studentID == ID:
		    if len(users.schedule) == 0:
			print "User has no schedule made."
		    else:
			for i in range(len(user.schedule)):
			    print "Class", i+1, ":", user.schedule[i]

    def printScheddy(self):
	if len(self.schedule) > 0:
	    for i in range(len(self.schedule)):
		print "Class", i+1, ":"
		self.schedule[i].printClass()
	else:
	    print "User has no schedule made."

    def register(self, name, ID): #will need to add bounds for co/prereq, time conflicts
	for users in Users:
	    if users.username == name:
		if users.studentID == ID:
		    done = 0
		    while done != 1:
			print "Type the 6-digit CRN of the class you would like to register for, or type 'D' when done."
			num = raw_input("CRN: ")
			if num == 'D':
			    users.printScheddy()
			    done = 1
			for classes in Classes:
			    if classes.CRN == num: #find the class first
				if classes.level > users.level: #check to see if the class is made for the students year or lower
				    print "I'm sorry, due to your year you are not eligible to take this class."
				else:
				    users.schedule.append(classes)
				    classes.classRoster.append(users)

class teacher(user):
    employeeID = " "
    userLevel = 2

    def __init__(self, name, password, eID):
	self.username = name
	self.password = password
	self.employeeID = eID
	self.userLevel = 2

    def printMenu(self):
        print "To view available courses, press 1."
        print "To view your rosters, press 2."
        print "To log out, press 3."

    def checkRosters(self, eID):
	for classes in Classes:
	    if classes.professor.employeeID == eID:
		print classes.className,":"
		for people in classes.classRoster:
		    print people.username

    def getTeacherID(self, name, password):
	for users in Users:
	    if users.username == name:
		if users.password == password:
		    return users.employeeID

class course:
    className = " "
    CRN = " "
#    professor = teacher(" "," "," ") 
#    classRoster = []
#    times = []
#    days = []
    subject = " "
    level = 0
    prerequisites = [] #will hold CRN of prereqs, if any
    corequisites = [] #will hold CRN of coreqs, if any

    def __init__(self, cname, CRN, name, password, eID, numDays, subject, level):
	self.className = cname
	self.CRN = CRN
	self.professor = teacher(name, password, eID)
	self.subject = subject
	self.level = level
	self.times = []
	self.days = []
	for i in range(numDays): #will be used to create classes in the DB, will require user input to create from admin class
	    day = 1
	    self.days.append(day)
	    time = 11
	    self.times.append(time)
	#there is no pre/coreq for now, will be done as it is in day/time setup when the user is ready

    def printClass(self):
	print "Class:", self.className
	print "CRN:", self.CRN
	print "Professor:", self.professor.username   ##Doesnt work for some reason##
	print "Level:", self.level
	print "Subject:", self.subject
	for d in range(len(self.days)):
	    print "Day:", self.days[d], "Time:", self.times[d]
	if len(self.prerequisites) > 0:
	    for p in self.prerequisites:
		print "Prerequisite:", p
	if len(self.corequisites) > 0:
	    for c in self.corequisites:
		print "Corequite:", c
	    
    def addRoster(self):
	self.classRoster = []
	for i in range(3):
	    self.classRoster.append(student("Luke","cursesucks",000000,0,3))

def verifyUser(self, name, password):
    for users in self.Users:
        if users.username == name: #if one of the users has a matching username
            if users.password == password: #then check password for match
                return 1 #creds are valid if both password and username match a user
    return 0 #if the function gets here the creds didnt match a user, therefore they are invalid

#main

Users = [] # create "User DB" for testing
user0 = teacher("Carpenter","apc101","111111")
user1 = student("Luke","cursesucks",000000,0,3)
user2 = admin("Admin","admin")
user3 = teacher("Bynoe", "networks101", "101010")
Users.append(user0)
Users.append(user1)
Users.append(user2)
Users.append(user3)

Classes = [] # create "Class DB" for testing
class1 = course("Computer Newtorks","111111", "Bynoe", "networks101", "101010", 3, "Electrical", 3)
class2 = course("Applied Programming Concepts","111112", "Carpenter", "apc101", "111111", 2, "CompSci", 3)
class3 = course("Adv. Circuit Design","111113", "Zeman", "adcd101", "212121", 2, "Electrical", 2)
class4 = course("Comp. Arch.","111114", "Rawlins", "arch101", "313131", 1, "Electrical", 4)
class5 = course("Signals","111115", "Basnet", "signals101", "414141", 2, "Math", 1)
class6 = course("English II","111116", "Dow", "wierd101", "515151", 1, "English", 2)
Classes.append(class1)
Classes.append(class2)
Classes.append(class3)
Classes.append(class4)
Classes.append(class5)
Classes.append(class6)
Classes[0].addRoster()

quit = 0
print "Welcome to Curse!"
done = 0
valid = 0
while valid != 1 and done != 1:
    userType = raw_input("To log in as a student, press 1. \nTo log in as a teacher, press 2. \nTo log in as an administrator, press 3. \nTo quit, press 'Q'. \n")
    if userType == '1':
        newStudent = student(" "," ",0,0,0)
        while valid != 1:
            newStudent.username = raw_input("Username: ")
            newStudent.password = raw_input("Password: ")
            valid = newStudent.verifyUser(newStudent.username, newStudent.password, newStudent.userLevel) #make this equation, simply verifies creds in DB with 0 or 1
            if valid != 1:
                print "Those credentials are invalid. Try again or speak with an administrator for more details."
            else:
                print "You are now logged in,", newStudent.username
                newStudent.studentID = newStudent.getStudentID(newStudent.username, newStudent.password) #prototype, make function, inits student info for later use
                newStudent.holds = newStudent.getStudentHolds(newStudent.username, newStudent.password)
		newStudent.level = newStudent.getStudentLevel(newStudent.username, newStudent.password)
    elif userType == '2':
        newTeacher = teacher(" "," "," ")
        while valid != 1:
            newTeacher.username = raw_input("Username: ")
            newTeacher.password = raw_input("Password: ")
            valid = newTeacher.verifyUser(newTeacher.username, newTeacher.password, newTeacher.userLevel)
            if valid != 1:
                print "Those credentials are invalid. try again or speak with an administrator for more details."
            else:
                print "You are now logged in,", newTeacher.username
                newTeacher.employeeID = newTeacher.getTeacherID(newTeacher.username, newTeacher.password) #prototype, will be used to get information later
    elif userType == '3':
        newAdmin = admin(" "," ")
        while valid != 1:
            newAdmin.username = raw_input("Username: ")
            newAdmin.password = raw_input("Password: ")
            valid = newAdmin.verifyUser(newAdmin.username, newAdmin.password, newAdmin.userLevel)
            if valid != 1:
                print "Those credentials are invalid. Please try again."
            else:
                print "You are now logged in,", newAdmin.username
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
                newStudent.checkScheddy(newStudent.username, newStudent.studentID) #will print the student schedule, finds it by student ID
            elif userType == '2':
                newTeacher.checkRosters(newTeacher.employeeID) #will print teacher roster, find it by employee ID
            else:
                newAdmin.editStudent() #accepts no args because this function will hold deleteStudent(), addStudent(), and the ability to edit aspects of a student
        elif choice == '3':
            if userType == '1':
                newStudent.register(newStudent.username, newStudent.studentID) #enters registration mode
            elif userType == '2':
	        print "You have logged out."
                quit = 1
		valid = 0
            else:
                newAdmin.viewRosters() #will reveal all rosters by class or can look by teacherID
        elif choice == '4':
            if userType == '2':
                print "Invalid entry. Please try again. \n"
            else:
	        print "You have logged out."
                quit = 1
		valid = 0
        else:
            print "Invalid entry. Please try again. \n"

