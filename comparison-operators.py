name = input('Please enter your name: ')# prompts the user to enter their name
if len(name) <3: #limits the name to atleast 3 characters
    print ("Name should not be less than 3 characters")
elif len(name) > 20:#limits the name to utmost 20 characters
    print("Name should not be more than 10 characters")
else:
    print("Name looks  good")


#Q. If the name is less than 3 characters, the out put should be the name is less than 3 characters, if the name si more than 20 characters, the output should be the name is more than 50 charaters; If the name is between 3-20 characters, the output should be name looks good
