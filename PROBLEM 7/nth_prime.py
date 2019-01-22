'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''
import math

#function to find n th prime
def find_prime(n):
    i = 2           #number for prime check
    p = 0           #count of the number of primes
    while True:
        if(p == n):                  #if the no of primes counted by the algo matches the input count
            return i-1               #return the corresponding prime
        count = 0                    #count refressed to keep track of the factors of a number
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0:             #if j is a factor of i
                count += 1           
                break               
        if count == 0:              #if count is 0 the checked number is a prime 
            p += 1
            
        i += 1
        
n = 10001        
print("The {}th prime number is {}".format(n,find_prime(n)))
