from sys import exit
class Date:  
    def __init__(self, d, m, y):  
        self.d = d             
        self.m = m    
        self.y = y    
    
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ] 

def countLeapYears(d): 
      
    years = d.y  
    if (d.m <= 2) : 
        years =years - 1 
    return int(years / 4 - years / 100 + years / 400 ) 
   
def getDifference(dt1, dt2) :  
    n1 = dt1.y * 365 + dt1.d  
    for i in range(0, dt1.m - 1) : 
        n1 = n1 + monthDays[i]  
    n1 =n1 + countLeapYears(dt1)   
    n2 = dt2.y * 365 + dt2.d  
    for i in range(0, dt2.m - 1) : 
        n2 =n2 + monthDays[i]  
    n2 = n2 + countLeapYears(dt2)  
    return (n2 - n1)  
   
  
# Driver program
monthDict={'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12, 'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
file1 = open('date_calculator.txt', 'r')
line = file1.readline() 
if line.find('th') != -1:
    str = line.split(' ')
    d1 = int(str[1][:-2])
    m1 = monthDict[str[2][:-1]]
    y1 = int(str[3][:4])
    #print(type(d1))
    #print(type(m1))
    #print(m1)
    #print(type(y1))
    #print(str)
    #print(line)
    dt1 = Date(d1, m1, y1 )
elif line.find('/') !=-1:
    str = line.split(' ')
    str = str[1].split('/')
    #print(str)
    d1 = int(str[0])
    m1 = int(str[1])
    y1 = int(str[2][:4])
    dt1 = Date(d1, m1, y1 )

elif line.find('-') !=-1:
    str = line.split(' ')
    str = str[1].split('-')
    #print(str)
    d1 = int(str[0])
    m1 = int(str[1])
    y1 = int(str[2][:4])
    dt1 = Date(d1, m1, y1 )

elif line.find('.') !=-1:
    str = line.split(' ')
    str = str[1].split('.')
    #print(str)
    d1 = int(str[0])
    m1 = int(str[1])
    y1 = int(str[2][:4])
    dt1 = Date(d1, m1, y1 )

else:
    print("Please enter valid date in the file!")
    exit()


line = file1.readline() 
if line.find('th') != -1:
    str = line.split(' ')
    d1 = int(str[1][:-2])
    m1 = monthDict[str[2][:-1]]
    y1 = int(str[3][:4])
    #print(type(d1))
    #print(type(m1))
    #print(m1)
    #print(type(y1))
    #print(str)
    #print(line)
    dt2 = Date(d1, m1, y1 )
elif line.find('/') !=-1:
    str = line.split(' ')
    str = str[1].split('/')
    #print(str)
    d1 = int(str[0])
    m1 = int(str[1])
    y1 = int(str[2][:4])
    dt2 = Date(d1, m1, y1 )

elif line.find('-') !=-1:
    str = line.split(' ')
    str = str[1].split('-')
    #print(str)
    d1 = int(str[0])
    m1 = int(str[1])
    y1 = int(str[2][:4])
    dt2 = Date(d1, m1, y1 )

elif line.find('.') !=-1:
    str = line.split(' ')
    str = str[1].split('.')
    #print(str)
    d1 = int(str[0])
    m1 = int(str[1])
    y1 = int(str[2][:4])
    dt2 = Date(d1, m1, y1 )
    
else:
    print("Please enter valid date in the file!")
    exit()

file1.close() 
file2 = open("output.txt", "w")
temp = getDifference(dt1,dt2)
temp = f'{temp}'
#temp = str(temp)
#print(type(temp))
s = "Date difference: "+temp+" days"
file2.write(s)
file2.close()
#dt1 = Date(10, 9, 2020 ) 
#dt2 = Date(11, 9, 2020 ) 
#print(type(getDifference(dt1, dt2)))
print("Date difference:", getDifference(dt1, dt2), "days") 