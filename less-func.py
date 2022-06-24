# a = '5'
# b = '5'
# print(eval(a, b))

# S = input('ведите рост учеников через пробелы').split()
# Petr = int(input('введите рост Пети'))
# Index = 0
# while Index < len(S) and int(S[Index]) >= Petr:
#     Index += 1
# print(Index + 1)
# S = S[:Index] + [str(Petr)] + S[Index:]
#
# # S.insert(Index, Petr)
# print(*S)








def function1(a, b):
    c = a + b
    return c


def dr(a):
    print('*' * a)


def pi_():
    print('=' * 80)


def sum1(a, b=0, c=0, d=0, e=0):
    return a + b + 2*c + d + e


# print(sum1(6, c=7, d=9))


def sum2(*args):
    res = 0
    # print(type(args), args)
    for i in args:
        res += i
    return res


# print(sum2(5, 6, 8, 9, 9, 0, 4, 6, 7, 9))


def foo():
    b = a
    print(a)
    b += 5
    return b


# a = 9
# # a = foo()
# print(a)


# print(sum2(3, 2, 5, 7, 8, 9, 34, 87))


# print(pi_())
# print(function1(2, 5))
# print(pr(9))















a = 5

def foo(b=2):
    # global a
    a = 10
    return a

# foo()
# print(a)




# def sum(*x):
#     print('Купи калькулятор!')



# print(sum(56, 67, 89)
# b = foo(3)



# def prn(n):
#     print('=' * n)

# def sum3(a, b, c):
#     return a * b + c
#
# def max2(a, b):
#     if a >= b:
#         return a
#     else:
#         return b
#
#
# def max3(a, b=10, c=-15):
#     if c >= max2(a, b):
#         return c
#     else:
#         return max2(a, b)
#
#
# def sum_(*args):
#     res = 0
#     for i in args:
#         res += int(i)
#     return res
#
#
# print(sum_(23, 45, '678', '23454'))

#
# def max2(a, b):
#     if a >= b:
#         return a
#     else:
#         return b
#
#
# def max3(a, b, c):
#     if c >= max2(a, b):
#         return c
#     else:
#         return max2(a, b)
#
#
# def sum_(*args):
#     res = 0
#     for i in args:
#         res += int(i)
#     return res
#

# print(sum_(45, 67, 9, 46, 4))











#
# def max_(a, b):
#     if a >= b:
#         return a
#     else:
#         return b
#
#
# def max3(a, b, c):
#     if c >= max_(a, b):
#         return c
#     else:
#         return max_(a, b)
#
#
# def sum_(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# def maxx(*args):
#     res = args[0]
#     for i in args[1:]:
#         if i > res:
#             res = i
#     return res
#
# print(maxx(23, 45, 78, 89, 56, 23, -34, 34))


# print(sum_(23, 56, 78, -89, 234, 88, 67, 45))


# print(max3(104, 90, 17))






# i = 5
# print(i)
#
# def foo():
#     # global i
#     i = 10
#     print('*' * i)
#     return i
#
# foo()
# print(i)


# def prn(n, y, k=2, n1=67, m=0):
#     print('***' * n * y)
#     return n**k
#
#
# res = prn(5, 2)
# print(res)

# def max_(*args):
#     res = args[0]
#     for i in args[1:]:
#         if i > res:
#             res = i
#     return res
#
#
# print(max_(23, 45, 23, 12))


# def max2(a, b):
#     if a >= b:
#         return a
#     else:
#         return b
#
# def max3(a, b: int, c=0, d=3, h=8):
#     print(a * b)
#     return a, b, c



# a1, x, y = max3(2, 6, 9)
# print(a1, x, y)










# def prn(n: int, sym: str, a=0):
#     print(sym * n, a)
#     return n**2
#
#
# print(prn(44, '='))

# def max_(a, b):
#     if a >= b:
#         return a
#     else:
#         return b
#
#
# def max3(a, b, c):
#     if c >= max_(a, b):
#         return c
#     else:
#         return max_(a, b)
#
#
# print(max_(12, max_(55, 99)))
# print(max3(12, 55, 99))
# print(max_(120, 67))

# def sum_(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(sum_(23, 45, 6768, 565, 34, -5766))
#

# i = 10
# print(i)
#
# def foo():
#     # global i
#     i = 9
#     print(i)
#     return i








