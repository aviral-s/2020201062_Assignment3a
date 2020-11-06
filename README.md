# **ASSIGNMENT-3(part B)**
* I am using python 3.8.5 and the project was developed in sublime text editor.
* Folder contain `q1.py`, `q2.py`, `q3.py` and input - output files `org.json`, `date_calculator.txt`, `Employee1.txt`, `Employee2.txt` ...`Employeek.txt`and `output.txt`
* For question no. 3, `Employee1.txt`, `Employee2.txt` ...`Employeek.txt` files can be given as input file.
* All the file gave correct output on my system
* [https://github.com/aviral-s/2020201062_Assignment3a.git]

## **Q1**
* input json in `org.json` file.
* input is as follows:
<n> <emp1> <emp2> ... <empn>
* output is generated on terminal as follows:
<xyz>
<xyz> is <number> levels above <emp1>
<xyz> is <number> levels above <emp2>
where `<xyz` is the leader of the input employees.
* line30 : declare list as now there can be more than 2 employees.
* line31-33 : input is put in the list
* line 38 ,56 ,68 ,73 ,93 ,107 : for loop is added inorder to loop to all given employees and perform the operations as done on part a.
* line38-44 : these lines from part a are removed because now all the employee manipulation is done inside loop.


## **Q2**
* Input file `date_calculator.txt` contains two dates in two different lines.
* New date formats if present are specified in command line argument like mm/dd/yyyy ,mm.dd.yyyy ,mm-dd-yyyy.
* Output is produced on terminal and also written on `output.txt` 
* Haven't used any python library for date.
Following are the changes made to previous code:
* line2-6: `import sys` along with code to read command line input if given by user.
* `if` `else` statements are added for the new date format in line 53 58, 68 73, 83 88, 116 121, 131 136, 146 151

## **Q3**
* ast and simplejson lib is used as `import ast` and `import simplejson`
* Input is taken from user as 0.5, 1, 1.5 etc as slot duration.
* `Employee1.txt`,`Employee2.txt`,...,`Employeek.txt` contains busy slots of the employees and input is given in it.
* The desired output is produced on `output.txt`
* line3 : `import glob` inorder to get all the `Employee*.txt` file present inside the folder.
* line9 : Employees = glob.glob('Employee*.txt') is inserted to read all Employee files.
* line29 30: now list of listflag is created for each employee.
* line 13 ,31 ,45 ,48 ,117 ,124 ,179 ,199 : for loop for all the employee is inserted inorder to attain a kgeneric functionality for the code.

