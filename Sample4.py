# Factorial using recursion
def factorial(num):
    if num>=1:
        return num*factorial(num-1)
    else:
        return 1
num=int(input("Enter the number"))
print("Factorial of {}=".format(num),factorial(num))

# Factorial without recursion
num=int(input("Enter the number"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of {}=".format(num),fact)

# Area
import math
def triangle(s1,s2,s3):
    s=(s1+s2+s3)/2
    area=math.sqrt((s*(s-s1)*(s-s2)*(s-s3)))
    return area
s1=int(input("Enter side1"))
s2=int(input("Enter side2"))
s3=int(input("Enter side3"))
print("Area of triangle=",triangle(s1,s2,s3))

def square(side):
    area=side*side
    return area
side=int(input("Enter the side"))
print("Area of square=",square(side))

def rectangle(length,breadth):
    area=length*breadth
    return area
length=float(input("Enter the length of rectangle"))
breadth=float(input("Enter the breadth of rectangle"))
print("Area of rectangle=",rectangle(length, breadth))

# Inheritance
class Data1:
    def Name(self, name):
        return name


class Data2:
    def Age(self, age):
        return age


class DerivedData(Data1, Data2):
    def Country(self, country):
        return country


d = DerivedData()
print(d.Name("Akshi"))
print(d.Age(20))
print(d.Country("Canada"))


class Data1:
    def Name(self, name):
        return name


class Data2(Data1):
    def Age(self, age):
        return age


class DerivedData(Data2):
    def Country(self, country):
        return country


d = DerivedData()
print(d.Name("Akshi"))
print(d.Age(20))
print(d.Country("Canada"))

# Sum of natural numbers
num=int(input("Enter the number"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print("Sum of first {} natural numbers=".format(num),sum)





