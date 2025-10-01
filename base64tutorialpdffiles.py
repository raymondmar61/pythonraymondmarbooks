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

#Base64 Encoding Binary Files in Python [bEA8HI_I5bQ]
'''
1 byte is 8 bits.  1 byte is either 0s and/or 1s.  8 bits is eight numbers consist of 0s and/or 1s.  For example, 10011011 is 8 bits and is 1 byte.  10110110 01100011 00001100 is 3 times 8 bits and 3 bytes or 24 bites.  Takes the 3 times 8 bits convert to 6 bits.  101101 100110 001100 001100 is 4 times 6 bits and 4 bytes or 24 bites.  Base64 converts the binary numbers to text or transforms binary data to printable characters.  Thre are 64 unique printable characters; in other words, each 6 bits binary number or six binary numbers of 0s and 1s are converted to a character or string letter or number A-Z, a-z, 0-9, + and /.  The binary data is taken 6 bits at a time.  Each group of 6 bits is mapped to one of the 64 unique characters.  Base64 carries data stored in binary formats which allows to be data to be communicated on text content programs.  Base64 is also used for email attachments.
'''
import base64
mytext = "Hello World"
encodemytexttoascii = mytext.encode("ascii") #Convert to bytes or 8bits
print(encodemytexttoascii) #print b'Hello World'
asciitobase64 = base64.b64encode(encodemytexttoascii) #Convert from 8bits to 6bits base64
print(asciitobase64) #print b'SGVsbG8gV29ybGQ='
base64toascii = base64.b64decode(asciitobase64)
print(base64toascii) #print b'Hello World'
#Convert image convert picture to base64
with open("dilbert.jpg", "rb") as openimagereadbytes:
    data = openimagereadbytes.read()
print(data) #print b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x02X\x02X\x00\x00\xff\xfe\x00\tDilbert\xff\xed!\xe6Photoshop 3.0\x008BIM\x04%\x00\x00\x00\x00\x00\x10\xca\x8ce8\xb4\xd2K\x86\xa59\xb5\x9d\x88\xfeMs8BIM\x04:\x00\x00\x00\x00\x00\xe5\x00\x00\x00\x10\x00\x00\x00\x01\x00\x00\x00\x00\x00\x0bprintOutput\x00\x00\x00\x05\x00\x00\x00\x00PstSbool\x01\x00\x00\x00\x00Inteenum\x00\x00\x00\x00Inte\x00\x00\x00\x00Clrm\x00\x00\x00\x0fprintSixteenBitbool\x00\x00\x00\x00\x0bprinterNameTEXT\x00 . . .
imagetobase64 = base64.b64encode(data)
print(imagetobase64) #print b'/9j/4AAQSkZJRgABAQECWAJYAAD//gAJRGlsYmVydP/tIeZQaG90b3Nob3AgMy4wADhCSU0EJQAAAAAAEMqMZTi00kuGpTm1nYj+TXM4QklNBDoAAAAAAOUAAAAQAAAAAQAAAAAAC3ByaW50T3V0cHV0AAAABQAAAABQc3RTYm9vbAEAAAAASW50ZWVudW0AAAAASW50ZQAAAABDbHJtAAAAD3ByaW50U2l4dGVlbkJpdGJvb2wAAAAAC3ByaW50ZXJOYW1lVEVYVAAAAAEAAAAAAA9wcmludFByb29mU2V0dXBPYmpjAAAADABQAHIAbwBvAGYAIABTAGUAdAB1AHAAAAAAAApwcm9vZlNldHVwAAAAAQAAAABCbHRuZW51bQAAAAxidWlsdGluUHJvb2YAAAAJcHJvb2ZDTVlLADhCSU0EOwAAAAACLQAAABAAAAABAAAAAAAScHJpbnRPdXRwdXRPcHRpb25zAAAAFwAAAABDcHRuYm9vbAAAAAAAQ2xicmJvb2wAAAAAA . . .
#Convert base64 to image
imageasdata = imagetobase64 #image is base64 from the variable imagetobase64
viewimageasdata = base64.b64decode(imageasdata)
print(viewimageasdata) #print b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x02X\x02X\x00\x00\xff\xfe\x00\tDilbert\xff\xed!\xe6Photoshop 3.0\x008BIM\x04%\x00\x00\x00\x00\x00\x10\xca\x8ce8\xb4\xd2K\x86\xa59\xb5\x9d\x88\xfeMs8BIM\x04:\x00\x00\x00\x00\x00\xe5\x00\x00\x00\x10\x00\x00\x00\x01\x00\x00\x00\x00\x00\x0bprintOutput\x00\x00\x00\x05\x00\x00\x00\x00PstSbool\x01\x00\x00\x00\x00Inteenum\x00\x00\x00\x00Inte\x00\x00\x00\x00Clrm\x00\x00\x00\x0fprintSixteenBitbool\x00\x00\x00\x00\x0bprinterNameTEXT\x00 . . .
with open("viewimagefrombase64.jpg", "wb") as convertbase64topicture:
    convertbase64topicture.write(viewimageasdata)
#Copy image with new file name
with open("dilbert.jpg", "rb") as openimagereadbytes:
    data = openimagereadbytes.read()
with open("newimagename.jpg", "wb") as createimagewritebytes:
    createimagewritebytes.write(data) #take image dilbert.jpg as data = to copy same image save as newimagename.jpg
