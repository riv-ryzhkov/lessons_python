# 
# n = int(input('Input number of steps in cycle : '))
# sum_ = 0
# for i in range(n):
#     num = int(input('input number : '))
#     if num == 0:
#         break
#     sum_ += num
#     print('step No.', i, sum_)
# else:
#     print('number of the cycle over')
# print('=====', sum_, 'Finish!!!!')


# sum_ = 0
# num = True
# while num:
#     num = int(input('input number : '))
#     sum_ += num
#     if num == 0:
#         print('FINISH')
#     else:
#         print(num, end=' ')
#
# print(sum_, '===FINISH====')


# n = int(input('Input number of cycles : '))
# sum_ = 0
# while n:
#     num = int(input('Input symbol : '))
#     sum_ += num
#     n -= 1
# print('='*60)
# print(sum_)
# print('='*60)

text = 'kjhkljh;kl'
n = len(text)
# for i in text:
#     print(i, end='-')
while n:
    print(text[-n], end='-')
    n -= 1





#
# n = int(input('Input number of steps in cycle : '))
# a = n
# while a > 0:
#     print('step No.', n - a + 1)
#     a -= 1
#     if a < 4:
#         break
# # print('Finish!!!!')
# else:
#     print('Finish!!!!')



# n = int(input('Input number of numbers : '))
# sum_ = 0
# for i in range(n):
#     number = int(input('Input number : '))
#     sum_ += number
# print('Sum = ', sum_)



# sum_ = 0
# while True:
#     n = input('Input number or "0"(for count sum) : ')
#     if n == '' or not n.isdigit():
#         print('Input only numbers, please!' )
#         continue
#     n = int(n)
#     if n == 0:
#         break
#     sum_ += n
# print('Sum = ', sum_)

#
# text = 'Input integer number or "0"(for count sum) : '
# number = '0'
# count = 0
# count1 = 0
#
# sum_ = int(number)
# while number:
#     count += 1
#     number = input(text)
#     if not number or not number.isdigit() :
#         print('Input only integer numbers, please!' )
#         number = '0'
#         continue
#     count1 += 1
#     number = int(number)
#     sum_ += number
# print('The cycle took', count, 'steps. And ', count-count1, 'of them is ERROR!')
# print('Sum = ', sum_)



# text = input('Input text, please : ')
# attempt = len(text)
# n = 60
# while attempt:
#     symbol = input('Input a symbol, please: ')
#     if text.count(symbol):
#         print('\n' * 3, '!' * n)
#         print('You win!!!'.center(n, ' '))
#         print(('The symbol "' + symbol + '" is in the text !').center(n, ' '))
#         print('!' * n)
#         break
#     print()
#     attempt -= 1
#     print('No symbol "' + symbol + '" in the text!')
#     print('Try again, please! You have', attempt, 'attempts.')
# else:
#     print('=' * n)
#     print("Sorry, You don't have any attempt...")
#     print('=' * n)


# text = 'Hellooooopp'
# count, count1 = 0, 0
# for i in text:
#     if text.count(i) == 1:
#         # text = text[text.find(i)+2:]
#         print(i, 'One time')
#         count += 1
#     else:
#         print(i, '->', text.count(i), 'times')
#         count1 += 1
# else:
#     print('No break')
# print(int(count), count1)



