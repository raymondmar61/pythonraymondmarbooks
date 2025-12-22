name = "Raymond"
age = 34
height = 70
print("Use plus signs for string variables " + name + ".  Need a space inside the quotes for spaces " + str(age) + "str() function for numbers " + str(height) + " Lots of plus signs.") #print Use plus signs for string variables Raymond.  Need a space inside the quotes for spaces 34str() function for numbers 70 Lots of plus signs.
print("Use curly brackets contained inside quotes to reference variables.  name {} age {}.  End the sentence after the last quote with .format() or dot format().  The variables are inside the parenthesis in order from left to right for the curly brackets. Here's the height {}".format(name, age, height)) #print Use curly brackets contained inside quotes to reference variables.  name Raymond age 34.  End the sentence after the last quote with .format() or dot format().  The variables are inside the parenthesis in order from left to right for the curly brackets. Here's the height 70
print("Change positional argument variables.  Start count 0.  Print age first, height second, and name third.  Age {1}, height {2}, and name {0}.".format(name, age, height)) #print Change positional argument variables.  Start count 0.  Print age first, height second, and name third.  Age 34, height 70, and name Raymond.
print("The format specifiers also work for .format. Left align {:>}".format(name)) #print The format specifiers also work for .format. Left align Raymond
print("The letter d in {{:d'}} is an integer variable.  Age {:d}.".format(age)) #print The letter d in {:d'} is an integer variable.  Age 34.
print("The letter f in {{:f'}} is a floating point variable.  Age {:f}.".format(age)) #print The letter f in {:f'} is a floating point variable.  Age 34.000000.
print("Give me a negative number for negative numbers use the negative sign -. I must multiply height by -1 for a negative number.  {:-d}".format(height * -1))
#Align left which is default
casenumbers = [5, 16, 294]
for eachcasenumbers in casenumbers:
    print("Number of cases align left which is default:  {:<}".format(eachcasenumbers))
    '''
    Number of cases align left which is default:  5
    Number of cases align left which is default:  16
    Number of cases align left which is default:  294
    '''
#Align right with five total spaces
for eachcasenumbers in casenumbers:
    print("Number of cases align right which needs a number of total spaces:{:>5}".format(eachcasenumbers))
    '''
    Number of cases align right which needs a number of total spaces:    5
    Number of cases align right which needs a number of total spaces:   16
    Number of cases align right which needs a number of total spaces:  294
    '''

'''
Format specifiers {value:flags} format a value based on what flags are inserted.  The value can be a variable.  The flags are the format specifiers.

value.(number)f rounds to a decimal place or rounds a fixed point
value:(number) allocates a number many spaces
value:03 allocates a number many spaces which is three and use zeros as padding
value:< left justify
value:> right justify
value:^ center align
value:+ indicate positive value for positive numbers.  Print the positive sign.
value:- indicate negative value for negative numbers.  Print the negative sign.
value:= place sign to the leftmost position
value: insert a space before positive numbers
value:, comma separator for thousands numbers.  Underscore is the only other valid separator.
'''
stringvalue = "A string is the value F string"
print(f"Center align inside the curly brackets{stringvalue:^}.  The value is not a variable.") #print Center align inside the curly bracketsA string is the value F string.  The value is not a variable.
stringvalue = "A string is the value F string"
print(f"Center align inside the curly brackets{stringvalue:^}.  The value is not a variable.") #print Center align inside the curly bracketsA string is the value F string.  The value is not a variable.
print(f"{len(stringvalue)}") #print 30
print(f"Left align using underscores numbered {40-len(stringvalue)} spaces {stringvalue:_<40}") #print Left align using underscores numbered 10 spaces A string is the value F string__________
print(f"Right align using underscores numbered {40-len(stringvalue)} spaces {stringvalue:_>40}") #print Right align using underscores numbered 10 spaces __________A string is the value F string
variablefornumberofspaces = 40
print(f"Left align using underscores numbered {40-len(stringvalue)} spaces variable with curly braces {stringvalue:_<{variablefornumberofspaces}}") #print Left align using underscores numbered 10 spaces variable with curly braces A string is the value F string__________
price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 3498.8999
print(f"Begin the string using format specifiers with the letter f.  Price 1 is {price1:.2f}.  .2f is round to a decimal point two places as a float f.") #print Begin the string using format specifiers with the letter f.  Price 1 is 3.14.  .2f is round to a decimal point two places as a float f.
print(f"Begin the string using format specifiers with the letter f.  Price 2 is ${price2:.2f}") #print Begin the string using format specifiers with the letter f.  Price 2 is $-987.65
print(f"Begin the string using format specifiers with the letter f.  Price 3 is {price3:.1f}") #print Begin the string using format specifiers with the letter f.  Price 3 is 12.3
print(f"Ten spaces for the format specifier price3.  Price 3 is {price3:10}") #print Ten spaces for the format specifier price3.  Price 3 is 12.34
print(f"Ten spaces for the format specifier price3.  The number zero before 10 is zero padding to fill for a total of ten spaces.  Price 3 is {price3:010}") #print Ten spaces for the format specifier price3.  The number zero before 10 is zero padding to fill for a total of ten spaces.  Price 3 is 0000012.34
print(f"Ten spaces for the format specifier price3.  Less than is left justify.  Price 3 is {price3:<10}") #print Ten spaces for the format specifier price3.  Less than is left justify.  Price 3 is 12.34
print(f"Ten spaces for the format specifier price3.  The number zero before 10 is zero padding to fill for a total of ten spaces.  Less than is left justify.  Price 3 is {price3:<010}") #print Ten spaces for the format specifier price3.  The number zero before 10 is zero padding to fill for a total of ten spaces.  Less than is left justify.  Price 3 is 12.3400000
print(f"Price 3 is positive {price3:+}") #print Price 3 is positive + 12.34
print(f"Price 3 is with a space_{price3: }") #print Price 3 is with a space_ 12.34
print(f"Price 4 using thousands separator and space{price4: ,}") #print Price 4 using thousands separator and space 3, 498.8999
print(f"Price 4 using thousands separator indicate positive two decimal places {price4:+,.2f}") #print Price 4 using thousands separator indicate positive two decimal places + 3, 498.90
print(f"Can type an expression inside the curly braces for a f string {1+1}=1+1.") #print Can type an expression inside the curly braces for a f string 2=1+1.
print(f"{1+1=}") #print 1+1=2
print(f"{1+1 = }") #print 1+1 = 2
quickdebugging = 100
print(quickdebugging) #print 100
print("quickdebugging=" + str(quickdebugging)) #print quickdebugging=100
print(f"{quickdebugging}") #print 100
print(f"{quickdebugging=} is faster than typing 'quickdebugging=+str(quickdebugging)'.") #quickdebugging=100 is faster than typing 'quickdebugging=+str(quickdebugging)''.
print(isinstance(quickdebugging, int)) #print True
print(f"{isinstance(quickdebugging,int)=}") #print isinstance(quickdebugging,int)=True
decimaltopercent = .5678
print(f"Two decimal places {decimaltopercent:.2f}")
print(f"Convert decimal to percent two decimal places {decimaltopercent:.2%}")
print(f"Convert decimal to percent one decimal places {decimaltopercent:.1%}")
underscoresvisualguidecommas = 1_000_000_000
print(f"One billion {underscoresvisualguidecommas}") #print One billion 1000000000
print(f"One billion underscore separator {underscoresvisualguidecommas:_}") #print One billion 1000000000
print(f"One billion comma separator {underscoresvisualguidecommas:,}") #print One billion 1000000000

