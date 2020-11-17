import ast
import simplejson
import glob
l1 =list()
l2 =list()
l = list()
emp = list()
number_files = 0
def fileread():
	duration = float(input())
	Employees = glob.glob('Employee*.txt')
	Employees.sort()
	#elist = os.listdir('./Employee/') # dir is your directory path
	number_files = len(Employees)
	for i in range(0,number_files):
		#s = 'Employee'+str(i+1)+'.txt'
		s = Employees[i]
		file1 = open(s,'r')
		data1 = file1.read().replace('\n','')
		res1 = ast.literal_eval(data1)
		for x in res1:
			emp.append(x)
			res1=res1[x]
		for x in res1:
			dt = x
			l.append(res1[x])
		print(data1)
		file1.close()
	return number_files, l, duration, dt,emp
boolsf = 0
boolef = 0
sflag = list()
eflag = list()
#for i in range(0,number_files):
	#sflag.append([0]*17)
	#eflag.append([0]*17)
#sflag1 =[0]*17
#eflag1 =[0]*17
#sflag2 =[0]*17
#eflag2 =[0]*17
timetoint = {'9:00AM':0, '9:30AM':1, '10:00AM':2, '10:30AM':3, '11:00AM':4, '11:30AM':5, '12:00PM':6, '12:30PM':7, '1:00PM':8, '1:30PM':9, '2:00PM':10, '2:30PM':11, '3:00PM':12, '3:30PM':13, '4:00PM':14, '4:30PM':15, '5:00PM':16}
inttotime = {0:'9:00AM', 1:'9:30AM', 2:'10:00AM', 3:'10:30AM', 4:'11:00AM', 5:'11:30AM', 6:'12:00PM', 7:'12:30PM', 8:'1:00PM', 9:'1:30PM', 10:'2:00PM', 11:'2:30PM', 12:'3:00PM', 13:'3:30PM', 14:'4:00PM', 15:'4:30PM', 16:'5:00PM'}


temp = list()
free = list() 
def freeslot(number_files, l):
	for j in range(0,number_files):
		free.append([])
		sflag.append([0]*17)
		eflag.append([0]*17)

	for j in range(0,number_files):
		for item in l[j]:
			item = item.split(' ')
			#print(item)
			sflag[j][timetoint[item[0]]]=1
			eflag[j][timetoint[item[2]]]=1
			for i in range(timetoint[item[0]]+1 , timetoint[item[2]]):
				sflag[j][i]=1
				eflag[j][i]=1
		#free1 =list()
def freed1(boolsf):
	for j in range(0,number_files):
		str=''
		free1 = list()
		for i in range(0,17):
			boolsf,str = freeslotstr(i,j,boolsf,str)
			
		#print('hi',free1)
		#free.append(free1)
		#print('hew',free)
		#free1.clear()
		boolsf = 0
	#print(free)
'''def funE():
	if sflag[j][i]==1 and eflag[j][i]==1:
		continue
	elif sflag[j][i]==1 and eflag[j][i]!=1 and boolsf==1:
		str = str + inttotime[i]
		free[j].append(str)
		boolsf=0
	elif sflag[j][i]!=1 and eflag[j][i]==1:
		boolsf = 1
		str = inttotime[i]+"-"
		continue
	elif sflag[j][i]!=1 and eflag[j][i]!=1 and boolsf==0:
		str = inttotime[i]+"-"
		boolsf = 1
	elif sflag[j][i]!=1 and eflag[j][i]!=1 and i==16:
		str = str + inttotime[i]
		free[j].append(str) '''





def freeslotstr(i,j,boolsf,str):
	if sflag[j][i] == 1:
		#if eflag[j][i] == 1:
			
		if eflag[j][i]!=1 and boolsf==1:
			str = str + inttotime[i]
			free[j].append(str)
			boolsf=0
	else:
		if eflag[j][i]==1:
			boolsf = 1
			str = inttotime[i]+"-"
			#continue
		else:
			if boolsf==0:
				str = inttotime[i]+"-"
				boolsf = 1
			elif i==16:
				str = str + inttotime[i]
				free[j].append(str)
	return boolsf,str





#for item in l2:
	#item = item.split(' ')
	#print(item)
	#sflag2[timetoint[item[0]]]=1
	#eflag2[timetoint[item[2]]]=1
	#for i in range(timetoint[item[0]]+1 , timetoint[item[2]]):
		#sflag2[i]=1
		#eflag2[i]=1
