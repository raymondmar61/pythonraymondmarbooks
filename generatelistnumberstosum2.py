from random import randint

sumlist = []
totalcount = 6
sumgoal = 45
counter = 1
randomintegers = randint(0, sumgoal)
while True:
    if len(sumlist) <= totalcount - 1 and sum(sumlist) >= sumgoal:
        print("sumlist greater than and equal to sumgoal and len(sumlist) less than totalcount.  Need to delete")
        sumlist = []
    elif len(sumlist) == totalcount - 1 and sum(sumlist) < sumgoal:
        sumlist.append(sumgoal - sum(sumlist))
        break
    else:
        sumlist.append(randomintegers)
        randomintegers = randint(0, sumgoal - sum(sumlist))
    counter += 1

print(sumlist, sum(sumlist), counter)
'''
sumlist greater than and equal to sumgoal and len(sumlist) less than totalcount.  Need to delete
sumlist greater than and equal to sumgoal and len(sumlist) less than totalcount.  Need to delete
sumlist greater than and equal to sumgoal and len(sumlist) less than totalcount.  Need to delete
sumlist greater than and equal to sumgoal and len(sumlist) less than totalcount.  Need to delete
[0, 17, 3, 15, 0, 10] 45 28
'''

negativesumlist = []
totalcount = 6
sumgoal = -45
counter = 1
randomintegers = randint(sumgoal, 0)
while True:
    if len(negativesumlist) <= totalcount - 1 and sum(negativesumlist) <= sumgoal:
        print("negativesumlist greater than and equal to sumgoal and len(negativesumlist) less than totalcount.  Need to delete")
        negativesumlist = []
    elif len(negativesumlist) == totalcount - 1 and sum(negativesumlist) > sumgoal:
        negativesumlist.append(sumgoal - sum(negativesumlist))
        break
    else:
        negativesumlist.append(randomintegers)
        randomintegers = randint(sumgoal - sum(negativesumlist), 0)
    counter += 1

print(negativesumlist, sum(negativesumlist), counter)
'''
negativesumlist greater than and equal to sumgoal and len(negativesumlist) less than totalcount.  Need to delete
negativesumlist greater than and equal to sumgoal and len(negativesumlist) less than totalcount.  Need to delete
[0, -37, -4, -2, -1, -1] -45 15
'''

from random import randint

sumlist = []
totalcount = 12
sumgoal = 45
counter = 1
randomintegers = randint(0, sumgoal)
while True:
    if len(sumlist) >= totalcount:
        sumlist = []
        counter = 1
    elif sum(sumlist) < sumgoal:
        print("counter", counter)
        sumlist.append(randomintegers)
        randomintegers = randint(0, sumgoal - sum(sumlist))
        counter += 1
    # elif sum(sumlist) > sumgoal:
    #     print("sum(sumlist) > sumgoal")
    #     sumlist.append(sumgoal - sum(sumlist))
    #     break
    elif sum(sumlist) == sumgoal:
        print("sum(sumlist) == sumgoal")
        break

print(sumlist, sum(sumlist), counter)

negativesumlist = []
negativetotalcount = totalcount - len(sumlist)
print(negativetotalcount)
negativesumgoal = -45
counter = 1
allcounter = 1
negativerandomintegers = randint(negativesumgoal, 0)
while True:
    print(negativesumlist)
    if len(negativesumlist) > negativetotalcount:
        print("Delete.  Too many numbers negativesumlist.  Start over.")
        negativesumlist = []
        counter = 1
        negativerandomintegers = randint(negativesumgoal, 0)
    elif sum(negativesumlist) > negativesumgoal:
        print("negative counter", counter)
        negativesumlist.append(negativerandomintegers)
        negativerandomintegers = randint(negativesumgoal - sum(negativesumlist), 0)
        counter += 1
    elif len(negativesumlist) == negativetotalcount - 1 and sum(negativesumlist) > negativesumgoal:
        negativesumlist.append(negativesumgoal - sum(negativesumlist))
        break
    elif sum(negativesumlist) == negativesumgoal and len(negativesumlist) == negativetotalcount:
        print("sum(negativesumlist) == negativesumgoal and and len(negativesumlist) == negativetotalcount")
        break
    elif sum(negativesumlist) >= negativesumgoal and len(negativesumlist) < negativetotalcount:
        print("Delete.  Too few numbers negativesumlist.  Start over.")
        negativesumlist = []
        counter = 1
        negativerandomintegers = randint(negativesumgoal, 0)
    allcounter += 1

