# # Max girls that can be together
g = int(input("boys:"))
b = int(input("girls:"))

m = 0

if g>(b+1):
	if(g>(b*2)):
		m = g//b

	elif (g<(b*2)):
		m = (g//b)+1

else:
	 m = 1

print m

#Time interval between 2 times

from datetime import datetime
s1 = raw_input("start")
s2 = raw_input("end")
FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
print tdelta