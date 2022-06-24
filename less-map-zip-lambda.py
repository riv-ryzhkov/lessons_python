# map-zip-lambda-filter-sort
def sqr(x):
    return abs(int(x))


l1 = [2, '-3', -45, '67', '-99']
# print(l1)
# print(sqr(-4))

l2 = list(map(lambda x: abs(int(x)), l1))
# l2 = list(map(sqr, l1))
# l2 = list(map(sqr, [1, "2", -3, 5]))
# print(l2)



# l1 = list(map(lambda x: abs(int(x)) ** 2, l1))
# l2 = list(filter(lambda x: int(x) > 0, l1))
# print(l1)
# print(l2)

text = 'Hello, world!'
# l1 = list(text)
# l2 = list(range(10))
# l3 = list(zip(l2, l1))
# print(l1)
# print(l2)
# print(l3)
# print(list(enumerate(l1)))







l3 = [422, '373', 145, '867', '18899']

# l3 = list(map(int, l3))
# l3.sort(key=lambda x: int(x), reverse=True)
# l3.sort()
# # print(l1)
# print(l3)
# print(l3)

#
city = ['Dnepr', 'Kiev', 'Lviv', 'Odessa', 'Rivno']
population = [1000000, 4500000, 900000, 850000, 200000]
population = list(map(lambda x: int(x/1000), population))
# print(*population)
res = list(zip(city, population))
# res = list(zip(range(1, 30), city, population))
# print(*res)
res.sort(key=lambda x: x[1], reverse=True)
# print(*res)
res = list(filter(lambda x: x[1] > 250, res))
# print(*res)
# print(*res, sep='\n')
# for i in res:
#     print(*i, sep='\t')




l1 = list(map(lambda x: (int(x)+2) ** 2, l1))
# l2 = list(filter(lambda x: type(x) == str, l1))
l2 = list(filter(str, l1))
# print(l1)
# print(l2)
# print(max(l1))





# l1 = [1, 2, 3, 4, 5]
# l2 = [chr(i) for i in range(97, 108)]
# print(l1)
# print(l2)









# l1 = 'Hello uoiuyiuypoiuoiu oiu ouoiu'
# l2 = list(zip(range(len(l1)), list(l1)))
# print(*l2)
#
# print(*list(enumerate(l1)))

# def sqr(x):
#     return int(x) ** 2

# l1 = [2, '3', 45, '67', '99']
#
# # l1 = list(map(lambda x: int(x) ** 2, l1))
# # print(list(map(lambda x: int(x) ** 2, l1)))
# l1 = list(filter(lambda x: int(x) > 40, l1))
# print(l1)






# def sqr(x: str):
#     return int(x) ** 2
#
# l1 = [2, '3', 45, '67', '999']

# l2 = list(map(sqr, l1))
# l2 = list(map(lambda x: int(x) ** 2, l1))
# l2 = list(filter(lambda x: int(x) > 40, l1))
# print(l1)
# print(l2)
# print(max(l2))







# l1 = list(map(int, l1))
# print(l1)
# print(max(l1))
#
#
# def foo(x):
#     return int(x) ** 2
#
# print(list(map(foo, l1)))

########## lambda





# l1 = [1, '2', 3, 4, '5', '6']
# print(l1)
#
# l3 = list(filter(lambda x: int(x) > 3, l1))
# print(l3)
#
# print(list(map(lambda x: int(x) > 3, l1)))




l1 = ['Dnepr', 'Kiev', 'Lviv', 'Odessa']
l2 = [10000000, '4500000', 900000, '88888', 55555, 44444, 99996766]
l2 = list(map(int, l2))
l3 = list(zip(l1, l2))
# print(l3)
# l3.sort(key=lambda x: x[1], reverse=True)
# print(list(filter(lambda x: x[1] > 800000, l3)))
# print(*l3)
# for i in l3:
#     print(*i, sep='\t')





# l3 = list(zip(l1, l2))
# print(l3)
# # l3 = list(filter(lambda x: x[1] >= 1000000, l3))
# l3.sort(key=lambda x: x[1], reverse=True)
# print(*l3, sep='\n')




# n = input('name = ')
# print(*list(filter(lambda x: x[0] == n, l3)))
# l3.sort(key=lambda x: x[1], reverse=True)
# for i in l3:
#     print(*i, sep='\t')










# l3 = ['a', 'b']
# l2 = [str(i) + '->' + str(k) for i in range(1, 10) if i > 4 for k in l1]
# print(*l1)
# print(*l2, sep='   ')






def foo(x):
    return int(x) ** 2


l1 = [2, '3', 5, '8', '9']
l1 = list(map(lambda x: int(x) ** 2 + 789, l1))
# print(l1)








# def sqr(x):
#     return x**2



# l1 = ['a', 'b', 'c', 'd']
# l1 = [i for i in range(9)]
# l1 = list(range(10))
# l2 = list(range(15))
# l2 = list(map(lambda x: x**3, l1))
# l2 = list(filter(lambda x: x % 2 == 0, l1))
# l3 = list(zip(l2, l1))
# print(l1)
# print(l2)



# print(*l3)


# l1 = [i for i in range(10, 50)]
#
# print(list(map(lambda x: x**3, l1)))
# print(l2)
# l2 = []
# for i in l1:
#     l2.append(i**3)
# l2 = list(filter(lambda x: x % 2, l1))
# print(l1)
# print(l2)
#
#
# print(list(filter(lambda x: x % 2, l1)))








# base_numbers = [2, 3, -4, -5, 0, 8, 10, 12, 14, 16]
# print(list(filter(lambda x: x % 2 == 0, base_numbers)))
# print(list(filter(None, base_numbers)))
# powers = [1, 2, 3, 4, 5]
#
# numbers_powers = list(map(pow, base_numbers, powers))
# #
# print(numbers_powers)
#
# z = list(zip(base_numbers, powers))
# z = zip(base_numbers, powers)
#
# print(list(z))
# print(list(z))
# print(list(z))

# for k, n in zip(base_numbers, powers):
#     print(k, '**', n, '=', k**n)



# a = [1, 3, 5, 7]
# print(a)
# b = list(map(lambda x: x**2, a))
# print(b)
# c = list(zip(a, b))
# for k, l in c:
#     print(k, '*', k, '=', l)

