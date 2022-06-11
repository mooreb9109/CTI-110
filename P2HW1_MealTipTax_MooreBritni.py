 # The program is to that calculate the total amount of a meal purchased at a restaurant
    # 6/11/2022
    # CTI-110 P2HW1 - Meal Tip Tax Calculator
    # Britni Moore
    #

meal_charge = float(input('Enter Food Cost:'))

tip = float(input('Enter Tip Percentage:'))
tip_percent = 0.15
tax = float(input('Enter Tax Percentage:'))

tax_percent = 0.06
tip_total = meal_charge * tip_percent
tax_total = meal_charge * tax_percent

print('Calculated Tip:', format(tip_total, ',.2f'))
print('Calcuted Tax:', format(tax_total, ',.2f'))
meal_total = meal_charge + tip_total + tax_total

print('Total cost including tip and tax $', format(meal_total, ',.2f'))


#----------------------------------
#The user will enter the meal cost along with the tip and tax percentage.
#Next the program will display the calculated tip and calculated tax.
#Lastly the program will display the total cost of the meal ( food charge + tip +tax )
