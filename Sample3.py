# Arithmetic functions
def arithmetic(operator):
    a=10
    b=3
    if operator=='+':
        print("Sum=",a+b)
    elif operator=='-':
        print("Subtraction=",a-b)
    elif operator=='/':
        print("Division=",a/b)
    elif operator=='//':
        print("Floor division=",a//b)
    elif operator=='*':
        print("Multiplication=",a*b)
    else:
        print("Exponent=",a**b)

arithmetic(input("Enter the operator"))

# Binary sort
def sorting(seq):
   for i in range(1, len(seq)):
      temp = seq[i]
      pos = binary_search(seq, temp, 0, i) + 1
      for k in range(i, pos, -1):
         seq[k] = seq[k - 1]
      seq[pos] = temp
def binary_search(seq, key, start, end):
   if end - start <= 1:
      if key < seq[start]:
         return start - 1
      else:
         return start
   mid = (start + end)//2
   if seq[mid] < key:
      return binary_search(seq, key, mid, end)
   elif seq[mid] > key:
      return binary_search(seq, key, start, mid)
   else:
      return mid
seq = [10,5,30,14,8,86,13,400]
n = len(seq)
sorting(seq)
print("Sorted output is:")
for i in range(n):
   print(seq[i],end=" ")

# Lambda function
list1=[i for i in range(1,11)]
table=list(map(lambda n:n*2,list1))
print("\nTable of 2=",table)

# Factors
num=int(input("Enter the number"))
factors_list=[]
for i in range(1,n+1):
    if num%i==0:
        factors_list.append(i)
print(factors_list)

# squareroot
num=int(input("Enter the number"))
squareroot=num**0.5
print("Squareroot=",squareroot)

# Prime number
num=int(input("Enter the number"))
count=0
for i in range(2,num):
    if num%i==0:
        count=count+1
        break
if count==0:
    print("Prime number")
else:
    print("Not prime")

