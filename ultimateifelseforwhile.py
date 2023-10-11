#If, elseif which is elif, else
flowcontrol = "elif is elseif in Python"
if flowcontrol == "use double equal signs for comparison":
    print("Remember colon at the end of the if statement")
elif flowcontrol == "elif is elseif in Python":
    print("Type elif for else if") #print Type elif for else if
elif flowcontrol == "type if statements by logic":
    print("If statements stop at the first true.")
else:
    print("All ifs and elfis are false the else statement is printed.")
apples = 20
if apples > 3:
    print("First if statement independent greater than three apples at 3.") #print First if statement independent greater than three apples at 3.
if apples > 5:
    print("Second if statement independent greater than three apples at 5.") #print Second if statement independent greater than three apples at 5.
if apples > 50:
    print("Third if statement independent greater than fifty applies at 50.")
else:
    print("Third if statement independent greater than fifty applies at 50 with an else less than or equal to fifty applies.") #print Third if statement independent greater than fifty applies at 50 with an else less than or equal to fifty applies.
if 10 <= apples <= 20:
    print("If statement between if statement greater than equal less than equal") #print If statement between if statement greater than equal less than equal
truevariable = True
if truevariable:
    print("The truevariable is True.  Print the sentence.")
truesentence = "Anything between the quotes"
if truesentence:
    print("The truesentence is True.  Print the sentence.")
#yytest.py:30: SyntaxWarning: "is" with a literal. Did you mean "=="? if location is "home" or location is "Vegas":
# location = "home"
# if location is "home" or location is "Vegas":
#     print(f"If statment with ors and iss {location}.") #print If statment with ors and iss home.
#     print("If statment with ors and iss {}.".format(location)) #print If statment with ors and iss home.
integernumber = 90
checkdatatypefunciton = isinstance(integernumber, int)
print(checkdatatypefunciton)
if checkdatatypefunciton:
    print(integernumber, "is an integer int by checking data type") #print 90 is an integer int by checking data type
else:
    print(integernumber, "is not an integer int by checking data type")
if type(integernumber) == int:
    print("isinstance function better than type(integernumber) == int") #print isinstance function better than type(integernumber) == int
