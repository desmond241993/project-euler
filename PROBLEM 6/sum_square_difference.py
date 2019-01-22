'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

#function to find the sum of the squares of first n natural numbers - (1)
def sum_of_squares(n):
    s = 0
    for i in range(1,n+1):
        s = s + i ** 2
        
    return s

#function to find the square of the sum of first n natural numbers - (2)
def square_of_sum(n):
    return (n * (n+1) / 2) ** 2

#function to find the difference between (1) and (2)
def find_sum_square_diff(num):
    return int(square_of_sum(num) - sum_of_squares(num))

n = 100
print("The difference between the sum of the squares of the first {} natural numbers and the square of the sum is {}".format(n,find_sum_square_diff(n)))
