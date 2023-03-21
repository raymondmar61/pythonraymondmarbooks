#Python For Programmers by Paul Deitel Chapter 09 Files And Exceptions
with open("accountscreatetextfile.txt", mode="w") as accountsvariableobject:
    accountsvariableobject.write("100 Jones 24.98\n")
    accountsvariableobject.write("200 Doe  345.67\n")
    accountsvariableobject.write("300 White 0.00\n")
    accountsvariableobject.write("400 Stone -42.16\n")
    accountsvariableobject.write("500 Rich 224.62\n")
    print("600 printstatementwritetotextfile 123.45", file=accountsvariableobject)
with open("accountscreatetextfile.txt", mode="r") as accountsvariableobject:
    print(f'{"Account":<10}{"Name":<40}{"Balance":<10}') #header for the three columns and its lengths
    for eachaccountsvariableobject in accountsvariableobject:
        account, name, balance = eachaccountsvariableobject.split() #The split method returns tokens in the line as a list unpacked to variables.  The default is split discards the newline character \n.
        print(f"{account:<10}{name:<40}{balance:<10}") #displays the variables in columns using field widths
        '''
        Account   Name                                    Balance   
        100       Jones                                   24.98     
        200       Doe                                     345.67    
        300       White                                   0.00      
        400       Stone                                   -42.16    
        500       Rich                                    224.62    
        600       printstatementwritetotextfile           123.45
        '''
#Update text file.  RM:  too long and too difficult.  I think there's a better way I learned in the past.
accounts = open("accountscreatetextfile.txt", "r")
tempfile = open("tempfile.txt", "w")
with accounts, tempfile:
    for eachaccounts in accounts:
        account, name, balance = eachaccounts.split()
        if account != "300":
            tempfile.write(eachaccounts)
        else:
            newrecord = " ".join([account, "Williams", balance])
            tempfile.write(newrecord + "\n")
with open("tempfile.txt", "r") as read:
    for eachread in read.readlines():
        print(eachread)
        '''
        100 Jones 24.98

        200 Doe  345.67

        300 Williams 0.00

        400 Stone -42.16

        500 Rich 224.62

        600 printstatementwritetotextfile 123.45
        '''
#delete old accountscreatetextfile.txt, rename tempfile as the new accountscreatetextfile.txt
import os
os.remove("accountscreatetextfile.txt")
os.rename("tempfile.txt", "accountscreatetextfile.txt")
with open("accountscreatetextfile.txt", "r") as fileobjectvariable:
    for eachfileobjectvariable in fileobjectvariable:
        print(eachfileobjectvariable)
        '''
        100 Jones 24.98

        200 Doe  345.67

        300 Williams 0.00

        400 Stone -42.16

        500 Rich 224.62

        600 printstatementwritetotextfile 123.45
        '''
#Serializing is convert Python objects to JSON text format
accountsdictionary = {"accounts": [{"account": 100, "name": "Jones", "balance": 24.98}, {"account": 200, "name": "Doe", "balance": 345.67}]}
print(accountsdictionary) #print {'accounts': [{'account': 100, 'name': 'Jones', 'balance': 24.98}, {'account': 200, 'name': 'Doe', 'balance': 345.67}]}
import json
with open("accountsjson.json", "w") as accountsvariableobject:
    json.dump(accountsdictionary, accountsvariableobject) #The dump function serializes the dictionary accountsdictionary
with open("accountsjson.json", "r") as accountsvariableobject:
    accountsjson = json.load(accountsvariableobject)
print(accountsjson) #print {'accounts': [{'account': 100, 'name': 'Jones', 'balance': 24.98}, {'account': 200, 'name': 'Doe', 'balance': 345.67}]}
print(type(accountsjson)) #print <class 'dict'>
print(accountsjson["accounts"]) #print [{'account': 100, 'name': 'Jones', 'balance': 24.98}, {'account': 200, 'name': 'Doe', 'balance': 345.67}]
print(type(accountsjson["accounts"])) #print <class 'list'>
print(accountsjson["accounts"][0]) #print {'account': 100, 'name': 'Jones', 'balance': 24.98}
print(accountsjson["accounts"][1]) #print {'account': 200, 'name': 'Doe', 'balance': 345.67}
with open("accountsjson.json", "r") as accountsvariableobject:
    print(json.dumps(json.load(accountsvariableobject), indent=4))
    '''
    {
        "accounts": [
            {
                "account": 100,
                "name": "Jones",
                "balance": 24.98
            },
            {
                "account": 200,
                "name": "Doe",
                "balance": 345.67
            }
        ]
    }
    '''
#zerodivisionerror = 10 / 0 #return ZeroDivisionError: division by zero
#typehelloforinteger = int(input("Enter an integer by typing hello: ")) #return ValueError: invalid literal for int() with base 10: 'hello'
while True:
    try:
        # numbernumerator = int(input("Enter numerator: "))
        # numberdenominator = int(input("Enter denominator: "))
        numbernumerator = 5
        numberdenominator = 10
        result = numbernumerator / numberdenominator
    except ValueError:
        print("Tried to convert non-numeric value to integer.  Enter two integers.\n")
    except ZeroDivisionError:
        print("Division by zero.  Attempted to divide by zero.\n")
    else:
        print("No except errors", str(numbernumerator), "divided by", str(numberdenominator), "equals", str(numbernumerator / numberdenominator))
        break
'''
No except errors 5 divided by 10 equals 0.5
'''
#The finally clause guarantees execution.  In Python, we prefer the with statement for the purpose and place other code in the finally.
try:
    print("try suite with no exceptions raised")
