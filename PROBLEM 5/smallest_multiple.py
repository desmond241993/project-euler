'''
Problem 5: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

'''
import math

#function to return the lcm of first n numbers
def smallest_find_number(num):
    p = 1
    for i in range(1,num+1):
         p = int((p * i)/math.gcd(p,i))    #gcd(to find Greatest Common Divisor) is a function of math class
    
    return p


n = 20
print("The smallest positive number that is evenly divisible by all the numbers from 1 to 20"+str(smallest_find_number(n)))
