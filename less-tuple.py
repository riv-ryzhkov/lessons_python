# l1 = (1, 2, 3, 4, 99)
# l1 = range(10)
# t1 = (3)
# t2 = (3,)
# print(t1, type(t1))
# print(t2, type(t2))
# t1 += (44, 66)
# print(t1, id(t1))
# t2 = (5, 7, 8, 9, 8, 8, 8, 10)
# # print(t1 * 3)

# t1 = ('Hello,', 'world!')
# text1 = ' '.join(t1)
# print(text1, type(text1))
# print(t2.index(8))
# print(t2.count(888))




# l1 = [2, 3, 'yui', 8]
# print(l1, id(l1))
# l1.append(9999)
# print(l1, id(l1))
# ll = list(zip(l1, l1))
# print(ll, type(ll))
# print(ll[0], type(ll[0]))
# print(l1, type(l1))
# l1[0] = 99
# t1[4][0] = 99
# print(t1[0])
# print(t1, type(t1))
# print(l1, type(l1))




# t1 = (777, 567, 7898, 435, 777, 777)
# t1 = tuple(map(str, t1))
# print(t1)
# print('='.join(t1))
# print(t1)
# # del t1
# print(t1)

# print(t1, type(t1))
# # print(t1.count(777))
# # print(t1)
# l1 = list(t1)
# # print(l1, type(l1))
# l1.insert(3, 3333333)
# l1.sort()
# t1 = tuple(l1)
# print(t1, type(t1))
# # t2 = [8888]
# print(t1.count(777))
# print(t1.index(777, 1))
#
# t1 = tuple(map(str, t1))
#
# print(t1, type(t1))
# print('=>'.join(map(str, range(3, 10))))
# print(min(t1[1:3]))

# t1 = (1, 45, 'kjlk', (678, 89, 'ghjkh', [23, 67, 'hj']))
# t2 = (1, 45, 'kjlk', (678, 89, 'ghjkh', [23, 67, 'hj']))
# print(t1, type(t1), id(t1))
# print(t2, type(t2))
# t1 = (999,) + t1[1:]
# print(t1, id(t1))
# print(len(t1))


# t1 = ('Hello', ',', ' ', 'world', '!')




# print('->'.join(tuple(map(str, range(10)))))

# t1 = (1, 2, 3)

# del t1
# print(t1, id(t1))
#
# l1 = list(t1)
# l1.insert(1, 789)
# l1.pop()
# l1.sort(reverse=True)
# t1 = tuple(l1)
#
# print(t1, id(t1))



# t5 = tuple('Hello')
# print(t5, type(t5), len(t5))


# t1 = (1, '34', 'ghghj', (23, 78), 67, 'abc', '34')
# t2 = (1, '34', 'Hello', (23, 78), 67, 'abc')

# print(t1[:1] + (55,) + t1[1:])
# print(t1)
# print(t1.count('34'))

# print(t1, id(t1), id(t1[2]))
# t1[2].append('rrrrr')
# print(t1, id(t1), id(t1[2]))
# for i in t1:
#     print(i, id(i), sep='\t')


# str   неизменяемая последовательность символов
# list  изменяемая последовательность объектов
# tuple неизменяемая последовательность объектов







# print(t1, id(t1))
# l1 = list(t1)
# l1.append('Hello!')
# t1 = tuple(l1)
#
#
# print(t1, id(t1))



# # t1 = (8,) + t1[1:]
# print(t1, id(t1))
# # t1 = (9,) + t1[1:]
# t1[2].append(0)
# print(t1, id(t1), len(t1))







# a = 'Hello'
# print(a, type(a), id(a))


############ for list ###################
# a = [1, 'Hello', 5, 5, 5, [9, 5], (20, 3), 'abc']
# b = a
# print(a, id(a))
# print(b, id(b))
# b.pop(1)
# a.append(888)
# print(a, id(a))
# print(b, id(b))
# l = a.pop(5)
# a.append(l)
# print(a)
# print(l)



#
# print(id(a))
# # a.clear()
# a = ()
# print(id(a))

# b1 = tuple(i for i in range(5))
#
# print(a, type(a))
# print(b1, type(b1))
#
# print('\n< a + b >  ->', a + b1)
#
# print('\n< * 4 >  ->', a * 4)
#
# a = tuple(filter(lambda x: type(x) == str, a))
# print('\nfilter  ->', a, type(a))
#
# b = '='.join(a)
# print('\njoin ->  ', b, type(b))
#
# c = tuple(b)
# print('\ntuple ->', c, type(c))
#
# d = tuple(filter(lambda x: x.islower(), c))
# print('\nfilter, lambda, tuple   ->', d, type(d))
#
# print('\ncount  l -> ', d.count('l'))
#
# print(*tuple(zip(a, b)))
# print(*tuple(filter(str, a)))
# print(*tuple(map(lambda x: x**2, b1)))
#
# del d







# a = [1, 2, 3]
# b = a.copy()
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)
# print(id(a) == id(b))




#
# a = ('1', 'hfjh', 3)
#
# print(a.index('1'))

#   +   *     count     join     index


#
# n = ord('R')
# print(n)
# print(chr(n))
# print(bin(n))
# print(hex(n))
# print(oct(n))
#
#
# # a = (1, 2, 3)
# # print(a is a)
# #
# # # x = list(reversed(a))
# # x = list(zip(a, a))
# # print(a, x)
# # b = [7, 8, 9]
# # c = b
# # print(id(b))
# # print(id(c))
# # print(c == b)
# # print(c is b)
# #
# # print('='*50)


#
# a = input().split()
# print(sorted(list(map(lambda x: int(x)**2, a)), reverse=True))
#

# a = []
# print(*dir(a), sep='\n')

# a = [2, 4]
# # b = [2, 4]
# # print('a', id(a))
# # print('b', id(b))
# # print(a == b)
# # print(a is b)
# # print(id(a) == id(b))

a = ['abc', 'abd', 'AHGFJHHLKJJ:KLJLKJKL']
a1 = 'Hello'
a3 = range(10)

print(*list(zip(a, a1, a3)), sep='\n')
# print(max(a))
# print(min(a))
# a.sort()
# print(sorted(a))