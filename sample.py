#write a python3 program to take a number input from user and check if it is a prime or not
#we will use the fact that no is prime if there is no divisor before its square root 
# we also knows that all prime number areo of the form 6n+1 or 6n-1 except 2 and 3

import math
def isprime(n):
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

n=int(input("Enter a number: "))
if isprime(n):
    print("Prime")
else:
    print("Not Prime")

#output
#Enter a number: 13
#Prime
#Enter a number: 12
#Not Prime

# Path: sample.py
# Author: Arpit
