# CTI-110
# P3HW2 - MealTipTax
# Britni Moore 
# 6/20/2022
#-----------------------------------
#Program will ask user to input charge for meal
#It will then ask the user the tip % they would like (15,18,20)
#The program is then going to calculate the tip and and 6 percent sales tax
#The program is to display all of these amounts (original food charge, tip, tax and total cost of meal)

meal_charge = float(input('Please enter meal total:'))
print('Enter tip amount of 15, 18, or 20:')
tip_chosen = int(input('Tip percent:' ' '))
if tip_chosen == 15:
    print('Meal price:', format(meal_charge,',.2f'))
    tip = tip_chosen
    tip_percent = tip/100
    tax = 6
    tax_percent = tax/100
    tip_total = meal_charge * tip_percent
    tax_total = meal_charge * tax_percent
    print('Tip:', format(tip_total, ',.2f'))
    print('Tax:', format(tax_total, ',.2f'))
    meal_total = meal_charge + tip_total + tax_total
    print('Total:', format(meal_total, ',.2f'))
    
elif tip_chosen == 18:
    print('Meal price:', format(meal_charge,',.2f'))
    tip = tip_chosen
    tip_percent = tip/100
    tax = 6
    tax_percent = tax/100
    tip_total = meal_charge * tip_percent
    tax_total = meal_charge * tax_percent
    print('Tip:', format(tip_total, ',.2f'))
    print('Tax:', format(tax_total, ',.2f'))
    meal_total = meal_charge + tip_total + tax_total
    print('Total:', format(meal_total, ',.2f'))
    
elif tip_chosen == 20:
    print('Meal price:', format(meal_charge,',.2f'))
    tip = tip_chosen
    tip_percent = tip/100
    tax = 6
    tax_percent = tax/100
    tip_total = meal_charge * tip_percent
    tax_total = meal_charge * tax_percent
    print('Tip:', format(tip_total, ',.2f'))
    print('Tax:', format(tax_total, ',.2f'))
    meal_total = meal_charge + tip_total + tax_total
    print('Total:', format(meal_total, ',.2f'))
    
else:
    print('That tip percent is not available. Please start over.')
    tip = int(input('Enter tip amount of 15, 18, or 20:' ' '))
    print('Meal price:', format(meal_charge,',.2f'))
    tip_percent = tip/100
    tax = 6
    tax_percent = tax/100
    tip_total = meal_charge * tip_percent
    tax_total = meal_charge * tax_percent
    print('Tip:', format(tip_total, ',.2f'))
    print('Tax:', format(tax_total, ',.2f'))
    meal_total = meal_charge + tip_total + tax_total
    print('Total:', format(meal_total, ',.2f'))