print(sumlist, sum(sumlist), counter)
print(negativesumlist, sum(negativesumlist), counter, allcounter)
'''
counter 1
counter 2
counter 3
counter 4
counter 5
counter 6
counter 7
sum(sumlist) == sumgoal
[12, 22, 3, 0, 0, 6, 2] 45 8
5
...
[]
negative counter 1
[-14]
negative counter 2
[-14, -16]
negative counter 3
[-14, -16, -1]
negative counter 4
[-14, -16, -1, -3]
negative counter 5
[-14, -16, -1, -3, -8]
negative counter 6
[-14, -16, -1, -3, -8, 0]
Delete.  Too many numbers negativesumlist.  Start over.
[]
negative counter 1
[-23]
negative counter 2
[-23, -9]
negative counter 3
[-23, -9, -9]
negative counter 4
[-23, -9, -9, -4]
Delete.  Too few numbers negativesumlist.  Start over.
[]
negative counter 1
[-44]
negative counter 2
[-44, 0]
negative counter 3
[-44, 0, 0]
negative counter 4
[-44, 0, 0, 0]
negative counter 5
[-44, 0, 0, 0, -1]
sum(negativesumlist) == negativesumgoal and and len(negativesumlist) == negativetotalcount
[12, 22, 3, 0, 0, 6, 2] 45 6
[-44, 0, 0, 0, -1] -45 6 34
'''

from random import randint

def generatezerosumintegerslist(totalcount, zerosumgoal):
    #Generate positive integers sum
    positivesumlist = []
    positiverandomintegers = randint(0, zerosumgoal)
    while True:
        #Reset positivesumlist and positiverandomintegers if the count is greater than or equal to totalcount
        if len(positivesumlist) >= totalcount:
            positivesumlist = []
            positiverandomintegers = randint(0, zerosumgoal)
        #Append positiverandomintegers to positivesumlist
        elif sum(positivesumlist) < zerosumgoal:
            positivesumlist.append(positiverandomintegers)
            positiverandomintegers = randint(0, zerosumgoal - sum(positivesumlist))
        #If positivesumlist less than or equal to zerosumgoal-5, then append integer zerosumgoal-5
        elif sum(positivesumlist) <= zerosumgoal - 5:
            positivesumlist.append(zerosumgoal - 5)
            break
        #Break while loop when positivesumlist is equal to zerosumgoal
        elif sum(positivesumlist) == zerosumgoal:
            break
    positivesumlist.sort(reverse=True)

    #Generate negative integers sum
    negativesumlist = []
    negativetotalcount = totalcount - len(positivesumlist)
    negativesumgoal = -zerosumgoal
    negativerandomintegers = randint(negativesumgoal, 0)
    while True:
        #Reset negativesumlist and negativerandomintegers if the count is greater than or equal to negativetotalcount
        if len(negativesumlist) > negativetotalcount:
            negativesumlist = []
            negativerandomintegers = randint(negativesumgoal, 0)
        #Append negativerandomintegers to negativesumlist
        elif sum(negativesumlist) > negativesumgoal:
            negativesumlist.append(negativerandomintegers)
            negativerandomintegers = randint(negativesumgoal - sum(negativesumlist), 0)
        #If one integer is needed to complete negativesumlist and count equals totalcount, then append the one integer
        elif len(negativesumlist) == negativetotalcount - 1 and sum(negativesumlist) > negativesumgoal:
            negativesumlist.append(negativesumgoal - sum(negativesumlist))
            break
        #Break while loop when negativesumlist is equal to zerosumgoal and negativesumlist count equals negativetotalcount
        elif sum(negativesumlist) == negativesumgoal and len(negativesumlist) == negativetotalcount:
            break
        #Reset negativesumlist and negativerandomintegers if the negativesumlist sum is higher than sumgoal while the len(negativesumlist) is less than negativetotalcount
        elif sum(negativesumlist) >= negativesumgoal and len(negativesumlist) < negativetotalcount:
            negativesumlist = []
            negativerandomintegers = randint(negativesumgoal, 0)
    negativesumlist.sort(reverse=True)
    return (positivesumlist + negativesumlist, sum(positivesumlist), sum(negativesumlist))


print(generatezerosumintegerslist(12, 45))
print(generatezerosumintegerslist(20, 50))
print(generatezerosumintegerslist(10, 100))
print(generatezerosumintegerslist(20, 90))
'''
([33, 8, 3, 1, 0, -1, -2, -3, -4, -7, -8, -20], 45, -45)
([18, 11, 9, 7, 3, 2, 0, 0, 0, 0, -1, -1, -2, -2, -3, -3, -3, -5, -14, -16], 50, -50)
([70, 16, 5, 4, 3, 1, 1, -3, -30, -67], 100, -100)
([31, 21, 21, 8, 4, 2, 1, 1, 1, 0, 0, -1, -1, -1, -1, -3, -8, -18, -25, -32], 90, -90)
'''
