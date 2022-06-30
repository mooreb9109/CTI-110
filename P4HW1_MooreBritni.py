# CTI-110
# P4HW1 - Score List
# Britni Moore
# 6/30/2022
# Ask user to enter for number of scores they would like to enter
# Create a loop to collect the number of scores the user wants to enter.
# After collecting all scores, the program is to do the following: Lowest score entered, score list after dropping lowest score, the average of scores in modified list

num_scores=int(input('How many scores do you want to enter? '))
num = 1
score_list=[]
A_score = 90
B_score = 80
C_score = 70
D_score = 60

while num <= num_scores:
    print('Enter score #{}: '.format(num), end= '')
    score = float(input())
    
    if (score < 0) or (score > 100):
        print('INVALID Score entered!!!!')
        print('Should be between 0 and 100')

    else:
        score_list.append(score)
        num += 1 


print('**********Results**********')
print('Lowest Score: ', min(score_list))
lowest_scored = min(score_list)

score_list.remove(lowest_scored)


print('Modified List: ',score_list)
average_scores = sum(score_list) / len(score_list)
print(f'Score Averaged: {average_scores:.2f}')

if average_scores >= A_score:
    print('Grade: A')
elif average_scores >= B_score:
    print('Grade: B')
elif average_scores >= C_score:
    print('Grade: C')
elif average_scores >= D_score:
    print('Grade: D')
else:
    print('Grade: F')
print()
print('********************************')