except:
    print("except isn't executed")
else:
    print("else executes because no exceptions in the try suite")
finally:
    print("finally always executes")
'''
try suite with no exceptions raised
else executes because no exceptions in the try suite
finally always executes
'''
try:
    print("try suite an exception raised")
    int("hello")
    print("error because hello in the int function")
except ValueError:
    print("a ValueError occurred")
else:
    print("else doesn't execute because an exception occurred")
finally:
    print("finally always executes")
'''
try suite an exception raised
a ValueError occurred
finally always executes
'''
try:
    with open("filenotexist.txt", "r") as tryexceptfilenotfound:
        print(f'{"ID":<3}{"Name":<7}{"Grade"}')
        for student in tryexceptfilenotfound:
            studentid, name, grade = tryexceptfilenotfound.split()
            print(f'{studentid:<3}{name:<7}{grade}')
except FileNotFoundError:
    print("The file name specified doesn't exist")
'''
The file name specified doesn't exist
'''
import csv
with open("accountscsvfile.csv", mode="w", newline="") as accountscreatecsvfile:
    writer = csv.writer(accountscreatecsvfile)
    writer.writerow([100, "Jones", 24.98])
    writer.writerow([200, "Doe", 345.67])
    writer.writerow([300, "White", 0.00])
    writer.writerow([400, "Stone", -42.16])
    writer.writerow([500, "Rich", 224.62])
with open("accountscsvfile.csv", "r", newline="") as accountscreatecsvfile:
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}') #The >10 means right align?
    reader = csv.reader(accountscreatecsvfile)
    for eachreader in reader:
        account, name, balance = eachreader
        print(f'{account:<10}{name:<10}{balance:>10}') #The >10 means right align?
'''
Account   Name         Balance
100       Jones          24.98
200       Doe           345.67
300       White            0.0
400       Stone         -42.16
500       Rich          224.62
'''
import pandas as pd
dfdataframe = pd.read_csv("accountscsvfile.csv", names=["account", "name", "balance"])
print(dfdataframe)
'''
   account   name  balance
0      100  Jones    24.98
1      200    Doe   345.67
2      300  White     0.00
3      400  Stone   -42.16
4      500   Rich   224.62
'''
dfdataframe.to_csv("pandadataframetocsvfile.csv", index=False) #index=False means exclude index numbers or index column
with open("pandadataframetocsvfile.csv", "r", newline="") as pandasaccountscreatecsvfile:
    reader = csv.reader(pandasaccountscreatecsvfile)
    for eachreader in reader:
        account, name, balance = eachreader
        print(f'{account:<10}{name:<10}{balance:>10}') #The >10 means right align?
'''
account   name         balance
100       Jones          24.98
200       Doe           345.67
300       White            0.0
400       Stone         -42.16
500       Rich          224.62
'''

#Python For Programmers by Paul Deitel Chapter 10 Object-Oriented Programming
#Everything in Python is an object.  Houses are built from blueprints.  Objects are built from classes.  Object-based programming is create objects and use objects from existing classes.  For example, int, float, str, list, tuple, dict, set, Decimal from the standard library, arrays from NumPy, Figures from Matplotlib, and DataFrames from Pandas.
#Inheritance or inheriting:  take an attribute or variable from another class
#Methods:  a function in a class
#Base class:  The initial class or the first class.  Also called superclass.
#Derived class:  The new class or the class created after the base class.  Also called subclass.
#Polymorphism:  Program "in the general" rather than "in the specific."  Send the same method call to objects possibly of many different types.  Each object responds by "doing the right thing."  The same method call takes on "many forms."
from decimal import Decimal
class Account:
    """Class description or class docstring Account class for maintaining a bank account balance."""
    def __init__(self, name, balance):
        if balance < Decimal("0.00"):
            raise ValueError("Initial balance must be greater than or equal to zero.")
        self.name = name
        self.balance = balance
    def goingaheadofchapter10(self):
        print(self.name + " has a balance of " + str(self.balance) + ".")
    def depositclassmethod(self, amount):
        """Account class method depositclassmethod to deposit money to the account."""
        if amount < Decimal("0.00"):
            raise ValueError("amount must be positive")
        self.balance += amount


#print(Account?) #print SyntaxError: invalid syntax.  To view any class’s docstring in IPython, type the class name and a question mark, then press Enter.  RM:  how does it work not in IPython?
#The class name Account is used in a constructor expression to create an object for Account.  The class name Account also invokes the class's __init__ method.  __init__ is the initializing class object.
#account1 creates a new object.  The __init__ method initializes the data.  Each new class you create provides an __init__ method which specifies how to initialize an object's data attributes.
#When you call a method for a specific object, Python implicitly passes a reference to that object as the method's first argument.  Python programmers call a method's first parameter self.  A class's methods must use the self reference to access the object's attributes and other methods.  The __init__ method also specifies parameters for the other variables.
#When an object of a class is created, the object doesn't have any attributes.  The attributes are added dynamically using the self.attributename = value.
account1 = Account("John Green", Decimal("50.00"))
account1.goingaheadofchapter10() #return John Green has a balance of 50.00.
print(account1.balance) #print 50.00
account1.balance = Decimal("-1000.00")
print(account1.balance) #print -1000.00
#Any attribute name beginning with an underscore is for a class's internal use only.  Attributes don't begin with an underscore are considered ppublicly accessible.
classparameters = Account("John Green vars properties", Decimal("50.00")) #source https://stackoverflow.com/questions/5969806/print-all-properties-of-a-python-class
print(vars(classparameters)) #print {'name': 'John Green vars properties', 'balance': Decimal('50.00')}