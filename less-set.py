

# изменяемый неупорядоченный набор неповторяющихся объектов



# НЕизменяемые :
"""
1. Int
2. Float
3. Boolean
4. Tuple
5. String
a = b  создается НОВЫЙ объект а!
"""
# a = (1, 2, 3)
# b = a
# a += a
# print(a, id(a))
# print(b, id(b))
# print(a, b)



# Изменяемые :
"""
1. List
2. Set
a = b создается ПСЕВДОНИМ того же самого объекта!
"""
# # a = {1, 2, 3, 3, 5, 4, 2, 1, 1, 1, 1, 3}
# text = input(': ')
# print(len(text))
# print(len(set(text)))
# a = set(range(5))
# print(a, type(a))
# b = a
# a.add(77777)
# print(a, id(a))
# print(b, id(b))
# print(a, b)

s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}
# print('s1 =', s1, type(s1), id(s1))
# print('s2 =', s2, type(s2), id(s2))
# s3 = s1 | s2
# s3 = s1.union(s2)
# print('s3 =', s3, type(s3), id(s3))
# s1 = s1 | s2
# s1 |= s2
# s1.update(s2)

# s1 = s1 & s2
# s1 = s1.intersection(s2)
# s1.intersection(s2)
# s1.difference_update(s2)
# s1 -= s2
# s3 = s1.symmetric_difference(s2)
# s1.symmetric_difference_update(s2)
# s1 = s1 ^ s2
# s1 |= s2
# print('s1 =', s1, type(s1), id(s1))
# print('s2 =', s2, type(s2), id(s2))
# print(s1.issuperset(s2))
# print(s1.issubset(s2))
# print(s1.issuperset(s1))
# print(s1 > s1)
# print('s3 =', s3, type(s3), id(s3))
# print(44 in s1)
# print(44 in range(22, 55))
# s2.difference_update(s1)
# print(s1.isdisjoint(s2))
# s3 = s1.copy()
s3 = set(s1)
s3.add('ss')
# print('s3 =', s3, type(s3), id(s3))
# print('s1 =', s1, type(s1), id(s1))
# s1 = list(s1)
# print(s1[0])
# s1 = set(s1)
# s1.remove(22)
# s1.pop()
# print(s1.pop())
# s1.discard(3333)
# s1 = frozenset(s1)
# s1.clear()
# s1 = set()
# print('s1 =', s1, type(s1), id(s1))



# s1.discard(int(input('symbol = ')))
# if symbol in s1:
#     s1.remove(symbol)
# else:
#     print('No symbol', symbol, 'in s1!!!!')
# s1.clear()
# print('s1 =', s1, type(s1), id(s1))
# s1 = set()
# print('s1 =', s1, type(s1), id(s1))












# print('s1 = ', s1, id(s1))
# print('s2 = ', s2, id(s2))
# s3 = s1.copy()
# s3 = set(s1)
# print('s3 = ', s3, id(s3))
# symbol = int(input('symbol = '))
# s4 = s3.pop()
# print(s4)
# s3.discard(symbol)
# if symbol in s3:
#     s3.remove(symbol)
# else:
#     print('No symbol', symbol, 'in s3!!!')

# print('s1 = ', s1, id(s1))
# print('s3 = ', s3, id(s3))
# s3.clear()
# s3 = set()
# print('s3 = ', s3, id(s3))


# s3 = s1.union(s2)
# s3 = s1 | s2
# s1.update(s2)
# s1 |= s2
# s3 = s1.intersection(s2)
# s1.intersection_update(s2)
# s3 = s1 & s2
# s1 &= s2
# s3 = s1.difference(s2)
# s1.difference_update(s2)
# s3 = s2.symmetric_difference(s1)
# s1.symmetric_difference_update(s2)
# print('s3 = ', s3, id(s3))
# print('s1 = ', s1, id(s1))

# print(s3.isdisjoint(s1))
# print(s2 > s1)
# print(s2.issuperset(s1))
# print(s1 < s2)
# print(s1.issubset(s2))




# print(s1, type(s1))
# print(s3, type(s3))
# LIFO







# print('s1=', s1, id(s1))
# # symbol = int(input('symbol = '))
# # s1.discard(symbol)
# s1.clear()
# print('s1=', s1, id(s1))
# s1 = set(range(2, 8))
# print('s1=', s1, id(s1), type(s1))

# s3 = s1
# s3 = s1.copy()
# s3 = set(s1)
# s2 = {4, 5, 6, 7, 8, 9}
# print('s1=', s1, id(s1))
# print('s3=', s3, id(s3))
# print(s1.issuperset(s2))
# print(s1 == s2)
# s1.add(0)
# print('s1=', s1, id(s1))
# print('s3=', s3, id(s3))

# text = 'Hello, world!'
# print(list(text))
# print(tuple(text))
# print(set(text))


