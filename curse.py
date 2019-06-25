from array import *

class user:
    username = ""
    password = ""

    def login(self):
        valid = 0
        input = raw_input("To log in as a student, press 1. \n To log in as a teacher, press 2. \n To log in as an administrator, press 3.")
        if input == 1:
            student newStudent
            while !valid:
                newStudent.username = raw_input("Username: ")
                newStudent.password = raw_input("Password: ")
                valid = verifyUser(newStudent.username, newStudent.password) #make this equation, simply verifies creds in DB with 0 or 1
                if !valid:
                    print "Those credentials are invalid. Try again or speak with an administrator for more details."
            print "You are now logged in, %s \n", newStudent.username
            newStudent.studentID = getStudentID(newStudent.username) #prototype, make function, inits student info for later use
            newStudent.holds = getStudentHolds(newStudent.username)
        elif input == 2:
            teacher newTeacher
            while !valid:
                newTeacher.username = raw_input("Username: ")
                newTeacher.password = raw_input("Password: ")
                valid = verifyUser(newTeacher.username, newTeacher.password)
                if !valid:
                    print "Those credentials are invalid. try again or speak with an administrator for more details."
            print "You are now logged in, %s \n", newTeacher.username
            newTeacher.employeeID = getTeacherID(newTeacher.username) #prototype, will be used to get information later
        elif input == 3:
            admin newAdmin
            while !valid:
                newAdmin.username = raw_input("Username: ")
                newAdmin.password = raw_input("Password: ")
                valid = verifyUser(newAdmin.username, newAdmin.password)
                if !valid:
                    print "Those credentials are invalid. Please try again."
            print "You are now logged in, %s \n", newAdmin.username
        return input

class admin(user):

    def printMenu(self):
        print "To see available courses, press 1."
        print "To edit a student, press 2."
        print "To view rosters, press 3."
        print "To quit, press 4."

class student(user):
    studentID = 0
    holds = 0 # will find in DB

    def printMenu(self):
        print "To see available courses, press 1."
        print "To check your schedule, press 2."
        print "To register for classes, press 3."
        print "To quit, press 4."

class teacher(user):
    employeeID = 0

    def printMenu(self):
        print "To view available courses, press 1."
        print "To view your rosters, press 2."
        print "To quit, press 3."



def main():
    quit = 0
    permission = 0
    print "Welcome to Curse!"
    userType = login() #verifies user is allowed into Curse, returns class type to get the proper functions
    while !quit:
        choice = 0
        printMenu()
        choice = raw_input("Choice: ")
        if choice == 1:
            displayCourse() #this will have filter options built into it, just meant to make main look clean
        elif choice == 2:
            if userType == 1:
                checkScheddy(newStudent.studentID) #will print the student schedule, finds it by student ID
            elif userType == 2:
                checkRosters(newTeacher.employeeID) #will print teacher roster, find it by employee ID
            else:
                editStudent() #accepts no args because this function will hold deleteStudent(), addStudent(), and the ability to edit aspects of a student
        elif choice == 3:
            if userType == 1:
                register() #enters registration mode, DO WE NEED RAC CODES????
            elif userType == 2:
                quit = 1
            else:
                viewRosters() #will reveal all rosters by class or can look by teacherID
        elif choice == 4:
            if userType == 1:
                quit = 1
            elif userType == 2:
                print "Invalid entry. Please try again. \n"
            else:
                quit = 1
        else:
            print "Invalid entry. Please try again. \n"
