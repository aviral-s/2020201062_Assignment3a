import ast
import simplejson
l1 =list()
l2 =list()
duration = float(input())
with open('Employee1.txt', 'r') as file1:
    data1 = file1.read().replace('\n', '') 
    res1 = ast.literal_eval(data1)
    for x in res1:
    	emp1 = x
    	#print(type(emp1))
    	res1=res1[x]
    for x in res1:
    	dt = x
    	l1 = res1[x]
    print(data1)
with open('Employee2.txt', 'r') as file2:
    data2 = file2.read().replace('\n', '')
    res2 = ast.literal_eval(data2)
    for x in res2:
    	emp2 = x
    	res2=res2[x]
    for x in res2:
    	l2 = res2[x]
    print(data2)
boolsf = 0
boolef = 0
sflag1 =[0]*17
eflag1 =[0]*17
sflag2 =[0]*17
eflag2 =[0]*17
timetoint = {'9:00AM':0, '9:30AM':1, '10:00AM':2, '10:30AM':3, '11:00AM':4, '11:30AM':5, '12:00PM':6, '12:30PM':7, '1:00PM':8, '1:30PM':9, '2:00PM':10, '2:30PM':11, '3:00PM':12, '3:30PM':13, '4:00PM':14, '4:30PM':15, '5:00PM':16}
inttotime = {0:'9:00AM', 1:'9:30AM', 2:'10:00AM', 3:'10:30AM', 4:'11:00AM', 5:'11:30AM', 6:'12:00PM', 7:'12:30PM', 8:'1:00PM', 9:'1:30PM', 10:'2:00PM', 11:'2:30PM', 12:'3:00PM', 13:'3:30PM', 14:'4:00PM', 15:'4:30PM', 16:'5:00PM'}
for item in l1:
	item = item.split(' ')
	#print(item)
	sflag1[timetoint[item[0]]]=1
	eflag1[timetoint[item[2]]]=1
	for i in range(timetoint[item[0]]+1 , timetoint[item[2]]):
		sflag1[i]=1
		eflag1[i]=1
free1 =list()
str
for i in range(0,17):
	if sflag1[i]==1 and eflag1[i]==1:
		continue
	if sflag1[i]==1 and eflag1[i]!=1:
		str = str + inttotime[i]
		free1.append(str)
	if sflag1[i]!=1 and eflag1[i]==1:
		str = inttotime[i]+"-"
		continue
	if sflag1[i]!=1 and eflag1[i]!=1 and boolsf==0:
		str = inttotime[i]+"-"
		boolsf = 1
	if sflag1[i]!=1 and eflag1[i]!=1 and i==16:
		str = str + inttotime[i]
		free1.append(str)
boolsf = 0



for item in l2:
	item = item.split(' ')
	#print(item)
	sflag2[timetoint[item[0]]]=1
	eflag2[timetoint[item[2]]]=1
	for i in range(timetoint[item[0]]+1 , timetoint[item[2]]):
		sflag2[i]=1
		eflag2[i]=1
free2 =list()
str
for i in range(0,17):
	if sflag2[i]==1 and eflag2[i]==1:
		continue
	if sflag2[i]==1 and eflag2[i]!=1:
		str = str + inttotime[i]
		free2.append(str)
	if sflag2[i]!=1 and eflag2[i]==1:
		str = inttotime[i]+"-"
		continue
	if sflag2[i]!=1 and eflag2[i]!=1 and boolsf==0:
		str = inttotime[i]+"-"
		boolsf = 1
	if sflag2[i]!=1 and eflag2[i]!=1 and i==16:
		str = str + inttotime[i]
		free2.append(str)
boolsf = 0




flag1 = [0]*17
flag2 = [0]*17
flag = [0]*17
for item in free1:
	item = item.split('-')
	begin = timetoint[item[0]]
	end = timetoint[item[1]]
	for i in range(begin, end+1):
		flag1[i]=1

print(flag1)


for item in free2:
	item = item.split('-')
	begin = timetoint[item[0]]
	end = timetoint[item[1]]
	for i in range(begin, end+1):
		flag2[i]=1

print(flag2)

for i in range(0,17):
	flag[i] = flag1[i] & flag2[i]

print(flag)

sum=0
for i in range(0,17):
	if i==16 and sum<duration:
		str = "no slot available"
		break
	if flag[i]==1 and boolef ==0:
		sum = 0
		initial = inttotime[i]
		boolef = 1
	elif flag[i]==1 and flag[i+1]==0 and i!=16:
		sum = sum + 0.5
		boolef = 0
		if(sum==duration):
			str=initial+"-"+inttotime[i]
			break
	elif flag[i]==1 :
		sum = sum + 0.5
		if(sum==duration):
			str = initial+"-"+inttotime[i]
			break
	elif flag[i]==0:
		sum=0
		boolef = 0
		continue
	


print("Available slot")
print(emp1,":",free1)
print(emp2,":",free2)
print(str)


#for i in sflag1:
	#print(i)

#print(sflag1)
#print(eflag1)
#print(sflag2)
#print(eflag2)
#print(l1)
#print(l2)
file = open('output.txt', 'w')
file.write('Available slot \n')
file.write(emp1+': ')
simplejson.dump(free1, file)
file.write('\n'+emp2+': ')
simplejson.dump(free2, file)
file.write('\n')
file.write('\n')
file.write('Slot duration: '+f'{duration}'+' hours\n')
dict = {dt:str}
simplejson.dump(dict,file)
file.close()












#{'Employee2': {'5/10/2020':['10:30AM - 11:30AM', '12:00PM - 1:00PM', '1:00PM - 1:30PM', '3:30PM - 4:30PM']}}
#{'Employee1': {'5/10/2020':['10:00AM - 11:00AM', '12:30PM - 1:00PM', '4:00PM - 5:00PM']}}