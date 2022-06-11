# In this assignment I will create a program that allows user to enter the name and cost of an expense.
# 6/11/2022
# CTI-110 P1HW2 - Basic Math
# Britni Moore
#
nam_Exp = input("Enter name of expense: ")
mon_Charge = input("Enter monthly charge: ")

monthly_tax=float(mon_Charge)*(0.06)
monthly_charge= float(float(monthly_tax) + float(mon_Charge))
annual=float(float(monthly_charge)*12)

print("Bill: "+str(nam_Exp)+" --------- Before Tax: $"+format(float(mon_Charge),".2f"))
print("Monthly Tax: $"+format(monthly_tax,".2f"))
print("Monthly Charge: $"+format(monthly_charge,".2f"))
print("Annual Charge: $"+format(annual,".2f"))


#---------------------------------------------------------------------------------
#The user will enter name of expense or bill
#The user will then enter the monthly charge of that expense or bill without taxes.
#Program will give you the monthly & annual charges with a 6% tax
