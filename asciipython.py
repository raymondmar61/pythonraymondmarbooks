#asciipython.py
#Python ascii() function
#ASCII (American Standard Code for Information Interchange) is a 7-bit character encoding standard that represents 128 characters, including English letters, digits, punctuation marks, and control characters.
#ASCII defines exactly 128 characters (0-127).  Control characters (0-31) non-printable characters like newline, tab, carriage return.  Printable characters (32-126) space, letters, digits, punctuation.  DEL (127) delete character.

#Common ASCII Values.  Digits 0-9: 48-57.  Uppercase letters A-Z: 65-90.  Lowercase letters a-z: 97-122.  Space: 32.  Newline: 10.  Tab: 9.
#ord() function ordinal gets the ASCII value.  Input must be a string value.
print(ord("0")) #print 48
print(ord("9")) #print 57
print(ord("A")) #print 65
print(ord("B")) #print 66
print(ord("Y")) #print 89
print(ord("Z")) #print 90
print(ord("a")) #print 97
print(ord("b")) #print 98
print(ord("y")) #print 121
print(ord("z")) #print 122
print(ord(" ")) #print 32.  Space
print(ord("\n")) #print 10.  New line.
print(ord("\t")) #print 9.  Tab.
#chr() function gets character from ASCII value.
print(chr(48)) #print 0
print(chr(57)) #print 9
print(chr(65)) #print A
print(chr(66)) #print B
print(chr(89)) #print Y
print(chr(90)) #print Z
print(chr(97)) #print a
print(chr(98)) #print b
print(chr(121)) #print y
print(chr(122)) #print z
print(chr(32) + "<-- is a space") #print  <--is a space
print(f"{chr(32)}<-- is a space") #print  <--is a space
#The ascii() function returns a readable version for strings, tuples, lists, and any object.  It returns a printable representation of an object using only ASCII characters.  Non-ascii characters are replaced with escape characters; any non-ASCII characters present are automatically escaped using Unicode escape sequences such as \x, \u, or \U.
numbertoascii = 1
print(ascii(numbertoascii)) #print 1
print(type(ascii(numbertoascii))) #print <class 'str'>
converttoascii = "The quick brown fox jumps over the lazy dog."
print(ascii(converttoascii)) #print 'The quick brown fox jumps over the lazy dog.'
#Method check string is all ASCII
print(converttoascii.isascii()) #print True
nonasciicharacteryensymbol = "¥"
print(ascii(nonasciicharacteryensymbol)) #print '\xa5'
asciiandnonascii = "G ë ê k s f ? r G ? e k s"
print(ascii(asciiandnonascii)) #print 'G \xeb \xea k s f ? r G ? e k s'.  Non-ASCII characters are replaced with their Unicode escape sequences.
print(ascii("marquée")) #print 'marqu\xe9e'
print(ascii("résumé")) #print 'r\xe9sum\xe9'
print(ascii("jalapeño")) #print 'jalape\xf1o'
newlinecharacter = '''New line character
is replaced with
the \n character.
The \n is an unicode escape.'''
print(ascii(newlinecharacter)) #print 'New line character\nis replaced with\nthe \n character.\nThe \n is an unicode escape.'
nonasciiinaset = {"Š", "E", "T"}
print(ascii(nonasciiinaset)) #print {'\u0160', 'E', 'T'}
nonasciilist = ["L", "i", "s", "t", "Ň", "ĕ", "Ŵ"]
print(ascii(nonasciilist)) #print ['L', 'i', 's', 't', '\u0147', '\u0115', '\u0174']
nonasciituple = ("T", "u", "p", "l", "ĕ")
print(ascii(nonasciituple)) #print ('T', 'u', 'p', 'l', '\u0115')
print(type(ascii(nonasciituple))) #print <class 'str'>

#ASCII is the first 128 code points of Unicode from U+0000 to U+007F. Every ASCII character has the same numeric value in Unicode.  UTF-8 encodes ASCII characters as single bytes.  ASCII files are valid UTF-8 files.
converttoascii = "The quick brown fox jumps over the lazy dog."
print(ascii(converttoascii)) #print 'The quick brown fox jumps over the lazy dog.'
#Encode to ASCII bytes.  ASCII and UTF-8 produce identical bytes for ASCII characters.
print(converttoascii.encode("ascii")) #print b'The quick brown fox jumps over the lazy dog.'
print(converttoascii.encode("utf-8")) #print b'The quick brown fox jumps over the lazy dog.'
#Try except to handle encoding errors with non-ascii characters
try:
    "café".encode("ascii")
except UnicodeEncodeError:
    print("Can't encode non-ASCII characters") #print Can't encode non-ASCII characters
#encode method with errors= option
print("café".encode("ascii", errors="ignore")) #print b'caf'
print("café".encode("ascii", errors="replace")) #print b'caf?'
print("café".encode("ascii", errors="xmlcharrefreplace")) #print b'caf&#233;'