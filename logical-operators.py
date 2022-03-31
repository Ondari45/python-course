high_income = True
good_credit = True
if high_income and good_credit:#this is the logical AND operator
    print ('Eligible for loan(and operator)')
else:
    print ('Not eligible for loan(and operator)')
##This means both conditions must be true for the output to be eligible for loan.


if high_income or good_credit:#this is the logical OR operator
    print ('Eligible for loan(or operator)')
else:
    print ('Not eligible for loan(or operator)')
##This means at least one condition must be true for the output to be eligible for loan


criminal_record = False
if high_income and not criminal_record:#this is the logical NOT operator
    print ('Eligible for loan(NOT operator)')
else:
    print ('Not eligible for loan(Not operator)')
#This means that the not operator converts the boolean function above if it was false it becomes positive



# Q. if an apllicant has high income (logical operator) good credit, they are eligible for a loan. 