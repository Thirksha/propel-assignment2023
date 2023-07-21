#QUESTION 1
list = []
for i in range(2000,2500):
    if i%5==0 and i%8==0:
        x=list.append(i)
print(list)


#QUESTION 2
n= int(input("enter the number:"))
c =10
for i in range(1,11):
    x=i*n
    print(i,"x",n,"=",x)


#QUESTION 3
list=[5,8,4,2,6,7,3]
list.sort()
print(list)
print(list[0])


#QUESTION 4
list=[23,54,34,87,56,77,99]
list.sort()
print(list)
print(list[-2])


#QUESTION 5
list=[1,2,3,4,5,6,7,8,9,10]
print(list)
even =[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers are",even)
print("odd numbers are",odd)


#QUESTION 6
list=[5,8,4,2,6,7,3]
print(list)
print(list[::-1])


#QUESTION 7
list=[]
for i in range(0,50+1):
    if i%2!=0:
        x=list.append(i)
print(list)


#QUESTION 8
list=[1,2,3,4,5,6,7,8,9,10]
print(list)
even_count =0
odd_count =0
for i in list:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even numbers are",even_count)
print("odd numbers are",odd_count)


#QUESTION 9
import re
IP_address= ("216.08.094.196")
print(IP_address)
Ip =re.sub('\.[0]*', '.',IP_address)
print(Ip)


#QUESTION 10
import re
str=input("enter the string:")
i=re.findall("a+\S+s",str)
print(i)


#QUESTION 11
string = "They ate 6 apples and 10 bananas"
a=string.replace("6","six")
b=a.replace("10","ten")
print(b)


#QUESTION 12
age = int(input("enter the age:"))
if age>18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")


#QUESTION 13
unit = int(input("enter the electricity unit:"))
if unit<=100 and unit>=0:
    print("free electricity no need to pay")
elif unit>100 and unit<=200:
    a=100*5
    print("current bill is",a,"rupees")
elif unit>200:
    b=200*10
    print("current bill is",b,"rupees")
else:
    print("invalid unit")


#QUESTION 14
mark = int(input("enter the marks:"))
if mark>90:
    print("Grade A")
elif mark>80 and mark<=90:
    print("Grade B")
elif mark>=60 and mark<=80:
    print("Grade c")
elif mark<60:
    print("Grade D")