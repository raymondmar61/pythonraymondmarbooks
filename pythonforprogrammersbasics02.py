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
from timewithproperties import Time #timewithproperties.py in same directory
wakeuptimeobject = Time(hour=6, minute=30) #Create an object
print(wakeuptimeobject.__repr__()) #print Time(hour=6, minute=30, second=0).  #Display an object
print(wakeuptimeobject.__str__()) #print 6:30:00 AM.  #Display an object
print(wakeuptimeobject) #print 6:30:00 AM.  #Display an object
print(wakeuptimeobject.hour) #print 6.  #Display a property
wakeuptimeobject.set_time(hour=7, minute=45) #Use Time's set_time method def set_time(self, hour=0, minute=0, second=0) which is like Time's __init__
print(wakeuptimeobject) #print 7:45:00 AM
wakeuptimeobject.hour = 6 #Call the hour method to set 6 as the argument
print(wakeuptimeobject.__repr__()) #print Time(hour=6, minute=45, second=0).  #Display an object
print(wakeuptimeobject.__str__()) #print 6:45:00 AM.  #Display an object
print(wakeuptimeobject) #print 6:45:00 AM
class PrivateClass:
    def __init__(self):
        self.publicdata = "public"
        self.__privatedata = "private begins with two underscores"
    def printpublicdata(self):
        print("Printing self.publicdata " + self.publicdata)
    def printprivatedata(self):
        return "Did printing self.__privatedata work? " + self.__privatedata


myobjectcreateobject = PrivateClass()
print(myobjectcreateobject) #print <__main__.PrivateClass object at 0x7effd8ca3310>
print(myobjectcreateobject.publicdata) #print public
myobjectcreateobject.printpublicdata() #return Printing self.publicdata public
# print(myobjectcreateobject.__privatedata) #print AttributeError: 'PrivateClass' object has no attribute '__privatedata'
print(myobjectcreateobject.printprivatedata()) #print Did printing self.__privatedata work? private begins with two underscores
#Inheritance is base classes and subclasses.  Loan is a base class.  CarLoan, HomeImprovementLoan, and MortgageLoan are subclasses.  Base classes tend to be more general.  Subclasses tend to be more specific.  More examples are student base class and graduate student and undergraduate student subclasses; shape base class and circle, triangle, rectangle, sphere, and cube subclasses; bankaccount base class and checking account and savings account subclasses; vehicle base class and cars, trucks, boats, and bicycles subclasses.
#Inheritance hierarchy example.  An administrator in the subclass is a faculty in the subclass is an employee in the subclass is a community member in the base class for which all are objects.  Another example shape is a base class separated to two dimensions hape and three dimensional shape subclasses which has circle, square, and triangle subclasses in two dimension shape and sphere, cube, and tetrahedron subclasses in the three dimension shape.
#Use inheritance to create new classes from existing classes.  Python assumes the class inherits directly from class object when you don't explicitly specify the base class.  The class hierarchy begins with class object.  The parentheses after a class name indicate inheritance and may contains a single class for single inheritance or a comma-separated list of base classes for multiple inheritance.  Multiple inheritance is beyond the scope of the book.
#The subclass starts essentially the same as the base class in single inheritance.
#Inheritance hierarchy class example.  Commission employee is base class.  Salaried commission employee is a subclass which inherits from base class Commission employee.
from decimal import Decimal
class CommissionEmployee:
    def __init__(self, firstname, lastname, ssn, grosssales, commissionrate):
        self.firstname = firstname
        self.lastname = lastname
        self.ssn = ssn
        self.grosssales = grosssales
        self.commissionrate = commissionrate
    def firstname(self):
        return self.firstname
    def lastname(self):
        return self.astname
    def ssn(self):
        return self.ssn
    def grosssales(self):
        return self.grosssales
    def grosssales(self, sales):
        if sales < Decimal("0.00"):
            raise ValueEreror("Gross sales must:  be >= to 0")
        self.grosssales = sales
    def commissionrate(self):
        return self._commissionrate
    def commissionrate(self, rate):
        if not (Decimal("0.0") < rate < Decimal("1.0")):
            raise ValueEreror("Interest rate must be greater than 0 and less than 1")
        self.commissionrate = rate
    def earnings(self):
        return self.grosssales * self.commissionrate
    def __repr__(self):
        return ("CommissionEmployee: " + f'{self.firstname} {self.lastname}\n' + f'social security number: {self.ssn}\n' + f'gross sales: {self.grosssales:.2f}\n' + f'commission rate: {self.commissionrate:.2f}')


