import math

#function for computing the sum of primes 
def sum_of_primes(num):
    sum = 0                   
    for i in range(2,num):                   #outer for loop feeds in the number being checked for prime
        count = 0
        for j in range(2,int(math.sqrt(i))+1): #inner for loop checks if the number is prime 
            if i % j == 0:
                count += 1 
                break
        if count == 0:
            print(i)
            sum += i 
                
    return sum
    
num = 2000000
print("The sum of all primes less than {} is {}".format(num,sum_of_primes(num)))
