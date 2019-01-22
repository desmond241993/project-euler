'''
Problem 4: A palindromic number reads the same both ways. The largest palindrome made from the product of 
2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

#function to determine if a number is palindrome
def palin(num):
    n = str(num)              #convert the number to a string
    l = len(n)                #find the length
    
    #loop through till half length
    for i in range(0,int(l/2)):
        if n[i] != n[l-i-1]:       #if values at opposite ends are not similar
            return False
    
    return True

b = None
largest_palin = 0
for i in range(0,1000):            #OUTER LOOP FOR 1ST 3-DIGIT NUMBER
    for j in range(0,1000):        #INNER LOOP FOR 2ND 3-DIGIT NUMBER
        p = i * j                  #PRODUCT OF THE TWO 3-DIGIT NUMBERS
        b = palin(p)               #CHECK IF THE PRODUCT IS A PALINDROME
        if(b == True):
            if(p > largest_palin):
                largest_palin = p
        
print("The largest palindrome made from the product of two 3-digit numbers is: "+str(largest_palin))