#Use f strings for date and for time
from datetime import datetime
asofnow = datetime.now()
print(asofnow) #print 2025-12-22 14:14:03.316495
print(f"F strings for dates F strings for time {asofnow:%x}") #print F strings for dates F strings for time 12/22/25
print(f"F strings for dates F strings for time {asofnow:%c}") #print F strings for dates F strings for time Mon Dec 22 14:14:03 2025
print(f"F strings for dates F strings for time {asofnow:%H:%M:%S}") #print F strings for dates F strings for time 14:14:03

#Use a dictionary for .format
jobsdictionary = {"name": "Mekael", "job": "Carpender"}
print("{name} is a {job}.  Double asterisks unpacks the dictionary.".format(**jobsdictionary)) #print Mekael is a Carpender.  Double asterisks unpacks the dictionary.
print("{job} is a {name}.  Double asterisks unpacks the dictionary.".format(**jobsdictionary)) #print Carpender is a Mekael.  Double asterisks unpacks the dictionary.
#Use a list for .format
scoreslist = [78, 96, 83, 86]
print("The second entry score is {[1]}.".format(scoreslist)) #print The second entry score is 96.
print("The second entry score is {s[1]}.".format(s=scoreslist)) #print The second entry score is 96.
print("Scientific notation use {{:e}}.  Number is 874.577 8.745770X10^2.  {:e}".format(874.577)) #print Scientific notation use {:e}.  Number is 874.577 8.745770X10^2.  8.745770e+02
print("Scientific notation use {{:E}}.  Number is 602214090000000000000000 6.02214X10^23.  {:E}.  Move the decimal point 23 places to the right.".format(602214090000000000000000)) #print Scientific notation use {:E}.  Number is 602214090000000000000000 6.02214X10^23.  6.022141E+23.  Move the decimal point 23 places to the right.
print("Use format function for binary number.  {:b}".format(79)) #print Use format function for binary number.  1001111
print("Use format function for hexadecimal number.  {:x}".format(183)) #print Use format function for hexadecimal number.  b7
print("Use format function for hexadecimal number.  {:X}".format(183)) #print Use format function for hexadecimal number.  B7

#Custom F Strings
class Customfstrings:
    def __init__(self, texttomodify: str) -> None: #texttomodify input as string and return nothing
        self.texttomodify = texttomodify
    def __format__(self, formatspecifier: str) -> str: #formatspecifier input as string and return as string.  The formatspecifier is value user inputs after the f string colon.
        match formatspecifier:
            case "convertalluppercase":
                return self.texttomodify.upper()
            case "convertalllowercase":
                return self.texttomodify.lower()
            case "countstring":
                return str(len(self.texttomodify))
            case "swawpcases":
                return self.texttomodify.swapcase()
            # can't work because must return a string
            # case "stringtolist":
            #     return list(self.texttomodify.split(" "))
            # case _:
                raise ValueError(f"Don't recognize the custom F string format specifier {formatspecifier}.  Format specifier not created in class Customfstrings")


mytext = Customfstrings("The Quick Brown Fox Jumps Over The Lazy Dog")
print(f"{mytext:convertalluppercase}") #print THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
print(f"{mytext:convertalllowercase}") #print the quick brown fox jumps over the lazy dog
print(f"{mytext:countstring}") #print 43
print(f"{mytext:swawpcases}") #print tHE qUICK bROWN fOX jUMPS oVER tHE lAZY dOG
#print(f"{mytext:intentionalerror}") #print ValueError: Don't recognize the custom F string format specifier intentionalerror.  Format specifier not created in class Customfstrings