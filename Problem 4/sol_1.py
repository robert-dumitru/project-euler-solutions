'''
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def max_palindrome(x):
    '''
    determines the biggest palindrome that can be obtained by multiplying 2 numbers x digits long.
    '''
    max_digits = 10 ** x - 1
    deficit = 0 #we search on the diagonals
    list_of_palindromes = []
    while len(list_of_palindromes) == 0:
        for i in range(deficit):
            product = (max_digits - i) * (max_digits - (deficit - i))
            if str(product) == str(product)[::-1]:
                list_of_palindromes.append(product)
        deficit += 1
    return list_of_palindromes[-1]
            
if __name__ == "__main__":
    print(max_palindrome(3))                
