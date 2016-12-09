__author__ = 'jc451634'
"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales=1
while sales > 0:
    sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * 10/100
    print ('Bonus is' , bonus)
else:
    bonus = sales * .15
    print ('Bonus is', bonus)