cobject = CommissionEmployee("Sue", "Jones", "333-33-3333", Decimal("10000.00"), Decimal("0.06"))
print(cobject)
'''
CommissionEmployee: Sue Jones
social security number: 333-33-3333
gross sales: 10000.00
commission rate: 0.06
'''
print(cobject.__repr__())
'''
CommissionEmployee: Sue Jones
social security number: 333-33-3333
gross sales: 10000.00
commission rate: 0.06
'''
print(cobject.firstname) #print Sue
print(cobject.earnings()) #print 600.0000
cobject.grosssales = Decimal("20000.00")
cobject.commissionrate = Decimal("0.1")
print(cobject.earnings()) #print 2000.000
#Declare the subclass SalariedCommissionEmployee which inherits most of its capabilities from base class CommissionEmployee.  A SalariedCommissionEmployee is a CommissionEmployee.  Inheritance passes the capabilities from class CommissionEmployee to SalariedCommissionEmployee.
#SalariedCommissionEmployee inherits from CommissionEmployee class SalariedCommissionEmployee(CommissionEmployee).  SalariedCommissionEmployee __init__ method calls CommissionEmployee __init__ method to initialize the base class portion of SalariedCommissionEmployee which are the five inherited data attributes from CommissionEmployee.  super().__init__ uses the built-in function super to locate and call the base class's __init__ method passing the five arguments which initialize the inherited data attributes.  SalariedCommissionEmployee earnings method overrides CommissionEmployee earnings method to calculate the earnings of SalariedCommissionEmployee.  SalariedCommissionEmployee obtains the earnings based on commission alone by calling CommissionEmployee earnings method with super().earnings().  SalariedCommissionEmployee earnings method adds the basesalary to calculate the total earnings.  We avoid duplicate codes by having SalariedCommissionEmployee earnings method invoke CommissionEmployee earnings method to calculate SalariedCommissionEmployee total earnings.
#SalariedCommissionEmployee __repr__ method overrides CommissionEmployee method to return the CommissionEmployee "CommissionEmployee: " + f'{self.firstname} {self.lastname}\n' + f'social security number: {self.ssn}\n' + f'gross sales: {self.grosssales:.2f}\n' + f'commission rate: {self.commissionrate:.2f}' using super().__repr__() and SalariedCommissionEmployee base salary.
class SalariedCommissionEmployee(CommissionEmployee):
    def __init__(self, firstname, lastname, ssn, grosssales, commissionrate, basesalary):
        super().__init__(firstname, lastname, ssn, grosssales, commissionrate) #initialize SalariedCommissionEmployee attributes
        self.basesalary = basesalary
    def basesalary(self):
        return self.basesalary
    def basesalary(self, salary):
        if salary < Decimal("0.00"):
            raise ValueEreror("Base salary must be >= to 0")
        self.basesalary = salary
    def earnings(self):
        return super().earnings() + self.basesalary
    def __repr__(self):
        return ('Salaried' + super().__repr__() + f'\nbase salary: {self.basesalary:.2f}')


screateobject = SalariedCommissionEmployee("Bob", "Lewis", "444-44-4444", Decimal("5000.00"), Decimal("0.04"), Decimal("300.00"))
print(screateobject)
'''
SalariedCommissionEmployee: Bob Lewis
social security number: 444-44-4444
gross sales: 5000.00
commission rate: 0.04
base salary: 300.00
'''
#RM:  from CommissionEmployee: Bob Lewis to commission rate: 0.04 comes from the base class CommissionEmployee
print(screateobject.firstname) #print Bob
print(screateobject.earnings()) #print 500.00.  (5,000*0.04)+300=500
screateobject.grosssales = Decimal("10000.00")
screateobject.commissionrate = Decimal("0.05")
screateobject.basesalary = Decimal("1000.00")
print(screateobject)
'''
SalariedCommissionEmployee: Bob Lewis
social security number: 444-44-4444
gross sales: 10000.00
commission rate: 0.05
base salary: 1000.00
'''
print(screateobject.earnings()) #print 1500.00.  (10,000*0.05)+1000=1500
#check subclass check class
print(issubclass(SalariedCommissionEmployee, CommissionEmployee)) #print True
#check instance base class instance
print(isinstance(screateobject, CommissionEmployee)) #print True
employeeslist = [cobject, screateobject]
for eachemployeeslist in employeeslist:
    print(eachemployeeslist)
    print(eachemployeeslist.earnings())
    '''
    CommissionEmployee: Sue Jones
    social security number: 333-33-3333
    gross sales: 20000.00
    commission rate: 0.10
    2000.000
    SalariedCommissionEmployee: Bob Lewis
    social security number: 444-44-4444
    gross sales: 10000.00
    commission rate: 0.05
    base salary: 1000.00
    1500.0000
    '''
#Duck Typing:  A programming style which does not look at an object’s type to determine if it has the right interface; instead, the method or attribute is simply called or used ("If it looks like a duck and quacks like a duck, it must be a duck.").
class WellPaidDuck():
    def __repr__(self):
        return "I'm a well-paid duck"
    def earnings(self):
        return Decimal("1_000_000.00")


dcreateobject = WellPaidDuck()
employeeslist = [cobject, screateobject, dcreateobject]
for eachemployeeslist in employeeslist:
    print(eachemployeeslist)
    print(eachemployeeslist.earnings())
    '''
    CommissionEmployee: Sue Jones
    social security number: 333-33-3333
    gross sales: 20000.00
    commission rate: 0.10
    2000.000
    SalariedCommissionEmployee: Bob Lewis
    social security number: 444-44-4444
    gross sales: 10000.00
    commission rate: 0.05
    base salary: 1000.00
    1500.0000
    I'm a well-paid duck
    1000000.00
    '''
#RM:  skipped operator overload operator overloading