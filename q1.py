import json
with open('org.json',) as f:
	data = json.load(f)
a =0
mydict = dict()
mylist = list()
for item in data:
	for i in data[item]:
		i['level']=a
		x = i['name']
		if a != 0 :
			y = i['parent']
		else :
			y = 'None'
		z = i['level']
		#print(x)
		#print(y)
		#print(z)
		mydict[x] = y,z
		#mylist.append(i)
		#mydict['level']=a
		#print(i)
		#print(a)
	a = a+1
#print(mylist)
#for i in mydict:
	#print(mydict[i][0])

mylist1 = list()
key1 = input()
key = key1
while mydict[key][0] != 'None':
	#print(mydict[key][0])
	mylist1.append(mydict[key])
	key = mydict[key][0]


mylist2 = list()
key2 = input()
key = key2
while mydict[key][0] != 'None':
	#print(mydict[key][0])
	mylist2.append(mydict[key])
	key = mydict[key][0]

if mydict[key1][0] == 'None' or mydict[key2][0] == 'None':
	print('No leader found')

len1 = len(mylist1)
len2 = len(mylist2)
if len1 > len2:
	diff = len1 - len2
	mylist1 = mylist1[diff:]
elif len2 > len1:
	diff = len2 - len1
	mylist2 = mylist2[diff:]

for i in range(0,len(mylist1)):
	if mylist1[i][0] == mylist2[i][0]:
		print(mylist1[i][0])
		p = mydict[mylist1[i][0]][1]
		f = mydict[key1][1]
		s = mydict[key2][1]
		print(mylist1[i][0]+" "+"is "+str(f-p)+" level above "+key1)
		print(mylist1[i][0]+" "+"is "+str(s-p)+" level above "+key2)
		break


#print(mylist1)
#print(mylist2)
#print(mydict)
#print(type(data))
#print(data)