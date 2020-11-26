'''
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def biggest_factor(x):
    '''
    Prime factorizes x, then returns the greatest element of the list.
    '''
    prime_factors = []
    current_factor = 2
    remainder = x
    while remainder != 1:
        if remainder % current_factor == 0:
            prime_factors.append(current_factor)
            remainder = remainder / current_factor
        else: 
            current_factor += 1
    return(prime_factors[-1])
    
 if __name__ == "__main__":
    print(biggest_factor(600851475143))
