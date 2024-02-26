import  datetime

# print(datetime.datetime.now())
# print(datetime.datetime.now().date())
# print(datetime.datetime.now().time())
# print(datetime.timedelta(1))

# now = datetime.datetime.now()
# epoch =now
# print(epoch)


# import time
# epoch = time.time()
# t = time.localtime(epoch)
# #retrieve the date from structure t
# d = t. tm_mday
# m = t. tm_mon
# y = t. tm_year
# print("Current date is:%d - %d - %d" %(d,m,y))
# #retrieve the time from structure t
# h= t.tm_hour
# m =t.tm_min
# s = t.tm_sec
# print("Current time is:%d :%d :%d" %(h,m,s))

# print("Check_Format:{}/{}/{}".format("Prasad","Spyd","Tech"))

from datetime import *
# d=date(2019,7,29)
# t=time(11,30)
# dt=datetime.combine(d,t)
# print(dt)

# dt1=datetime(year = 2019,month=7,day=29,hour=11,minute=25,second=25)
# print(dt1)
# #change it’s year,month and hour values
# dt2=dt1.replace(year =2020,hour=11,month=12,day=26)
# print(dt2)


# today = datetime.now()
# today_type = type(today)
# print(today_type)
# st_today = today.strftime("%d-%m-%Y %H:%M:%S")
# print(type(st_today))

# from calendar import *


# this_month = month(2024,2)
# print(this_month)
# import re

# write a program re module to find all the numbers in a given string
# s = 'I have 2 pens and 3 pencils'
# print(re.findall(r'p\w+',s))



# details.py
# get input from user and check if the input is a String or not (Name)
# get input from user and check if the input is a valid email or not (Mobile)
# get input from user and check if the input is a valid phone number or not (Email)
# If above is not valid then ask the user to enter the correct input else prind the entered Details
# checking.py
# add some dummy data to the details in list/dict/set/tuple use any one
# Validate user details or there are valid or not
# if valid print the user confirmation message "User Exist"
# rout to Frappe Webpage page if the user is valid
# if the user is not valid then ask the user to enter the correct details

import re
# \d		   represents any digit (0-9)                       
# \D                        represents any non digit.
# \s                         represents white space.           
# \S                        represents non-white space character.
# \w                       represents any alphanumeric(A-Z,a-z,0-9)                  
# \W                       represents non-alphanumeric 			    
# \b                       represents a space around words
# \A                       Matches only at start of the string
# \Z		    Matches only at the end of the string         
digits = re.compile(r'\d')
# print(digits.findall('I have 2 pens and 3 pencils'))
non_digits = re.compile(r'\D')
# print(non_digits.findall('I have 2 pens and 3 pencils'))
white_space = re.compile(r'\s')
# print(white_space.findall('I have 2 pens and 3 pencils'))
non_white_space = re.compile(r'\S')
# print(non_white_space.findall('I have 2 pens and 3 pencils'))
alphanumeric = re.compile(r'\w')
# print(alphanumeric.findall('I have 2 pens and 3 pencils'))
non_alphanumeric = re.compile(r'\W')
# print(non_alphanumeric.findall('I have 2 pens and 3 pencils'))
# print(re.findall(r'p\w+', 'I have 2 pens and 3 pencils'))
# space_around_words = re.compile(r'\b')
# print(space_around_words.findall('I have 2 pens and 3 pencils'))
# match_start = re.compile(r'\A')
# print(match_start.findall('I have 2 pens and 3 pencils'))
# match_end = re.compile(r'\Z')
# print(match_end.findall('I have 2 pens and 3 pencils'))

# # new function
# import re
# str = 'Saketh : 8106429771'
# # \d represents any digit (0-9) 
# res = re.search(r'\d+',str)
# print(res.group())
# # \D represents any non digit.
# red = re.search(r'\D+',str)
# print(red.group())
# #a[nk] rep either ‘n’ or ‘k’ or both after ‘a’
# str="anil akhil arun arati arundhati ankur"
# res=re.findall(r'a[nk][\w]*',str)
# print(res)



#A Python Program to create a regular expression to retrieve data.
#displaying marks and names
# import re
# str = "Saketh got 95 marks,Sony got 98 marks and Ajay got 96 marks. and Prasad got 7 marks."
# #extract only marks having 2 digits
# marks=re.findall('\d{2}',str)
# print(marks)
# #extract names 
# names=re.findall('[A-Z][a-z]*',str)
# print(names)


#A Python Program to create a regular expression to retrieve specific data:
import re
# str='an apple a day keeps the doctor away'
# result=re.findall(r'a[\w]*',str)
# for word in result:
#       print(word) 
# # Create New File and write the above data into the file
# f=open('test1.txt', 'w') #open the file for writing
# for word in result:
# 	f.write(word+'\n')
# f.close()
# Read the data from the file and display the data
# D:\Python\day-4\day-7.py\day-7.py
f=open('test1.txt','r') #open the file for reading
data=f.read()
print(data)

#length of the string in the file
print(len(data))

#count the number of words in the file
print(len(data.split()))
