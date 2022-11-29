def sq(n, p, x):
    if abs((x * x) - n) < p:
        return x
    else:
        return sq(x, p, (.5 * (x + n / x)))


import math


def main():
    n = input('give a number\n')
    n = int(n)
    x = math.sqrt(n)
    p = 1

    print(sq(n, p, x))


if __name__ == '__main__':
    main()
