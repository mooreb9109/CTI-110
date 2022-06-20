# CTI-110
# P2HW2 - List and Sets
# Britni Moore 
# 6/18/2022
#

num1 = float(input('Enter num 1:' ' '))
num2 = float(input('Enter num 2:' ' '))
num3 = float(input('Enter num 3:' ' '))
num4 = float(input('Enter num 4:' ' '))
num5 = float(input('Enter num 5:' ' '))
num6 = float(input('Enter num 6:' ' '))

num_list = []
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)
num_list.append(num5)
num_list.append(num6)
lowest = min(num_list)
highest = max(num_list)
total = sum(num_list)
average = total / 6
num_set = set(num_list)


print('')
print('Created list \n', (num_list))
print('Smallest number in list:', lowest)
print('Largest number in list:', highest)
print('Sum of numbers in list:', total)
print('Average of numbers in list:', average) 
print('')
print('Created set\n', num_set)

#-------------------------------------------------
#The user will be asked to input a list of 6 numbers.
#The program will then store the numbers in a list.
#The lowest number , highest number , total of the numbers and the average of the numbers in the list will then be displayed.
#It will be converted to set and display the list and set content.

