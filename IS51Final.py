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

reference num * 100 to set percentage divided by len num_grades

initialize main function
print total number of grades
print average grade
print Percentage of grades above the average grade 

"""