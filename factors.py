import sys

file = sys.argv[1]

def get_factors(num):
    factor1 = 0
    factor2 = 0
    for i in range(2,num):
        if (num % i == 0):
            factor1 = max(i, num/i)
            factor2 = min(i , num/i)
            break

    print("{:.0f}={:.0f}*{:.0f}".format(num,factor1,factor2))

def open_file(arg):
    with open(arg, 'r') as file:
        for line in file:
            get_factors(int(line))
            

open_file(file)