#Hello World!  Third Edition by Warren Sande Chapter 26 Making Network Connections With Sockets
hellostring = "Hello"
print(hellostring) #print Hello
print(type(hellostring)) #print <class 'str'>
print(list(hellostring)) #print ['H', 'e', 'l', 'l', 'o']
hellostringinbytes = hellostring.encode("UTF-8")
print(hellostringinbytes) #print b'Hello' #The b tells Python the string is raw bytes and not normal text
print(type(hellostringinbytes)) #print <class 'bytes'>
print(list(hellostringinbytes)) #print [72, 101, 108, 108, 111]
bytesdigits = bytes([112, 105, 122, 122, 97])
print(bytesdigits) #print b'pizza'
print(type(bytesdigits)) #print <class 'str'>
print(list(bytesdigits)) #print [112, 105, 122, 122, 97]
print(bytesdigits.decode("UTF-8")) #print pizza
bytesstring = b"pepperoni pizza 50"
print(bytesstring) #print b'pepperoni pizza 50'
print(type(bytesstring)) #print <class 'bytes'>
print(list(bytesstring)) #print [112, 101, 112, 112, 101, 114, 111, 110, 105, 32, 112, 105, 122, 122, 97, 32, 53, 48]
print(bytesstring.decode("UTF-8")) #print pepperoni pizza 50