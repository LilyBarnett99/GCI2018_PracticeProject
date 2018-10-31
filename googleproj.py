# Google Code Project
for count in range (10): 
	print("GCI")
name = input("What's your name?")
name2 = name.lower()
nameLen = len(name)
backwardsName = name2[-1:-(nameLen + 1):-1]
print("Hey %s! Fancy meeting you here! Did you know that your name backwards is %s?" % (name,backwardsName))
