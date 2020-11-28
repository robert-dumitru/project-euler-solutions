'''
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def greatest_common_divisor(x,y):
    '''
    Returns the greatest common divisor of x and y via Euclid's algorithm.
    '''
    if y == 0:
        return x
    else:
        return greatest_common_divisor(y, x%y)

def least_common_multiple(x,y):
    '''
    Returns the least common multiple of x and y.
    '''
    return int(x * y / (greatest_common_divisor(x,y)))
    
def least_common_multiple_extended(list):
    '''
    Returns the least common multiple of a list.
    '''
    if len(list) == 2:
        return least_common_multiple(list[0], list[1])
    else:
        return least_common_multiple_extended([least_common_multiple(list[0], list[1])] + list[2:])

if __name__ == "__main__":
    print(least_common_multiple_extended(list(range(1,21))))
