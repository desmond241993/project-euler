'''
Problem 1: Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.
'''

def sum_of_multiples(m1,m2,n):
    sum = 0 
    for i in range(0,n):
        if i%3 == 0 or i%5 == 0:
           sum += i
    return sum
    
print("The sum of all multiples of 3 or 5 below 1000 is "+str(sum_of_multiples(3,5,1000)))
