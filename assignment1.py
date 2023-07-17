#Question 1
"""1. start the program
2. Take the input of a, b and c
3. if a == 0 then print the error message so that the coefficient cannot be zero
4. else calculate the discriminant = b**2-4*a*c
5. if discriminant < 0 then print error message that the roots are complex
6. else calculate  root1 = (-b + (discriminant ** 0.5)) / (2 * a)
          root2 = (-b - (discriminant ** 0.5)) / (2 * a)
7. print root1 and root2
8. stop the program"""

a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c:"))
root1 = root2 = 0
if a == 0:
    print("Error coefficient a cannot be zero")
else:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
          print("Error Roots are complex numbers")
    else:
          root1 = (-b + (discriminant ** 0.5)) / (2 * a)
          root2 = (-b - (discriminant ** 0.5)) / (2 * a)
print("Root 1:", root1)
print("Root 2:", root2)



#Question 2
sentence = input("enter a string:").lower()
x=sentence.split(" ")
y=[]
for i in x:
    if y.count(i)==0:
        y.append(i)
        print(i.title(),"-",sentence.count(i))




#Question 3
x = input("enter a sentence: ")
letters = digits = 0
for count in x:
    if count.isalpha():
        letters+=1
    elif count.isdigit():
        digits+=1
print("LETTERS",letters)
print("DIGITS",digits)



#Question 4
import re
pwd = input("enter your password:")
if int(len(pwd)<6 or len(pwd)>=12):
    if (re.search("[A-Z]",pwd) and re.search("[a-z]",pwd) and re.search("[0-9]",pwd) and re.search("[$#@]",pwd)):
        print("valid password")
    else:
        print("invalid password")



#Question 5
sentence = input("Enter a string: ")
target_word = input("Enter searchable word:")
words = sentence.split()#to split the sentence
positions = []#declare positions
index = 0
for word in words:
    if word == target_word:
        positions.append(index)
    index += 1
if positions:
    print(positions)
else:
    print(False)








