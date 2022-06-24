
d1 = {'name': 'Ivan', 33: 3244, 'surname': 'Pupkin', 56: [23, 45, 'bmn'], (34, 0): 6877, 5: {1: 'jhlkkllkhlk'}}
d2 = dict([('a', 'A'), ('b', 'B'), (1, 'C')])
d3 = dict(name='Ivan', surname='Petrov', nation='Ukrainian')


# print(id(d1), d1)
# d5 = d1.copy()
# d5 = dict(d1)
# d1['name'] = 'Gosha'
# print(id(d1), d1)
# print(id(d5), d5)

# print(d1.get('name222', 'No key!'))
# print(d1.keys())
# print(d1.values())
# print(d1.items())
# for key, value in d1.items():
#     print(key, value, sep=' -> ')

# print(d1)
# val = d1.pop('name')
# print(d1)
# print(val)
# d1['name'] = val
# print(d1)
# it = d1.popitem()
# print(d1)
# print(it)
# d1[it[0]] = it[1]
# print(d1)
# d1.setdefault('name333', 'No key')
# print(d1)
# d11 = {1: 'a', 2: 'b', 6: 'c'}
# for i in range(1, 9):
#     d11.setdefault(i, 'XXX')
# print(id(d11), d11)
# d11.clear()
# # d11 = {}
# print(id(d11), d11)


# print(d3)
#
# l1 = ('rt', (4, 99))
# print(dict(l1))
#
#
# d4 = {1: 2, 'peace': 'future', 99: {0: 5, 't': 'text'}}
# print(d4)
# print(d4[99])
# print(d1['name'])
# d1['name1'] = 'Vasya'
# d1['name2'] = 'Kolya'
# del d1['name1']
# print(d1['name'])
# print(d1)



# d1 = {0: 'H', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}
# text = 'Hello!'
# l1 = list('Hello!')
# # l1.pop(0)
# # d1.pop(0)
# print(d1[4])
# print(text[4])
# print(l1[4])
# print(text)
# print(l1)
# print(d1)
#


# print(d1['name'])
# print('d1 = ', d1, id(d1))
# print('d2 = ', d2, id(d2))
# print('d3 = ', d3, id(d3))
# # d4 = dict()
# # d4 = {}
# # d4 = set()
# # print(d4, type(d4))
#
#
# print('d3 = ', d3, id(d3))
# d3['age'] = 34
# print('d3  : ', d3, id(d3))
# d3['name'] = 'Petro'
# print('d3  : ', d3, id(d3))
# print(d3['name'])


# dd = d3
# dd = d3.copy()
dd = dict(d3)
dd['tel'] = '4354356'
# print('d3 =', d3, id(d3))
# print('dd =', dd, id(dd))


d4 = {}
d5 = dict()
# print(d4, type(d4))
# print(d5, type(d5))



d1 = {'name': 'Ivan', 56: [23, 45, 'bmn'], (34, 0): 6877, 0: 'jhlkkllkhlk'}
# print('d1 : ', d1, type(d1))
# print('d1[0] : ', d1[0], type(d1))
d1[0] = '777777777'
# print('d1', d1, type(d1))
# print('name' in d1)
# print('d3', d3, type(d3))
# print('d4', d4, type(d4))
# print('d5', d5, type(d5))
# print(d1[999])

# s = int(input('key = '))
# if s in d1:
#     print(d1[s])
# else:
#     print('No key ', s)

# key_ = input('key = ')
# if key_ not in d1:
#     d1[key_] = input('value = ') # LIFO
# else:
#     print('key', key_, 'exists!!!')
# print(d1[key_])
# print(d1)
# print('name' in d1)