# s3 = s1.union(s2)
# s3 = s1 | s2
# s1.update(s2)
# s1 |= s2  # s1 = s1.union(s2)
# s3 = s1.intersection(s2)
# s3 = s1 & s2
# s1.intersection_update(s2)
# s1 &= s2
# s3 = s1.difference(s2)
# s3 = s2 - s1
# s1.difference_update(s2)
# s1 -= s2
# s3 = s1.symmetric_difference(s2)
# s3 = s1 ^ s2
# s1.symmetric_difference_update(s2)
# s1 ^= s2

# print('s1=', s1, id(s1))
# print('s2=', s2, id(s2))
# print('s3=', s3, id(s3))










# s1 = set(range(4, 10))
# s2 = {1, 2, 3, 4, 5, 6}
# s3 = {1, 2, 3, 4, 5, 6, 7, 8}
# print(s1, type(s1), id(s1))
# # s4 = s1.copy()
# # s4 = set(s1)
# # print(s4, id(s4))
#
# a = s1.pop()
# print(s1, id(s1))
# print(a)
# # s1.clear()
# # s1 = set()
# # del s1
# print(s1, id(s1))
# # print(s4, id(s4))

# text = 'Hello, world!'
# print(list(text))
# print(tuple(text))
# print(set(text))









# s1 = set('Hello')
# s2 = set(range(3, 9))
# print(s1, type(s1), id(s1))
# print(s2)
# # s3 = s1.symmetric_difference(s2)
# s3 = s1 ^ s2
# # s1.symmetric_difference_update(s2)
# s1 ^= s2
# print(s3, id(s3))
# print(s1, id(s1))

# s1 = {1, 2, 3, 4}
# s2 = {1, 2, 3, 4, 5}
# print(s2, id(s2))
# # symbol = int(input('symb = '))
# # s2.clear()
# s2 = set()
# if symbol in s2:
#     s2.remove(symbol)
# else:
#     print('No symbol!')
# print(s2, id(s2))
# s1.add(8)
# print(4 in s1)
# print(s1.update(s1))
# sss = s1
# sss = s1.copy()
# sss = set(s1)
# s2 = sss.pop()
# print('s1 = ', s1, id(s1))
# print('sss = ', sss, id(sss))
# print(s2)

# s1.clear()
# # s1 = set()
# print(s1, id(s1))
# # print('sss = ', sss, id(sss))
# print(s1 > s2)
# print(s1, id(s1))
# print(sss, id(sss))
# print(s2)
# s1.intersection_update(s2)
# s1 &= s2
# s1.symmetric_difference_update(s2)
# print(s1)


# # s1 = s1.union(s2)
# s3 = s1 | s2
# # s1.update(s2)
# print(s1, id(s1))
# print(sss, id(sss))




text = '''
While The Python Language Reference describes the exact syntax and semantics of the Python language, this library reference manual describes the standard library that is distributed with Python. It also describes some of the optional components that are commonly included in Python distributions.

Python’s standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.

The Python installers for the Windows platform usually include the entire standard library and often also include many additional components. For Unix-like operating systems Python is normally provided as a collection of packages, so it may be necessary to use the packaging tools provided with the operating system to obtain some or all of the optional components.

In addition to the standard library, there is a growing collection of several thousand components (from individual programs and modules to packages and entire application development frameworks), available from the Python Package Index.
'''

l1 = text.split()
# print(len(l1))
# print(l1)

lll = set(text.split())
# print(len(lll))
# print(lll)




# list1 = [1, 2, 3, 4, 1, 2, 3, 3, 2, 3]
# list1 = list(set(list1))
# print(list1)
# print(len(list1))


# print(len(lll))
#
# lll.sort()
# print(*lll)
#
#
#
l1 = text
l2 = []
for i in l1:
    if i.isalpha() or i == ' ' or i == '’' or i == '-' or i == '\n':
        l2.append(i.lower())
text = ''.join(l2)
print(text)
print(len(text.split()))
print(len(set(text.split())))
# #
res = []
list_text = list(set(text.split()))
print(list_text)
for i in list_text:
    res.append((i, text.count(i)))
print(res)
res.sort(key=lambda x: x[1], reverse=True)
for i in res:
    print(*i, sep='\t')


# l1 = [45, 12, 2, 3, 3, 4, 12, 12, 78, 56,]
# a = set(l1)
# b = {i for i in range(5)}
# print(a, type(a))
# print(b, type(b))
# # a.update(b)
# # a = a | b
# # a.difference_update(b)
# # a &= b
# # a -= b
# # a.symmetric_difference_update(b)
# a ^= b
# # print(a)
# # a.difference_update(b)
# print(a)
# a.add(89809809)
# print(a, id(a))
# # a.remove(0)
# # a.discard(9999)
# # l1 = 'Hello'
# # print('e' in l1)
# k = a.pop()
# print(a)
# print(k)
# # a.clear()
# a = set()
# print(a, id(a))


# изменяемое неупорядоченное множество неповторяющихся объектов
# print(a, len(a), type(a), id(a))
# a.add('99')
# print(a, len(a), type(a), id(a))



# set_text = set(text.split())
# print(len(set_text), len(text.split()), set_text)
# a.add(9)
# a.clear()
#
# print(a, b)
# print(a)


