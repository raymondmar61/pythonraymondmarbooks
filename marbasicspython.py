#Basics Python Combine All Lessons Learned One Stop Book One Stop Documentation
#thenewbostonallvideos

print(18/5) #print 3.6
print(18//5) #print 3
print(18//5.0) #print 3.0
print(18/8) #print 2.25
print(18//8) #print 2
print(r"this story is \nokday d'kay") #print this story is \nokday d'kay. RM:  print as-is exact text
user = "Tuna McFish"
print(user[0]) #print T
print(user[1:4]) #print una
print(user[1:9:2]) #print uaMF
print(user[-1]) #print h
print(user[-1::-1]) #print hsiFcM an
players = [29, 58, 66, 71, 87]
print(players[2]) #print 66
players[2] = 68
print(players[2]) #print 68
newplayers = [90, 91, 98]
players = newplayers + players
print(players) #print [90, 91, 98, 29, 58, 68, 71, 87]
players.append(120)
print(players) #print [90, 91, 98, 29, 58, 68, 71, 87, 120]
players[7:] = [-1, -2, -3]
print(players) #print [90, 91, 98, 29, 58, 68, 71, -1, -2, -3]
name = "Bucky"
if name == "Bucky":
	print("Hey there Bucky") #print Hey there Bucky
elif name == "Lucky":
	print("You're lucky")
else:
	print("No name")
players = [29, 58, 66, 71, 87]
for eachplayers in players[0:3]:
	print(eachplayers,end=" ") #print 29 58 66
for eachnumber in range(100,-51,-25):
	print(eachnumber, end=", ") #print 100, 75, 50, 25, 0, -25, -50,
print("\n")