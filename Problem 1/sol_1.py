'''
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def multiples(x):
    '''
    Returns the sum of the multiples of 3 and 5 below x.
    '''
    sum = 0
    for i in range(1, x):
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    return(sum)

if __name__ == "__main__":
    print(multiples(1000))
