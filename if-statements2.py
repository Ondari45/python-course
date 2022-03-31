price = 1000000
good_credit = True
if good_credit:
    down_payment = int(0.1* price)
else:
    down_payment = int(0.2* price)
print (f'Your down payment: ${down_payment}' )
    
#Q: Imagine the price of a house is $1m, if the buyer has good credit they need to put down 10% the price of the property; Otherwise they need to put down 20%. Write a program with these rules and display the down payment required for a buyer with good credit 
