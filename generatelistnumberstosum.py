from random import randint
def generaterandomnumberstosum(totalrandomnumbers, totalsumlist, lowerbound, upperbound):
    sumlist = []
    randominteger = randint(lowerbound, upperbound)
    while True:
        if sum(sumlist) == totalsumlist and len(sumlist) == totalrandomnumbers:
            return sorted(sumlist, reverse=True)
        elif sum(sumlist) + randominteger > totalsumlist or sum(sumlist) + randominteger < -(totalsumlist / 2) or len(sumlist) > totalrandomnumbers:
            sumlist = []
            randominteger = randint(lowerbound, upperbound)
        elif sum(sumlist) + randominteger <= totalsumlist:
            sumlist.append(randominteger)
            randominteger = randint(lowerbound + abs(randominteger), upperbound - abs(randominteger))


print(generaterandomnumberstosum(12, 90, -40, 40)) #print [36, 29, 19, 18, 15, 11, 9, 4, 1, -2, -12, -38]

totalrandomnumbers = 12
randominteger = randint(-40, 40)
totalsumlist = 90
counter = 1
sumlist = [40]
print(randominteger) #print -23
if sum(sumlist) + randominteger > totalsumlist:
    print("repeat")
elif sum(sumlist) + randominteger < totalsumlist:
    sumlist.append(randominteger)
    counter += 1
    if sum(sumlist) == totalsumlist and counter == totalrandomnumbers:
        print("break")
print(counter) #print 2
print(sumlist) #print [40,-23]
print(sum(sumlist)) #print 17

# totalrandomnumbers = 12
# totalsumlist = 90
# counter = 1
# sumlist = []
# lowerbound = -40
# upperbound = 40
# randominteger = randint(lowerbound, upperbound)
# while True:
#     print(randominteger) #print 6
#     print(len(sumlist)) #print 12
#     print(sum(sumlist)) #print 90
#     if sum(sumlist) == totalsumlist and len(sumlist) == totalrandomnumbers:
#         sumlist = sorted(sumlist, reverse=True)
#         print("break")
#         break
#     elif sum(sumlist) + randominteger > totalsumlist or sum(sumlist) + randominteger < 0 or len(sumlist) > totalrandomnumbers:
#         sumlist = []
#         randominteger = randint(lowerbound, upperbound)
#         print("continue")
#     elif sum(sumlist) + randominteger <= totalsumlist:
#         print(randominteger, "add to sumlist")
#         sumlist.append(randominteger)
#         randominteger = randint(lowerbound + abs(randominteger), upperbound - abs(randominteger))
#     counter += 1
#     print("\n")

# print("end")
# print(counter) #print 145
# print(sumlist) #print [32, 24, 21, 20, 13, 9, 5, -3, -3, -5, -7, -16]
# print(sum(sumlist)) #print 90
# listn = [1, 2, 3]
# number = 5
# print(sum(listn) + number) #print 11
# listn.append(number)
# print(listn) #print [1, 2, 3, 5]