#Linux command line type eog newimagename.jpg to view image or open image.

#Python Tips and Tricks： Base64 String Encoding and Decoding [mxwvvMZaIvU]
simplestring = "ye old cheese shoppe"
encodetoascii = simplestring.encode("ascii")
print(encodetoascii) #print b'ye old cheese shoppe'.  b stands for bytes.  bytes array.
print(type(encodetoascii)) #print <class 'bytes'>
encodetoutf8 = simplestring.encode("utf-8")
print(encodetoutf8) #print b'ye old cheese shoppe'.  b stands for bytes.  bytes array.
print(type(encodetoutf8)) #print <class 'bytes'>
decodetheencodeutf8 = encodetoutf8.decode("utf-8")
print(decodetheencodeutf8) #print ye old cheese shoppe
import base64
stringsource = "Python rocks!"
encodetoutf8 = stringsource.encode("utf-8")
print(encodetoutf8) #print b'Python rocks!'
converttobase64 = base64.b64encode(encodetoutf8)
print(converttobase64) #print b'UHl0aG9uIHJvY2tzIQ=='
print(type(converttobase64)) #print <class 'bytes'>
decodebase64 = base64.b64decode(converttobase64)
print(decodebase64) #print b'Python rocks!'
print(type(decodebase64)) #print <class 'bytes'>
decodebase64toutf8 = converttobase64.decode("utf-8")
print(decodebase64toutf8) #print UHl0aG9uIHJvY2tzIQ==
print(type(decodebase64toutf8)) #print <class 'str'>
decodebase64toascii = converttobase64.decode("ascii")
print(decodebase64toascii) #print UHl0aG9uIHJvY2tzIQ==
print(type(decodebase64toascii)) #print <class 'str'>
stringsource = "Python rocks!"
encodetoutf8 = stringsource.encode("utf-8")
print(encodetoutf8) #print b'Python rocks!'
decodebase64tostring = encodetoutf8.decode("utf-8")
print(decodebase64tostring) #print Python rocks!
print(type(decodebase64tostring)) #print <class 'str'>
combineencodebase64 = base64.b64encode("Python rocks!".encode("utf-8"))
print(combineencodebase64) #print b'UHl0aG9uIHJvY2tzIQ=='
print(combineencodebase64, len(combineencodebase64), sep="\t") #print b'UHl0aG9uIHJvY2tzIQ=='   20
stringbase64missingequalsigns = "UHl0aG9uIHJvY2tzIQ" #A string needs two equal signs for base64
encodestringbase64missingequalsignsutf8 = stringbase64missingequalsigns.encode("utf-8")
print(encodestringbase64missingequalsignsutf8) #print b'UHl0aG9uIHJvY2tzIQ'
encodestringbase64missingequalsignsutf8 += b"===" #always use three equal signs because Python knows the amount of equal signs for correct padding
print(encodestringbase64missingequalsignsutf8) #print b'UHl0aG9uIHJvY2tzIQ==='
decodebase64 = base64.b64decode(encodestringbase64missingequalsignsutf8)
print(decodebase64) #print b'Python rocks!'
decodestringbase64missingequalsignsutf8 = encodestringbase64missingequalsignsutf8.decode("utf-8")
print(decodestringbase64missingequalsignsutf8) #print UHl0aG9uIHJvY2tzIQ===
decodebase64 = base64.b64decode(decodestringbase64missingequalsignsutf8)
print(decodebase64) #print b'Python rocks!'
googlewebaddress = "https://google.com"
encodegoogleutf8base64 = base64.b64encode(googlewebaddress.encode("utf-8"))
print(encodegoogleutf8base64) #print b'aHR0cHM6Ly9nb29nbGUuY29t'
decodegooglebase64utf8 = base64.b64decode(encodegoogleutf8base64.decode("utf-8"))
print(decodegooglebase64utf8) #print b'https://google.com'
convertutf8tostring = decodegooglebase64utf8.decode("utf-8")
print(convertutf8tostring) #print https://google.com
googlewebaddress = "https://google.com"
encodegoogleuasciibase64 = base64.b64encode(googlewebaddress.encode("ascii"))
print(encodegoogleuasciibase64) #print b'aHR0cHM6Ly9nb29nbGUuY29t'
decodegooglebase64uascii = base64.b64decode(encodegoogleuasciibase64.decode("ascii"))
print(decodegooglebase64uascii) #print b'https://google.com'
convertuasciitostring = decodegooglebase64uascii.decode("ascii")
print(convertuasciitostring) #print https://google.com
#Encode function
def encode(stringinput: str, encoding="utf-8") -> str:
    encoded = stringinput.encode(encoding) #convert stringinput to utf-8 if default
    encodetobase64 = base64.b64encode(encoded) #encode
    return encodetobase64.decode(encoding) #return base64 encoded as utf-8 string if default
#Decode function
def decode(stringinput: str, encoding="utf-8") -> str:
    encoded = stringinput.encode(encoding) #convert stringinput to utf-8 if default
    decodefrombase64 = base64.b64decode(encoded + b"===") #decode
    return decodefrombase64.decode(encoding) #return base64 decoded as utf-8 string if default


print(encode("https://google.com", "utf-8")) #print aHR0cHM6Ly9nb29nbGUuY29t
print(decode("aHR0cHM6Ly9nb29nbGUuY29t", "utf-8")) #print https://google.com