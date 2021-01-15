from payscale import *

Title = "******************* Gross Pay Calculator ***************************"
Instructions = "Please enter Your work_hour  within range of 0 to 40 and rate within $7.50 to $18.25 "

message = "Hello"


class utility(object):
    def greetings(name, greet):


        print(message+" Mr."+name+" "+greet)
        pass


    def farewell(name, greet):


        print(message+" Mr."+name+" "+byemsg)


    def title(msg):


        print(msg)
        pass


    def instruct(msg):


        print(msg)
        pass

name = input("Please enter your name :")

greet = input("Enter the greeting message :")

byemsg = input("Enter the farewell message :")
print("\n")

utility.title(Title)

utility.greetings(name, greet)
utility.instruct(Instructions)
Calculate_sal(work_hour())

utility.farewell(name, byemsg)
