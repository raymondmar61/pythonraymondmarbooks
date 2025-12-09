#bin() function returns the binary representation of an integer.  Converts an integer to a binary string which begins with 0b.  0b indicates a binary value.
#Python uses bitwise operations behind the scenes to achieve this conversion quickly. It divides the input number by two indefinitely, capturing the remainder until the quotient equals zero. To create the binary representation, the remainders are inverted.
binaryinteger = bin(36)
print(binaryinteger) #print 0b100100
print(type(binaryinteger)) #print <class 'str'>
twolengthbinaryinteger = bin(3)
print(twolengthbinaryinteger) #print 0b11
fourlengthbinaryinteger = bin(-10)
print(fourlengthbinaryinteger) #print -0b1010
remove0b = format(36, "b") #format() function formats the input following the Format Specification mini language
print(remove0b) #print 100100
remove0b = format(3, "b") #format() function formats the input following the Format Specification mini language
print(remove0b) #print 11
remove0b = format(-10, "b") #format() function formats the input following the Format Specification mini language
print(remove0b) #print -1010
remove0b = f"{36:b}"
print(remove0b) #print 100100
remove0b = f"{3:b}"
print(remove0b) #print 11
remove0b = f"{-10:b}"
print(remove0b) #print -1010
remove0b = bin(36)[2:]
print(remove0b) #print 100100
remove0b = bin(3)[2:]
print(remove0b) #print 11
remove0b = bin(-10)[3:]
remove0b = bin(36).lstrip("0b")
print(remove0b) #print 100100
remove0b = bin(3).lstrip("0b")
print(remove0b) #print 11
remove0b = "-" + bin(-10).lstrip("-0b")
print(remove0b) #print -1010
#int() function converts the binary string back to an integer using base 2 or binary
convertbinarytointeger = "100100"
print(int(convertbinarytointeger, 2)) #print 36
convertbinarytointeger = "11"
print(int(convertbinarytointeger, 2)) #print 3
convertbinarytointeger = "-1010"
print(int(convertbinarytointeger, 2)) #print -10
#Customize the output with string formatting techniques for precise widths and formatting.
print(bin(255)) #print 0b11111111
print(bin(255)[2:]) #print 11111111
print(bin(255)[2:].zfill(10)) #print 0011111111
print(bin(36)[2:].zfill(10)) #print 0000100100
print(bin(3)[2:].zfill(10)) #print 0000000011
print(bin(-10)[2:].zfill(10)) #print 00000b1010
print(bin(-10)[3:].zfill(10)) #print 0000001010
converthexadecimaltobinary = bin(0xff) #integer 255 in hexadecimal
print(converthexadecimaltobinary) #print 0b11111111
getbinarytointeger255 = int("0b11111111", 2)
print(getbinarytointeger255) #print 255
convertoctacltobinary = bin(0o24) #integer 20 in octal
print(convertoctacltobinary) #print 0b10100
convertbinarytointeger20 = int("0b10100", 2) #integer 20 in binary
print(convertbinarytointeger20) #print 20
#An object implementing the .__index__() method
class Number:
    def __init__(self, value):
        self.value = value
    def __index__(self):
        return self.value


number = Number(10)
print(number) #print <__main__.Number object at 0x7e314de63fd0>
print(bin(number)) #print 0b1010
class Id():
    def __init__(self, idnumber):
        self.idnumber = idnumber
    def __index__(self):
        return self.idnumber


binaryidnumber = bin(Id(10))
print(binaryidnumber) #print 0b1010
binaryidnumber = bin(Id(255))
print(binaryidnumber) #print 0b11111111
