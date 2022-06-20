# CTI-110
# P3HW1 - Debugging
# Britni Moore 
# 6/20/2022
#-----------------------------------
# This program asks user for number grade and outputs a letter grade.
# System uses 10-point grading scale
def main():
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50    
    score = int(input('Enter grade: '))
    if score >= A_score:
        print('Your grade is: A')
    elif score > B_score:
        print('Your grade is: B')
    elif score > C_score:
        print('Your grade is: C')
    elif score > D_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F') 
main()
