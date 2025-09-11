#Encoding and Decoding Base64 Strings in Python.pdf
#Binary data contains bytes which represent non-text information such as images.  Baes64 encoding converts bytes containing binary data or text data to ASCII characters.
#There are 64 characters which represent numbers.  The Base64 character set contains 26 uppercase letters, 26 lowecase letters, 10 numbers, + plus sign, and / foward slash for new lines.  26+26+10+2=64.  Each Base64 character represents 6 bits of information.
#Encode Base64 text data or Base64 encoding by coverting text data.  1 Take the ASCII value of each character.  2 Calculate the 8-bit binary equivalent of the ASCII values.  3 Convert the 8-bit chunks into 6 bits chunks by re-grouping the digits.  4 Convert the 6-bit binary groups to their respective decimal values.  5 Assign the respective base64 character for each decimal value from the base64 encoding table.
#Convert Python to a Base64 string.  1 The ASCII values of P, y, t, h, o, n are 15, 50, 45, 33, 40, 39.  2 The 8-bit binary are 01010000 01111001 01110100 01101000 01101111 01101110.  3 Convert the 8-bit binary to 6 bits are 010100 000111 100101 110100 011010 000110 111101 101110. . . Note The sequence is padded if we can't group the data into 6-bits sequences.  4 Obtain the decimal value for each 6-bits group for which the last 6 bits is 20 7 37 52 26 6 61 46.  5 Convert the decimals to Base64 characters using the Base64 converstion table.  The Base64 encoded for Python is UHl0aG9u.
#Base64 Encoding.  All data in computers are transmitted as 1s and 0s or ones and zeros.  However, some computers can't understand all the bits received because the meaning of the 1s and 0s sequence is dependent on the type of data it represents.  A 10110001 must be processed differently if it represents a number or an image.  Base64 is a popular method to get binary data into ASCII characters.  ASCII characters are understood by many networks and applications.
import base64
#Encode strings
message = "Python is fun"
messagebytes = message.encode("ascii") #Convert to bytes
print(messagebytes) #print b'Python is fun'
base64bytes = base64.b64encode(messagebytes) #Encode to Base64
print(base64bytes) #print b'UHl0aG9uIGlzIGZ1bg=='
base64message = base64bytes.decode("ascii") #String representation of the Base64 conversion.  Decode as ASCII.
print(base64message) #print UHl0aG9uIGlzIGZ1bg==
print("\n")
#Decode strings
base64bytes = base64message.encode("ascii") #Encode message to bytes
print(base64bytes) #print b'UHl0aG9uIGlzIGZ1bg=='
messagebytes = base64.b64decode(base64bytes) #Decode
print(messagebytes) #print b'Python is fun'
message = messagebytes.decode("ascii") #Decode to a string
print(message) #print Python is fun

#Encoding and Decoding Base64 Strings in Python - GeeksforGeeks.pdf
#Base64 encoding converts bytes with binary data or text data to ASCII characters.  Base64 encoding is a converstion from bytes to ASCII characters.  Each Base64 character represents 6 bits of data.  Don't use for encryption.
#Covert a string to Base 64 character:  get the ASCII value for each character, compute the 8-bit binary equivalent of the ASCII value, convert the 8-bit characters chunk into 6 bits chunks by regrouping the digits, convert the 6-bit binary groups to their respective decimal values, and use the Base64 encoding table to align the respective Base64 value for each decimal value; for example, letter I is 001000 and letter r is 101011.
#Encoding prevents the data from getting corrupted when transferred or processed through a text-only system.
#Decode is the opposite of encode.  Conver the Base64 strings into unencoded data bytes.  Convert bytes to a string.
#The base64 module encode data and decode data.
import base64
#Encode strings
samplestring = "GeeksforGeeks is the best"
samplestringbytes = samplestring.encode("ascii") #compute the 8-bit binary equivalent of the ASCII value
print(samplestringbytes) #print b'GeeksforGeeks is the best'
base64bytes = base64.b64encode(samplestringbytes) #compute the 8-bit binary equivalent of the ASCII value, convert the 8-bit characters chunk into 6 bits chunks by regrouping the digits, convert the 6-bit binary groups to their respective decimal values, and use the Base64 encoding table to align the respective Base64 value for each decimal value
print(base64bytes) #print b'R2Vla3Nmb3JHZWVrcyBpcyB0aGUgYmVzdA=='
base64string = base64bytes.decode("ascii")
print(base64string) #print R2Vla3Nmb3JHZWVrcyBpcyB0aGUgYmVzdA==
print("\n")
#Decode strings
base64bytes = base64string.encode("ascii")
print(base64bytes) #print b'R2Vla3Nmb3JHZWVrcyBpcyB0aGUgYmVzdA=='
samplestringbytes = base64.b64decode(base64bytes)
print(samplestringbytes) #print b'GeeksforGeeks is the best'
samplestring = samplestringbytes.decode("ascii")
print(samplestring) #print GeeksforGeeks is the best

#Base64-Encoding-Decoding-Using-Python-09-02-2025_12_30_PM.pdf
#The base64 library encodes binary data and decodes binary data from base64 strings.  Converts binary data to plain text.  Base64 converts binary data to string of printable ASCII characters.  Binary data can be transmitted via email and HTTP which handles ASCII characters.
#Type import base64 to use the base64 module.
'''
b64encode() function encodes a bytes-like object to ASCII bytes.  Returns the encoded data as a bytes object.
b64decode() function decodes an ASCII-like object to bytes.  Returns the encoded data as a unicode string.
'''
#The two functions supports Base16, Base32, Base64, ASCII85, and Base85.  Base64 encoding for which each group of three bytes is stored as a group of four characters.  26 uppercase letters, 26 lowercase letters, 10 numbers, and + plus sign and / forward slash for new lines.  The data stream is padded with an = equal sign at the end.
#Six bits of data are represensted by each Base64 character.  To convert a string into a Base64 character:  get the ASCII value for each character, compute the 8-bit binary equivalent of the ASCII value, reorganize the digits and divide the 8-bit character chunk into 6 bit pieces, convert the 6-bit binary groups to their respective decimal value, and align the correspoding Base64 values for each decimal value using the Base64 encoding table.  For example, letter A is 000000, letter k is 100100, and number 2 is 110110.
import base64
data = "Python is a programming language"
databytes = data.encode("ascii")
print(databytes) #print b'Python is a programming language'
base64bytes = base64.b64encode(databytes)
print(base64bytes) #print b'UHl0aG9uIGlzIGEgcHJvZ3JhbW1pbmcgbGFuZ3VhZ2U='
base64string = base64bytes.decode("ascii")
print(base64string) #print UHl0aG9uIGlzIGEgcHJvZ3JhbW1pbmcgbGFuZ3VhZ2U=
#base64.encodestring() method allows us to directly encode the string.  encodestring must be imported
# from base64 import encodestring
# stringtobeencoded = "Python is a programming language"
# encodestring = base64.encodestring(stringtobeencoded)
# print(encodestring) #return ImportError: cannot import name 'encodestring' from 'base64' (/usr/lib/python3.10/base64.py)
