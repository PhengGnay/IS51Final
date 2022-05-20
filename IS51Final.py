"""
The program is trying to display multiple outputs including
the number of grades, the average grade, and the percentages of grades
that are above the average grade.
First initialize the function to display the number of grades. 
Secondly, write a calulate_percentage_above_average() function to
calculate the percentage of grades that are above the average grade.

Function 1 will kickstart the application, it will extract from
the Final.txt file and calculate the average grade and close after the 
information has been collected.
Function 2 named percentage of grades above average will calculate 
the percentage of grades that are above the average grade.
"""


"""
infile = open #reference to the Final.txt
num_grades = [line.rstrip()] # takes away remaining spaces on the right side
close the infile

set for loop with list and use lens to count the number of items in list
set average = sum with num_grades divided by len num_grades
counter = 0

for num_grade add 1 to counter every count

initialize main function
print total number of grades
print average grade
print Percentage of grades above the average grade

"""

def main():
    infile = open("Final.txt", "r")
    grades = [line.rstrip() for line in infile]
    infile.close()
    calculate_percentage_above_average(grades) 

def calculate_percentage_above_average(grades):
    for i in range(len(grades)):
        grades[i] = int(grades[i])
    average = sum(grades)/len(grades)
    num = 0
    for grade in grades:
        if grade > average:
            num += 1
    print("Number of grades: ", len(grades))
    print("Average grade: ", average) 
    print("Percentage of grades above average: {0:2f}%".format(100*num / len(grades)))

main()