# s1 = frozenset(range(8))
# # s2 = frozenset(range(4, 10))
# print(s1, type(s1), id(s1))
# # print(s2, type(s2))
# # s3 = s1.union(s2)
# # print(s3, type(s3))
# s1 = set(s1)
# # print(s1, type(s1), id(s1))
# s1.add(9999)
# s1 = frozenset(s1)
# print(s1, id(s1))




text = '''
Get job-ready skills and be ready to work in SoftServe with Python Online Marathon from IT Academy.
Python Online Marathon is for you to convert theory into skills letting you create solutions or even new products. Join it to test your knowledge, or prove yourself that you are ready for more.
'''
# text = text.split()
# print(len(text), type(text), text)
# words = set(text)
# print(len(words), type(words), words)
# res = []
# for i in words:
#     res.append([i, text.count(i)])
# print(*res)
# res.sort(key=lambda x: x[1], reverse=True)
# # print(*res)
# for i in res:
#     print(*i, sep='\t')







# a = {'gkj', 'asd', 576, 23.45, 2, 2, 2, 'asd'}
# b = {'asd', 576, 0, 2, 2, 2, 'asd', 'bbbbb'}
# # a = {'asd', 576, 0, 2, 2, 2, 'asd', 'bbbbb'}
# # b = frozenset(a)
# print(type(a))
# print(*b)
# a = frozenset([2, 3, 4, 5, 6, 6, 6])
# print(a)
# a = set(a)
# a.add(99)
# a = frozenset(a)
# print((a))


# print(*a)
# print(*b)













# txt = '''
# While The Python Language Reference describes the exact syntax and semantics of the Python language, this library reference manual describes the standard library that is distributed with Python. It also describes some of the optional components that are commonly included in Python distributions.
#
# Python’s standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.
#
# The Python installers for the Windows platform usually include the entire standard library and often also include many additional components. For Unix-like operating systems Python is normally provided as a collection of packages, so it may be necessary to use the packaging tools provided with the operating system to obtain some or all of the optional components.
#
# In addition to the standard library, there is a growing collection of several thousand components (from individual programs and modules to packages and entire application development frameworks), available from the Python Package Index.
#
# '''
# a = txt.split()
# print(len(a))
# print(a)
# s = set(a)
# print(len(s))
# print(s)
# print(a.count('the'))





# lst = []
# for i in s:
#     lst.append((i, a.count(i)))
# print(lst)
# lst.sort(key=lambda x: x[1], reverse=True)
# for i in lst:
#     print(*i)




# a = {1, 2, 3, 4}
#
# b = frozenset(a)
# b.add(9)
# print(a)
# b = a
# b = a.copy()
# b.add(8)
# print(a, b)
# a.pop()
# b.pop()
# print(a, b)
# a.discard(5)
# a.remove(5)


#### ЗАДАЧА - Угадай число-2##################
# num_list = set(str(x) for x in range(1, int(input('n = '))+1))
# while True:
#     beatr = set(input().split())
#     if 'HELP' in beatr:
#         break
#     if len(beatr & num_list) > len(num_list - beatr):
#         print('YES')
#         num_list &= beatr
#     else:
#         print('NO')
#         num_list -= beatr
# num_list = list(map(int, num_list))
# print(' '.join([str(x) for x in sorted(num_list)]))
##################################################

########## задача ПОЛИГЛОТЫ#############
# n = [[] for i in range(int(input('к-во шк = ')))]
# for i in range(len(n)):
#     n[i] = [int(input('к-во яз = '))]
#     for j in range(1, n[i][0]+1):
#         n[i] += [input('яз = ')]
# all_lang = set()
# all_pup = set()
# for i in range(len(n)):
#     all_lang = all_lang | set(n[i][1:])
# for i in range(len(n)):
#     all_pup = all_lang & set(n[i][1:])
# all_pup = list(sorted(all_pup))
# print(len(all_pup), *all_pup, sep='\n')
# # for i in all_pup:
# #     print(i)
# all_lang = list(sorted(all_lang))
# print(len(all_lang), *all_lang, sep='\n')
# # for i in all_lang:
# #     print(i)
################################# ЗАДАЧА ДЗ ####################

# students = [{input('Language = ') for j in range(int(input('Number of languages = ')))} for i in range(int(input('Number of students = ')))]
# everyone, someone = set.intersection(*students), set.union(*students)
# print(len(everyone), *sorted(everyone), sep='\n')
# print(len(someone), *sorted(someone), sep='\n')
########################

################## Задача ЗАБАСТОВКИ ##################
# n, k = map(int, input('number of days = ').split())
# zab = set()
# for i in range(k):
#     a_i, b_i = [int(s) for s in input('a_i b_i = ').split()]
#     while a_i <= n:
#         zab.add(a_i)
#         a_i += b_i
# print(len(zab - set(range(0, n+1, 7)) - set(range(6, n+1, 7))))
# s1 = set(d)
# s2 = set(range(0, n+1, 7))
# s3 = set(range(6, n+1, 7))
# print(set(s1), len(s1))
# print(set(s2), len(s2))
# print(set(s3), len(s3))
# print(set(d), len(d))
# s = s1 - s2 - s3
# print(s, len(s))
