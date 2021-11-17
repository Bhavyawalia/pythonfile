#Arithmetic operations
value1=10
value2=20
value3=3
sum=value1+value1
print("sum=",sum)
subtraction=value2-value1
print("subtraction=",subtraction)
mutiply=value1*value2
print("Multiplication=",mutiply)
divide=value1/value3
print("Divide=",divide)
modulus=value1%value3
print("Modulus=",modulus)
floordiv=value1//value3
print("Floor division=",floordiv)
exponent=value1**value3
print("Exponent=",exponent)

# Assignment operators
a=10
print(a)
a+=5
print(a)
a-=2
print(a)
a*=2
print(a)
a/=2
print(a)
a%=2
print(a)
a//=2
print(a)
a**=2
print(a)

# Logical operators
if(value1<value2) and (value1>=value3):
    print("And condition")
if(value1>=value2) or (value1>value3):
    print("Or condition")
if(value1!=0):
    print("Not condition")

# if-else statement(even/odd number)
n=int(input("Enter the number"))
if n%2==0:
    print("Even")
else:
    print("Odd")

# Leap year
n=int(input("Enter the year"))
"""if n%4==0 and (n%100!=0 or n%400==0):
    print("Leap year")
else:
    print("Not a leap year")"""
if n%4==0:
    if n%100==0:
        if n%400==0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")


# List functions
list1=[]
list2=[10,'Python',20.5]
list1.extend(list2)         # extend
print(list1)
list1.append(80)            # append
print(list1)
list1.insert(3,"Three")     # insert
print(list1)
list1.remove("Python")      # remove
print(list1)
list2.clear()               # clear
print(list2)

# for and while loop
for i in range(0,1):
    i=i+5
    print("For loop",i)
b=5
while(b<10):
    b+=5
    print("while loop",b)
