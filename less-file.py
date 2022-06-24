
# f = open('test.txt', 'a')      # w - write, r - read, a - append, b - binary
# f = open(input('Inp name of file : '), 'w') # w -write, r - read, a - append, b - binary
#
# try:
#     f.write('''Start of writing...\n''')
#     f.write('Hello, World!\n')
#     f.write('End of writing...\n')
# finally:
#     f.close()




# f = open('test.txt', 'r')
#
# try:
#     for i in range(2):
#         p = f.readline()
#         print(i+1, 'line :', p, end='')
#     print(f.readline(10))
#     print(f.readline(100))
    # print()
    # print('symbols :', f.read(20))
    # print()
    # print('read :', f.read())
    # print()
    # print('read 1 :', f.read())
# finally:
#     f.close()

#


# with open('test.txt', 'w') as ff:
# with open(input('input name of file : '), 'w') as ff:
#     ff.write('''1234567
#     Hello World!
#     How do you do! ....
#     ''')
# #
# #
# with open('test.txt', 'r') as f2:
#     f0 = f2.read(2)
#     print(f0)
#     print(f2.read(3))
#     print('+' * 30)
#     print(f2.readline())
#     print('=' * 30)
#     print(f2.read())



import json   # JavaScript Object Notation

data = {'name': 'Ivan', 'surname': 'Popov', 'age': 28, 77: 'Casino'}

# with open('test.json', 'w') as f:
    # json.dump(data, f)
    # # json.dump(data, f, indent=4)

# d1 = json.dumps(data)
d1 = json.dumps(data, indent=4)
# print(d1, type(d1))
# # #
# # # #     print('\nWarning! 777 != "777" !!!!!!!!!\n')
# # # #
# with open('test.json', 'r') as file1:
#     k = json.load(file1) # file1 : test.json --> dict
#     k1 = json.loads(d1) # d1 type-str : d1 --> dict
#     print('k :', type(k), k)
#     print('k1 :', type(k1), k1)





#
# import pickle
#
#
# data = {'Alice': 89, 'Bob': '5', 'Charly': 32, 777: 'Casino'}
#
# print('======== dumps ===========')
# print('Dictionary data : ', data)
#
# serial_data = pickle.dumps(data)
#
# print('serial_data :', type(serial_data))
# print(serial_data)
# received_data = pickle.loads(serial_data)
# print('received_data :')
# print(received_data, type(received_data))
# print('=' * 40)
# print()
# print('======== dump ===========')
# with open('test.pickle', 'wb') as file:
#     pickle.dump(data, file)
# # #
# with open('test.pickle', 'rb') as file:
#     pr = pickle.load(file)
#     print(pr, type(pr))
#

#
#
import csv
#
#
# with open('test.csv', 'w', newline='') as file:
#     wr = csv.writer(file, delimiter=',')
#     wr.writerow(['Name', 'Surname', 'Age'])
#     wr.writerow(['Ivan', 'Petrov', 18])
#     wr.writerow(['Anton', 'Pupkin', 22])
#     wr.writerow(['Serge', 'Nikonov', '35'])
#     wr.writerow(['Serge1', 'Nikonovich', '55'])


# with open('test.csv', 'r') as file:
#     reader = csv.reader(file)
#     print('reader', reader, type(reader))
#     for i in reader:
#         # print(*i, sep='\t')
#         print(i)

# with open('test.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     print('reader', reader, type(reader))
#     # for i in range(2):
#     #     print(i, ':', next(reader))
#     # print('******************')
#     for i in reader:
#         print('line :', i, type(i))
##########################################
# f1 = 'Name'
# f2 = 'Surname'
# f3 = 'Age'
#
# fields = ['Name', 'Surname', 'Age']
# my_dict = [
#     {'Name': 'Ivan', 'Surname': 'Petrov', 'Age': 18},
#     {'Name': 'Oleg', 'Surname': 'Ivanov', 'Age': 22},
#     {'Name': 'Ira1', 'Surname': 'Kozlov', 'Age': 34},
#     {'Name': 'Sasha', 'Surname': 'Pupkin', 'Age': 56},
#     {'Name': 'Pasha', 'Surname': 'Sidorov', 'Age': 78}
# ]
#
# with open('test1.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fields, delimiter=',')
#     writer.writeheader()
#     writer.writerows(my_dict)
# #
# # #!!!!!!!!!!!!!!!!!!!! delimiter= ';' for Excel, but ',' for dict !!!!
# with open('test2.csv', 'w') as file:
#     writer = csv.DictWriter(file, fieldnames=fields, delimiter=';')
#     writer.writeheader()
#     writer.writerows(my_dict)
# #
# # #
with open('test1.csv', 'r') as file:
    reader = csv.DictReader(file)
    print('reader', reader, type(reader))
    print(next(reader))
    # print(next(reader))
    print(list(reader))
    # print(list(reader))





    for i in reader:
        print('Dictionary : ', i, type(i))
