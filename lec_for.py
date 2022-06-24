a = 176

print(a%10 + a//10%10 + a//100%10)



# n = 123456789
# print(n//1000%10)
# print(n%10)

# for i in 'Hello', 1.567, 2**2, True, 8/2*4+16:
#     print(i, type(i))
#     print('*************')
# print('================')




# for i in 1324, 456/3, 'Hello':
#     print(i, type(i))



# for i in 2, 5, 78, 'Hello', 89-3:
#     # print(i, i*2, sep='->', end='===')
#     print(i, i*2)




# for i in range(30, 50, 5):   #  [77;80)
#     print(i, end='\t')

# a = range(5)
# print(a)



# for i in range(3):
#     for j in range(7):
#         print(i, j, end='\t\t')
#     print()



# a, b, c, d = range(-4, -8, -1)   # [0;4)
# print(a, b, c, d)
# print(range(5))




# 5! = 1 * 2 * 3 * 4 * 5
# a = int(input('a = '))
# res = 1
# for i in range(1, a+1):
#     res = res * i
#     res *= i
# print(res)


# for i in range(5):
#     if i == 3:
#         continue
#     for j in range(10):
#         if j % 2:  # j%2=0    j%2=1
#             print(str(i) * j)




# for i in range(100):
#     if i % 20 == 0:
#         print(i, 'Super!')
#         continue
#     elif i % 5 == 0:
#         print(i, 'Stop!')
#         break
#     print(i)



# a = 'How are ou!'
# for i in a:
#     # print(i)
#     if i == 'o':
#         print(i * 3, end=' ')
#         continue
#     elif i == 'y':
#         print(i * 5)
#         break
#     print(i, end=' ')
# else:
#     print('\nNo symbol y!!!')



# a = 34 - 29
# for i in range(7):
#     if i == 3:
#         print(i, i, i, i)
#         continue
#     elif i == 5:
#         print(i**2, '!!!!!!!!!!!!')
#         break
#     print(i, i**2, type(i))
# else:
#     print('No number 5!!!!')
# print('=' * 10)


# a = "Hello, world!"
# for i in a:
#     if i == 'l':
#         continue
#         print('L', end=' ')
#     elif i == 'r':
#         break
#     else:
#         print(i, end=' ')
#     print('=' * 10)
# else:
#     print('there is no "r"!!!')
#
# print(a)



