#####################################################################################
##
## Name: Chen Prom 
## Date: 1/16/2024
## Class: CITP-3311
## Semester: Spring 2024
## Instructor’s Name: Magdelena Quiroz
##
## Program Title: CProm_Assignment_1
## Program Description: Write a program in C++, C or python that calculates the 
##                      average of six grades. 
##
#####################################################################################

#get user input
grade1,grade2,grade3,grade4,grade5,grade6 = input("Enter 6 grades: ").split() 

# declare a list and initialize with values from user input
my_grades = [int(grade1), int(grade2),int(grade3), int(grade4), int(grade5), int(grade6)]

# declare variables for total grade and average
total_grade = 0
grade_average = 0

# loop through list of grades and perform operation
for grade in my_grades:
    total_grade+=grade #sum the grades
    grade_average = round(total_grade/len(my_grades), 2) # divide total_grade by length of list
print("Average : " ,grade_average) # print out average to console
