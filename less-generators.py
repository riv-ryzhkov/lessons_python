# ########### GENERATORS LIST-TUPLE-SET-DICT #############

list1 = [chr(i) for i in range(97, 110)]
tuple1 = tuple(i for i in range(15, 0, -1))
set1 = {chr(i) for i in range(97, 110)}
dict1 = {x: y for x, y in zip(set1, tuple1)}


gen = (i for i in range(15, 0, -1))
# s = sum(i for i in range(10000) if i%2)
# print(s)
# print('gen:', type(gen))
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(list(gen))
# print(tuple(gen))
# print(next(gen))


# print('list1: ', type(list1))
# print(list1)
# print()
# print('tuple1: ', type(tuple1))
# print(tuple1)
# print()
# print('set1: ', type(set1))
# print(set1)
# print()
# print('dict1: ', type(dict1))
# print(dict1)
# print()









# dic_res = list(dict1.items())
# dic_res.sort(key=lambda x: x[1], reverse=True)
# for i in dic_res:
#     print(*i, sep='\t')


# ########## Generator on base of Factorial ###########
def factorial(n: int):
    res = i = 1
    while i <= n:
        res *= i
        i += 1
        yield res
        # yield res
        # yield res
    # return res # 1*2*3*4

# print(factorial(5))

# fact = factorial(7)

# print(fact, type(fact))
# print(next(fact))
# print(next(fact))
# print(next(fact))

# print(list(fact))
# print(list(fact))

fact = factorial(9)
# print(list(fact))
# print(next(fact))
# print(next(fact))
# fact = factorial(7)
# print(fact, type(fact))
# print(next(fact))
# print(next(fact))
# print(next(fact))
# # # #
# # # #
# print(fact)
# print('1: ', next(fact))
# print('2: ', next(fact))
# print('3: ', next(fact))
# print('4: ', next(fact))
# print('5: ', next(fact))
# print('6: ', next(fact))
# fact1 = list(fact)
# print('fact1 = ', fact1, type(fact1))
fact = factorial(7)
# fact2 = list(fact)
# print('fact2 = ', fact2, type(fact2))
# ###################################################

# n = 7
# fact = factorial(n)
# for i in range(1, n):
#     print(i, '! =', next(fact))


# #################################################

# n = 10
# fact = factorial(n)
# l5 = []
# for i in range(1, n - 3):
#     l5.append(next(fact))
# l6 = list(fact)
# print(l5)
# print(l6)
# fact = factorial(n)
# print(next(fact))
# f = factorial(n)
# print(id(fact), list(fact))
# print(id(f), list(f))
# f = factorial(n)
# print(list(f))
# ###########################################
#
# def fibonacci(xterms):
#     # первые два условия
#     x1 = 0
#     x2 = 1
#     count = 0
#     if xterms <= 0:
#         print("Укажите целое число больше 0")
#     elif xterms == 1:
#         print("Последовательность Фибоначчи до", xterms, ":")
#         print(x1)
#     else:
#         while count < xterms:
#             xth = x1 + x2
#             x1 = x2
#             x2 = xth
#             count += 1
#             yield xth
#
# n = 7
# fib = fibonacci(n)
#
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(fibonacci(n))
# print(next(fibonacci(3)))
# print(next(fibonacci(5)))
# print(next(fibonacci(9)))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# #############################################
#  GENERATORS : MAP-ZIP-ENUMERATE  RANGE #

l1 = [str(i) for i in range(10)]
# print(l1)
m = map(int, l1)
# print(m, type(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(tuple(m))
# print(list(m))


z = zip(l1, l1)
# print(next(z))
# print(next(z))
# print(next(z))
# print(next(z))
# print(list(z))

e = enumerate(l1)
# print(next(e))
# print(next(e))
# print(next(e))
# print(next(e))
# print(list(e))

r = range(10)
# print(next(r))
# print(next(r))
# print(next(r))
# print(list(r))


d = dict1.items()
# print(next(d))
# print(next(d))
# print(next(d))
# print(list(d))


###################
import sys


# print('m : ', sys.getsizeof(m), m)
# print('z : ', sys.getsizeof(z), z)
# print('e : ', sys.getsizeof(e), e)
# print('r : ', sys.getsizeof(r), r)
# #########################



# # ############# GENERATORS ####################
# ### сравним размеры объеков и скорость доступа ################
# import sys
# import time
#
#
# n = 1000000
# start = time.time()
# g = (i * 2 for i in range(n))
# print('Memory of generator =', sys.getsizeof(g))
# print('time of creating GENERATOR = ', time.time() - start)
# print()
#
# start = time.time()
# l = [i * 2 for i in range(n)]
# print('Memory of list = ', sys.getsizeof(l))
# print('time of creating LIST = ', time.time() - start)
#
#
# start = time.time()
# i = next(g)
# print()
# print('time of "NEXT" = ', time.time() - start)
# print()
#
# start = time.time()
# h = l[0]
# print()
# print('time of "L[0]" = ', time.time() - start)
# print()
#
# start = time.time()
# for i in g:
#     h = i
# print()
# print('time of "ALL GENERATOR" = ', time.time() - start)
#
# start = time.time()
# for i in l:
#     h = i
# print()
# print('time of "i in L" = ', time.time() - start)
#
#
# start = time.time()
# for i in range(len(l)):
#     h = l[i]
# print()
# print('time of "RANGE(LEN(L))" = ', time.time() - start)

# ##########################################################################
#
#
# def restart_gen():
#     return (i**2 for i in range(n))
#
# gen = (i**2 for i in range(n))
# # g = gen
# # print(g)
# print(gen)
# # print(gen, '---', type(gen))
# print(next(gen), '===')
# print(next(gen), '===')
# print(next(gen), '===')
# print(next(gen), '===')
# # l = list(map(lambda x: x, gen))
# # print(l)
# g = restart_gen()
# print(g, type(g))
# for i in g:
#     print(i, '!!!!!!!!')
#
#
#
# def gen():
#     i = 0
#     while True:
#         val = yield i
#         if val == 'restart':
#             i = 0
#         else:
#             i += 1
#
# g = gen()
# next(g)
# print(next(g))
# print(next(g))
# g.send('restart')
# print(next(g))
# print(next(g))
# print(next(g))
# ############################# Ganerators ZIP, MAP, ENUMERATE and RANGE ########
# base_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
# powers = [1, 2, 3, 4, 5]
# z = list(zip(base_numbers, powers))
# z = zip(base_numbers, powers)
# e = enumerate('Hello, world!')
# m = map(str, range(1, n))
# r = range(1, n) # Выдает всю последовательность сразу и много раз!!!!
#
# print('z: ', list(next(z)))
# print('z: ', list(next(z)))
# print('z: ', list(z))
# print('z: ', list(z))
# print('z: ', list(z))
# print('z: ', list(z))
# print('e: ', next(e))
# print('e: ', next(e))
# print('e: ', next(e))
# print('e: ', list(e))
# print('e: ', list(e))
# print('e: ', list(e))
# print('m: ', next(m))
# print('m: ', next(m))
# print('m: ', next(m))
# print('m: ', list(m))
# print('m: ', list(m))
# print('m: ', list(m))
# print('r: ', r)
# # print('r: ', next(r)) # ОШИБКА!!!!
# print('r: ', list(r))
# print('r: ', list(r))
# print('r: ', list(r))