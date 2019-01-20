'''
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 60085 ?

'''

def largest_prime_factor(n):
    largest_prime = 0               #variable to refer to largest prime 
    for i in range(2,n+1):          #outer loop to count numbers upto the given number 
        count = 0                   #count refreshed to 0 for reuse
        for j in range(2,int(i/2)):      #inner loop for determining whether a number is prime or not 
            if i%j == 0:
                count += 1
                break
        if count == 0:              #a prime number has only two factors;1 and the number itself
            #check if the new prime is a factor of the given number and is larger than the previous largest prime
            if n%i == 0 and i>largest_prime:      
                largest_prime = i 
    
    return largest_prime
    
print("The largest prime factor of the number 60085 is "+str(largest_prime_factor(60085)))
