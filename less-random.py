import random
from collections import Counter

words = ["кошка", "собака", "слон", "бегемот", "кавалерист"]
list_of_words = []
for i in range(20):
    word = random.choice(words)
    list_of_words.append(word)
    print(word)

#################################
print('=' * 60)
print('STATISTIC :')
print('=' * 60)
c = Counter(list_of_words)
print('c : ', c, type(c))
prn_res = list(c.items())
prn_res.sort(key=lambda x: x[1], reverse=True)
for row in prn_res:
    print(*row, sep='\t')


#
# lst = [5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7]
# c = Counter(lst)
# print('lst : ', c, type(c))



















# operators = ['+', '-', '/', '*']
# a = input('первое число: ')
# b = input('второе число: ')
#
# q = random.choice(operators)
#
# r = eval(a + q + b)
# print('Выполняем операцию <', q, '> :', sep='')
# print(a + q + b, '=', r)
# print('Результат ', r)


# print(eval(str(4+2)))