#
a = ['a', 'b', 'c']
# d3 = dict.fromkeys(a, '*')
# d3 = dict.fromkeys(range(1, 6), input(' student is : '))
d3[3] = '50x50'
# print('d3', d3, id(d3))
d3 = {}
# print(len(d3))
# for i in range(int(input('number of students = '))):
#     d3[input('surname : ')] = input('name = ')
# print('d3', d3, id(d3))
#
#
# d5 = d3.copy()
# d5 = dict(d3)
# d4 = d5
# print('d4', d4, id(d4))
# print('d5', d5, id(d5))
#
#
d5 = {}
d5[1] = 'aaaaaaaaaa'
d5[0] = 'xxxxxxxxx'
d5['1'] = 'bbbbbb'
d5['abc'] = '00000'
d5[True] = '999999'
d5[False] = 'AAAAAA'
d5[1] = d5[0] = 0
# print('d5', d5, id(d5))
#
# print(d5[1])
# print(d5[1111])
# print(d5.get(11111, 'No key!!!!!!!'))
# s = input('key = ')
# print(d5.get(s, 'No the key ' + s))
# print(d5.get('abc'))
# print(d5.get('Hello', 'No the key!'))
#
#
# p = d5.keys()
# print('p = ', p, type(p))
# print(list(d5.keys()))
# #
#
# print(d5.values())
# print(list(d5.values()))
#
#
# print(d5.items())
# print(list(d5.items()))
# print(list(zip(d5.keys(), d5.values())))
#
k = '1'
# s = d5.pop(k) # LIFO
# print(s)
# print(d5)
# d5[k] = s
# print(d5, id(d5))  # LIFO
# #
#
s = d5.popitem()
# print('s =', s)
# print(d5, id(d5))
d5[s[0]] = s[1]
# print(d5, id(d5))
#
#
# print(d5.pop(input('key ='), 'No key!!'))
# print(d5)
#
# print(d5.setdefault(1, 'NNNN'))
# d5[1] = 'KKKK'
# print(d5.setdefault(2222, 'MMM'))
# print('d5', d5)
#
#
d6 = dict(Name='Ivan', Surname='Petrov', age=34)
# d7 = {'Name': 'Ivan', 'Surname': 'Petrov', 'age': 34, 1: '000000'}
# print('d6 =', d6, id(d6))

d7 = {'age': 88, 'tel': '000000'}
# print('d7 =', d7, id(d7))
d6.update(d7)
# print('d6 =', d6, id(d6))

# d6.clear()
# d6 = {}
d6 = dict()
# print('d6 =', d6, id(d6))
# print(d7)

#
#
# print('d7', d7)
# d5.update(d7)
# print('d5', d5, id(d5))
#

d15 = {1: 'a', 2: 'b', 3: 'c'}
# for i in range(5):
#     if input('val = ') in d15.values():
#         print('Yes')
#     else:
#         print('No!')


# d15.update({1: 'PPPPP', '666': '76876897689'})
# print(d15)
#
#

dd = {x: chr(x) for x in range(97, 115) if x%2==0}
# dd[99] = 'X'
# print('dd =', dd)
# for k, v in dd.items():
#     print(k, v, sep=' -> ')
#
# print('99', dd[99])
# print('99', chr(99))
# print(ascii_[int(input('n = '))])
#
# for k in dd:
#     print(k, dd[k], sep='\t')
#
# for key, val in dd.items():
#     print(key, val, sep='\t')
#
#
import random


city = ['Kiev', 'Poltava', 'Dnipro', 'Lviv']
population = [4000, 700, 1000, 850]
dict_ua = {x: y for x, y in zip(city, population)}
# print(dict_ua)
# print(list(dict_ua.items()))
#
# key = random.choice(list(dict_ua))
# print(key)
# question, answer = key, dict_ua[key]
# print('question :', question)
# a = int(input('population?  = '))
# if a == answer:
#     print('You are right!')
# else:
#     print('You are wrong!')
# print('answer :', answer)




# #
# # #***************** Сортировка по населению
# l1 = list(dict_ua.items())
# print(l1)
# l1.sort(key=lambda x: x[1], reverse=True)
# # l1.sort()
# for i in l1:
#     print(*i, sep='\t')
# #**************************!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#
#******* Сортировка букв любого введенного текста
# l = set('ABC123')
# print(l)
# s = input('Input any text : ').upper()
# print(s)
# r = dict(zip(list(l), list(map(s.count, l))))
# print(r)
# ll = list(r.items())
# print(ll)
# ll.sort(key=lambda x: x[1], reverse=True)
# for i in ll:
#     print(*i, sep='\t')
#
#
#
# text = 'Hello, world!'
# a = dict(zip(list(range(len(text))), list(text)))
# print(a)
# for key, val in a.items():
#     print(key, '-', val, sep='', end='  ')
# print()
#
#
c1 = {1, 2, 3}
c = False
a = {c: 2}
b = dict(a)
# print('a: ', a)
# print('a: ', a[0])
# print('b: ', b)
#
# a.setdefault(False)
# a.setdefault('F')
# a.setdefault('Fal', True)
#
# a[1] = 33333
# b.update(a)
# print('a: ', a)
# print('b: ', b)
#
# a[True] = 555
# a[0] = 77777
# print('a: ', a)
# a.update({'Trash': ':-)'})
# print('a: ', a)

############# ФОРМИРОВАНИЕ СЛОВАРЯ ПО СПИСКУ #############3
# keys = 'ten, one, five, two, three, four'
# keys = keys.split(', ')
# values = ['номер ' + str(i) + ' в строке' for i in range(1, len(keys)+1)]
# dic = dict(zip(keys, values))
# dic = {}
# for i in range(len(keys)):
#     dic[keys[i]] = 'номер ' + str(i + 1) + ' в строке'
# print(dic)