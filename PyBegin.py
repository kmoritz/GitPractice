'''
Created on Aug 3, 2017

@author: Gregory
'''
name = input("What is your name?")
age = input("What is your age?")
difference = 0
age = int(age)
if age > 100:
    while age > 100:
        print("C'mon buddy, you'd be dead by this point. Put in your real age.")
        age = input("What is your age?")

    


while age < 100:
    difference = difference + 1
    age = age + 1
    
print(name + " must age " + str(difference) + " more years to be 100.")