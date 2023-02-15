'''
Task 1: Happy Numbers
A happy number is a number defined by the following process: starting with any positive integer, 
replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1. An example of a happy number is 19
(For more info: https://en.wikipedia.org/wiki/Happy_number)
Write a method that determines if a number is happy or sad
'''

def happy_numbers(num):

    is_happy = False
    x = num

    while x >= 10:
        sum = 0
        while x > 0:
            r = x % 10
        # modulo 10 will show the second digit in the number which we 
        # can then isolate and square (in this case 9**2 which is 81)
            sum += (r**2)
            x = x // 10
        # x//10 will show the first digit (rounded down which we want so in this case 19//10 is 1) 
        # and then x will be sent back through the loop where we will find x(1) % 10 (which would be 1) 
        # which will then be added to our sum -- the sum will now be 82 (9**2)+(1**2) then when we loop 
        # back around our remainder (82%10) will be 2 
        x = sum
    if x == 1:
        is_happy = True
    return is_happy

print(happy_numbers(19))

'''
Task 2: Prime Numbers
A prime number is a number that is only divisible by one and itself.
Write a method that prints out all prime numbers between 1 and 100 
'''

def prime_numbers(start, stop):

    for num in range(start, stop + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:    # divide by each index (starting at 2 bc index[1] is 0)
                    break           # if there is no remainder, don't print that number
            else:
                print(num)

# prime_numbers(1, 100)

def is_number_prime(num):

    is_prime = False

    if num == 1:
        is_prime == False
    elif num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            is_prime = True
    return is_prime

    # if num == 1:
    #     return False
    # elif num > 1:
    #     for i in range(2, num):
    #         if (num % i) == 0:
    #             return False
    #         else:
    #             return True

# print(is_number_prime(15))

def prime_numbers_w_function(start, stop):
    for num in range(start, stop +1):
        if is_number_prime(num) == True:
            print(num)

# prime_numbers_w_function(1, 100)

'''
Task 3: Fibonacci
A series of numbers in which each number (Fibonacci number) is the sum of the two 
preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
Write a method that does the Fibonacci sequence starting at 1

HARDER VERSION: Write a method that does the Fibonacci sequence starting at a 
number that a user inputs
'''

# The formula of the Fibonacci series
# xn=xn-1+ xn-2 (where 'n' is the term number)

def fibonacci(n):
    
    first = 0
    second = 1
    sequence = [0, 1]

    for num in range(2, n):
        third = first + second 
        sequence.append(third)
        first = second
        second = third 
    
    return sequence

# print(fibonacci(10))




   

