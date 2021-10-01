#1) Create and Assign a type float variable called fltOne the value 10 (3)
fltOne = 10.0
#2) Create and Assign a type float variable called fltTwo the value 20 (3)
fltTwo = 20.0
#3) Create and Assign a type float variable called fltThree with the product of fltTwo and fltOne(3)
fltThree = fltOne + fltTwo
#4) Create and assign a variable called stringOne with the value "The product of fltOne and fltTwo = "(3)
stringOne = "The product of fltOne and fltTwo = "
#5) On the console, output stringOne and fltThree (in that order) (3)
print("\nTask 5:")
print(stringOne, fltThree)
#6) increment fltOne  (3)
fltOne += 1
#7)  prompt the user to provide an input to fltTwo with the message "Please provide another number for fltTwo". Ensure a float is given (4)
print("\nTask 7:")
fltTwo = float(input("Please provide another number for fltTwo: "))
#8) on the console, output the product of fltOne and flotTwo with a suitable message (3)
print("\nTask 8:")
print(stringOne, fltOne + fltTwo)
#####################################################
#9) take the input from fltTwo and apply a decision based on the number inputted .
#The decision should be based on if the user inputs a number below 100 
#the code should output "below 100" (5)
print("\nTask 9:")
if fltTwo < 100:
    print("below 100")
#10) take the difference between of fltOne and fltTwo (fltOne - fltTwo)
#Using if, else and elif, output the following: 
#If the product is below 0, output "below 0"
#if the product is 0 output "value is zero"
#if the product is above 0 output "above 0" (8)
print("\nTask 10:")
if fltOne - fltTwo < 0:
    print("below 0")
elif fltOne - fltTwo == 0:
    print("value is zero")
else:
    print("above 0")
#11) create a list called listOfInts (4)
listOfInts = []
#12 part a) create a for loop to iterate through the above list and populate the list with
#{4,6,8,10,12,14,16,18,20,22}. Output the list to the console with a suitable message(7)
print("\nTask 12:")
listOfInts = [4 + i for i in range(0,20,2)]
print("Populated 'listOfInts' be looking like:",listOfInts)
#13 part b) create a for loop to iterate through the above list and
#multiply each value by three assigning the new value to the respective 
#index in the list. The list should now look like {12,18,24.....} (8)
listOfInts = [listOfInts[i] * 3 for i in range(len(listOfInts))]
#14 part c )output listOfInts to the screen with a suitable message (3)
print("\nTask14:")
print("Updated 'listOfInts' be looking like:", listOfInts)
#####################################################
#15) create a function which calculates a decrease of a given percentage (10 marks)
# the function should be called calcPerc
#the function should take a cost parameter and a percentage parameter
#it should return the cost less the percentage amount
#For example if the paramenters are cost = 100 and percentage = 50, it should return 50. 
#For another example, if the parameters are cost = 50 and percentage = 10, it should return 45.
#The percentage value should assume 10% if no value is given
#print a test to the screen with cost set as 50 and percentage set as 10
print("\nTask 15:")
def calcPerc(cost, percentage=10):
    discount = (percentage * cost)/100
    return cost - discount
print(calcPerc(50,25))
#16) create a function called caseChanger which takes a string argument written all in lower case
#It will output all letters in lowercase except e which it will convert to capital E (10 marks)
#Perform a test print which using hello: caseChanger("hello") this should
#print hEllo to the console.
def caseChanger(oldString):
    newString = ""
    for char in oldString:
        if char == "e":
            newString += char.upper()
        else:
            newString += char.lower()
    return newString
print(caseChanger("Hello"))
#####################################################
#17)a) Create a list that represents a set of students. The list should contain the following
#students: Clark,Horan,Rai,White,Cooper,Jones,Cox,Smith (4 marks)
students = ["Clark","Horan","Rai","White","Cooper","Jones","Cox","Smith"]
#b) use a method to order the students so that they are in alphabetical order (3 marks)
students = sorted(students)
print(students)
#18) create a tuple that represents exam marks with the following data. (4 marks)
#These are the respective exam marks for the alphabetically ordered student list
# 65,66,67,80,90,65,65,93
exam_mark = (65,66,67,80,90,65,65,93)
print(exam_mark)
#19) Dictionary question (9 marks)
#create a dictionary 
#write code which adds both the student and a their corresponding mark. 
#do not perform this long hand (as in writing out the values above). Use data
#from the existing tuples above to create the dictionary
dictionary = {}
for i in range(len(students)):
    dictionary[students[i]] = exam_mark[i]
print(dictionary)