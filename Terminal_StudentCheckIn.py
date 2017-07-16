import time
import datetime

print("\nHello please check-in\n")

#Produces current check-in (local) time for txt file
now = datetime.datetime.now()
datedisplay = now.strftime("%Y-%m-%d")
currentTime = now.hour
#this is 5 pm in military time
signout = 17
#creates the template for the text file
template = "{0:15} | {1:15} | {2:10} | {3:5} | {4:30}"

#Creates the text file and header
test = open('StudentCheckin_%s.txt' %datedisplay, "a")
test.write(template.format("Last Name", "First Name", "Student ID", "Major", "Check-In Time")+"\n")
test.write("----------------------------------------------------------------------------------" + "\n")

while currentTime < signout:
    first = input("Enter first name: ")
    last = input("Enter Last Name: ")

    # This checks if the SID is an integer
    def inputID(message):
        while True:
            try:
                sid = abs(int(input(message)))
            except ValueError:
                print("Error: Student ID must only have Integers (ie 0123456)")
                continue
            else:
                return sid
                break
    sid = inputID("Enter Student ID (ie 0123456): ")
    while len(str(abs(sid))) > 7:
        sid = input("Error: The length of the Student ID can only be less than 7 numbers: ")

    major = input("Enter Major (ie CS): ")
    #Checks if the Length of the String is less than 5 Characters for the Major
    while len(major) > 5:
        major = input("Error: The length of the Major can only be less than 5 letters (ie CS): ")

    print("Check-in Time: ", time.ctime())
    #Need to clear the output after a certain time period for the next user
    print("\n")

    #This reopens the text file and add the formated columns of the users input
    test = open('StudentCheckin_%s.txt' %datedisplay, "a")
    test.write(template.format(last, first, sid, major, time.ctime()) + "\n")
    test.write("----------------------------------------------------------------------------------" + "\n")
    test.close()

#This output is produced only when it is after 5 pm
print("\nRemember to email file to Nathanael.Carr01@utrgv.edu")
print("The file is located in the same file at the python program.")