#free2 =list()
#str
#for i in range(0,17):
	#if sflag2[i]==1 and eflag2[i]==1:
		#continue
	#elif sflag2[i]==1 and eflag2[i]!=1 and boolsf==1:
		#str = str + inttotime[i]
		#free2.append(str)
		#boolsf=0
	#elif sflag2[i]!=1 and eflag2[i]==1:
		#boolsf=1
		#str = inttotime[i]+"-"
		#continue
	#elif sflag2[i]!=1 and eflag2[i]!=1 and boolsf==0:
		#str = inttotime[i]+"-"
		#boolsf = 1
	#elif sflag2[i]!=1 and eflag2[i]!=1 and i==16:
		#str = str + inttotime[i]
		#free2.append(str)
#boolsf = 0



flagl = list()


#flag1 = [0]*17
#flag2 = [0]*17
flag = [0]*17
def setflag(flagl):
	for i in range(0,number_files):
		flagl.append([0]*17)
	for i in range(0,number_files):
		for item in free[i]:
			item = item.split('-')
			begin = timetoint[item[0]]
			end = timetoint[item[1]]
			for j in range(begin, end+1):
				flagl[i][j]=1
	return flagl

	#print(flag1)


#for item in free2:
	#item = item.split('-')
	#begin = timetoint[item[0]]
	#end = timetoint[item[1]]
	#for i in range(begin, end+1):
		#flag2[i]=1

#print(flag2)
def setintflag(flagl,number_files):
	for i in range(0,17):
		flag[i] = flagl[0][i] & flagl[1][i]
		for j in range(2,number_files):
			flag[i] = flag[i] & flagl[j][i]

	#print(flag)

sum=0
def commonslot(sum,duration,boolef):
	str = ''
	initial = ''
	for i in range(0,17):
		if i==16 and sum<duration:
			str = "no slot available"
			break
		if flag[i] == 1:
			sum, str, boolef, brk, initial = commonutil(i, boolef, str,sum, initial)
			if brk == 1:
				break
		
		elif flag[i]==0:
			sum=0
			boolef = 0
			continue



	print("Available slot")
	for i in range(0,number_files):
		print(emp[i],":",free[i])

	#print(emp1,":",free1)
	#print(emp2,":",free2)
	print(str)
	return str

def commonutil(i,boolef,str,sum, initial):
	brk = 0
	if boolef ==0:
		sum = 0
		initial = inttotime[i]
		boolef = 1
	elif flag[i+1]==0 and i!=16:
		sum = sum + 0.5
		boolef = 0
		if(sum==duration):
			str=initial+"-"+inttotime[i]
			brk = 1
	else :
		sum = sum + 0.5
		if(sum==duration):
			str = initial+"-"+inttotime[i]
			brk = 1
	return sum, str , boolef, brk , initial

	


	


#for i in sflag1:
	#print(i)

#print(sflag1)
#print(eflag1)
#print(sflag2)
#print(eflag2)
#print(l1)
#print(l2)
def filewrite(dt,number_files,emp,str):
	file = open('output.txt', 'w')
	file.write('Available slot \n')
	for i in range(0,number_files):
		file.write(emp[i]+': ')
		simplejson.dump(free[i],file)
		file.write('\n')
	file.write('\n')

	#file.write(emp1+': ')
	#simplejson.dump(free1, file)
	#file.write('\n'+emp2+': ')
	#simplejson.dump(free2, file)
	#file.write('\n')
	#file.write('\n')
	file.write('Slot duration: '+f'{duration}'+' hours\n')
	dict = {dt:str}
	simplejson.dump(dict,file)
	file.close()












#{'Employee2': {'5/10/2020':['10:30AM - 11:30AM', '12:00PM - 1:00PM', '1:00PM - 1:30PM', '3:30PM - 4:30PM']}}
#{'Employee1': {'5/10/2020':['10:00AM - 11:00AM', '12:30PM - 1:00PM', '4:00PM - 5:00PM']}}



number_files, l, duration,dt,emp = fileread()
freeslot(number_files, l)
freed1(boolsf)
flagl=setflag(flagl)
setintflag(flagl,number_files)
str = commonslot(sum, duration,boolef)
#commonutil()
filewrite(dt,number_files,emp,str)
