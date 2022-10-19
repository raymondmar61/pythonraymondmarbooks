import random
feetinmile = 5280
metersinkilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"]
def getfileextension(filename):
    return filename[filename.index(".") + 1:]
def rolldice(number):
    return random.randint(1, number)
