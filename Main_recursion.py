def get_summation(n):
    if n == 0:
        return 0
    elif n > 0:
        return n + get_summation(n - 1)
def get_powers(a,n):
    if n > 0:
        return a * get_powers(a,n-1)
    elif n == 0:
        return 1
def get_sum_of_numers_digits(n):
    if n < 10:
        return n
    elif n == 10:
        return 1
    elif n > 10:
        return n%10 + get_sum_of_numers_digits(n/10)
def get_factorial(n):
    if n == 1:
        return n
    else:
        return n * get_factorial(n - 1)
def get_fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return get_fibonacci(n - 1) + get_fibonacci(n - 2)
def GCD(x, y):                                                                                                          #calling the function
    if y <= x and (x % y) == 0:                                                                                         #conditional one, % means
        return y                                                                                                        #return the y statement
    else:
        return GCD(y, (x % y))                                                                                       #translated statement
def get_compound_interest_balance(p, r, t):
    # formula for compound interest
    amount = p * (pow((1 + (r / 100)), t))

    # how compound interest is made

    CI = amount - p

    return CI
def P(a, b):
    if b > 0:
       return a + P(a,(b-1))
    else:
       return 0
def sq(n, p, x):
    if abs((x * x) - n) < p:
        return x
    else:
        return sq(x, p, (.5 * (x + n / x)))


import math
def main():
    print("Funciton list:\n summation\n powers\n sum of number's digits\n factorial\n fibonacci\n GCD\n compound interest\n Product of 2 whole numbers\n Square root")

    type = input('what recursion function do you wish to use')

    if type == "summation":
        n = int(input('please give 1 numbers'))
        print(get_summation(n))

    elif type == "powers":
        a = int(input('please give a base number'))
        n = int(input('please give the exponent you ish to raise the base to'))

        print(get_powers(a,n))

    elif type == "sum of number's digits":
        n = int(input('please give a number 10 or over'))
        n = (get_sum_of_numers_digits(n))
        n = str(n)
        n = n.split('.')
        print(n[0])

    elif type == "factorial":
        n = int(input('please give up to 1 numbers'))
        print(get_factorial(n))

    elif type == "fibonacci":
        n = int(input('please give 1 numbers'))
        print(get_fibonacci(n))

    elif type == "GCD":
        x = int(input('please give the first number number'))
        y = int(input('please give the second number'))
        print(GCD(x,y))

    elif type == "compound interest":
        p = float(input("Enter Principal Amount: "))
        r = float(input("Enter Rate of Interest: "))
        t = float(input("Enter Time Period in years: "))

        print("Compound interest is", get_compound_interest_balance(p, r, t))

    elif type == "Product of 2 whole numbers":
        a = input('give a number')
        b = input('give another number')
        a = int(a)
        b = int(b)
        print(P(a, b))

    elif type == "Square root":
        n = input('give a number\n')
        n = int(n)
        x = math.sqrt(n)
        p = 1

        print(sq(n, p, x))

    else:
        print("you did not enter a proper function")
        return main()


if __name__ == '__main__':
        main()