# def prn(x: int, y: int, symbol: str, b=8, c='+'):
#     print(symbol * x)
#     print(c * int(y))
#     return 'x = ' + str(x)


# prn(3, 5, 9)


#
# def sqr(n):
#     return n**(1/2)
#
#
# print(sqr(81))
#
#
# a = prn(10, 5)
# print(a)
# a = prn(20, 7)
# print(a)
#




# def prn(x, y):
#     print(x, '! =', y)
#
# 5! = 1 * 2 * 3 * 4 * 5

def factorial(n: int):
    res = 1
    for i in range(1, n + 1):
        res *= i
    print(n, '! = ', res)
    return res

# factorial(5)
# print(factorial(5))

#
# factorial(7)
# factorial(9)
# factorial(3)
# #
# #
# #
# for i in range(1, int(input('n = '))+1):
#     factorial(i)

#
#
# for i in range(1, int(input('n = '))+1):
#     factorial(i)

#
#
# for i in range(1, 9):
#     factorial(i)



# a = factorial(5)
# print(a)

#
# sum_ = factorial(int(input('1st = ')))\
#        + factorial(int(input('2nd = ')))\
#        + factorial(int(input('3d = ')))
# print('=========', sum_)

# def max_(a, b):
#     if a >= b:
#         return a
#     else:
#         return b
#
#
# def max3_(a, b, c):
#     if c >= max_(a, b):
#         return c
#     else:
#         return max_(a, b)
#
# print(max_(3, 9))
# print(max3_(18, 3, 9))


# def foo(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res


# print(foo(3, 5, 7, 22, 77, -45))
#
# a = 2
#
# def foo(n):
#     # global a
#     aaaa = 100
#     res = aaaa * n
#     print(aaaa)
#     return aaaa, res
#
#
# print(a)
# a, res = foo(5)
# print(a)
#
# foo(8)



# def foo(a, b, c=1):
#     res = (a + b) * c
#     return res, a, b, c
#
# print(foo(2, 3))
# print(foo(2, 3, 4))
# print(foo(c=2, a=3, b=4))
# # print(foo(1))
# a, b, c, d = foo(c=2, a=3, b=4)
# print(a, b, c, d)




# def foo(*args):
#     return args
#
# print(foo(3, 6, 898, 'abc'))




# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res
#
# print(factorial(3))
# print(factorial(5))






# def max_(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     elif c >= a and c >= b:
#         return c
#
# print(max_(13, 5, 100))

#
# def max_(*a):
#     res = a[0]
#     for val in a:
#         if val > res:
#             res = val
#     return res
# #
# print(max_(3, 5, 4, 7, 23, -1000))




# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res
#
# for i in range(1, 6):
#     print(i, '! = ', factorial(i), sep='')



# def foo(n):
#     # global a
#     a = n
#     print('a =', a, '\t b =', b)
#
#
# a = 9999
# b = 333
# foo(44444)
# print('a =', a, '\t b =', b)


# def factorial(n):
#     res = 1
#     for i in range(2, n + 1):
#         res *= i
#     return res
#
# n = int(input())
# f = factorial(n)
#

def func1(a, b):

    def inner_func(x):
        return x*x*x

    return inner_func(a) + inner_func(b)


# print(func1(3, 4))
#
# print(inner_func(5))

#
def short_story():
    print("У попа была собака, он ее любил.")
    print("Она съела кусок мяса, он ее убил,")
    print("В землю закопал и надпись написал:")
    short_story()


# short_story()


#
# def factorial(n):
#     print('n = ', n)
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# n = int(input('n = '))
# print('factorial', n, '! =', factorial(n))


# !!!!!!!!!!!!!!!! reverse!!!!!
# res = []
# x = 'abc'
# while x:
#     x = int(input('x = '))
#     res.append(x)
# for i in range(1, len(res)):
#     print(res[len(res)-1-i])




def reverse():
    symbol = int(input('= '))
    if symbol:
        reverse()
    print(symbol)


# reverse()




# Change name !!!!!!!!!!!!!!
# def pwr(x, n):
#     return x ** n
#
#
# print(pwr(2, 3))
# power = pwr
# print(power(2, 3))
# print(pwr(2, 3))


# power = lambda x=1, y=2: x**y
# print(power(4))