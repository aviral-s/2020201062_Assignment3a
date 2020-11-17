import json
def openfile():
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
	#print(mydict[i])
	return mydict, mylist
def listkeys():
	keylist = list()
	keylist = input().split()
	n = int(keylist[0])
	keylist.pop(0)
	return keylist


def getlist(mydict,keylist):
	#key1 = input()
	for i in range(0,len(keylist)):
		mylist1 = list()
		key = keylist[i]
		while mydict[key][0] != 'None':
			#print(mydict[key][0])
			mylist1.append(mydict[key])
			key = mydict[key][0]
		mylist.append(mylist1)
	return mylist

#mylist2 = list()
#key2 = input()
#key = key2
#while mydict[key][0] != 'None':
	#print(mydict[key][0])
	#mylist2.append(mydict[key])
def leader(mydict,keylist):
	flag = 0
	for i in range(0,len(keylist)):
		if mydict[keylist[i]][0] == 'None':
			print('No leader found')
			flag=1
			break
	return flag

#if mydict[key1][0] == 'None' or mydict[key2][0] == 'None':
	#print('No leader found')
def calculate(mylist,keylist,flag):
	if flag!=1:

		lenlist = list()
		for i in range(0,len(keylist)):
			l = len(mylist[i])
			lenlist.append(l)

		minl = min(lenlist)
		for i in range(0,len(keylist)):
			diff = lenlist[i]-minl
			mylist[i]=mylist[i][diff:]
	return mylist 







#len1 = len(mylist1)
#len2 = len(mylist2)
#if len1 > len2:
	#diff = len1 - len2
	#mylist1 = mylist1[diff:]
#elif len2 > len1:
	#diff = len2 - len1
	#mylist2 = mylist2[diff:]


def printelements(mylist,mydict,keylist,flag):
	if flag!=1:
		k=0
		p=0
		count = 0
		for i in range(0,len(mylist[0])):
			count = 0
			for j in range (0,len(mylist)-1):
				if mylist[j][i][0] != mylist[j+1][i][0]:
					break
				else:
					count=count+1
			if count==len(mylist)-1:
				print(mylist[0][i][0])
				k=i
				p=mydict[mylist[0][i][0]][1]
				break

		for i in range(0,len(mylist)):
			f = mydict[keylist[i]][1]
			print(mylist[0][k][0]+" "+"is "+str(f-p)+" level above "+keylist[i])






# Driver Code
mydict, mylist = openfile()
keylist = listkeys()
mylist = getlist(mydict,keylist)
flag = leader(mydict,keylist)
mylist = calculate(mylist,keylist,flag)
printelements(mylist,mydict,keylist,flag)



