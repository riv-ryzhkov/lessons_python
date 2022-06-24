# from func import pr, pr1, pr3
#
#
# pr('Hello, world!')
# pr1('Hello, world!')
# pr3('Hello, world!')
#

######################################################################
#   ПРИМЕР  (с полиморфизмом)   ######################################
######################################################################
# class Door:
#     colour = 'brown'
#
#     def __init__(self, number=0, status='open'):
#         self.number = number
#         self.status = status
#
#     def open(self):
#         self.status = 'open'
#
#     def close(self):
#         self.status = 'closed'
#
#     def colouring(self):
#         col = input('colour = ')
#         self.colour = col
#
#     def __str__(self):
#         return 'The ' + self.colour + ' door number ' + str(self.number) + ' is ' + self.status
#         # return 'Hello, Vasya!'
#
#     def __add__(self, other):   #  +
#         # return self.number + other.number
#         return str(self.number) + '->' + str(other.number)
#
#     def __len__(self):
#         return len(str(self.number))
#
#     if __name__ == "__main__":
#         print('hello!')
#
#
#
# d1 = Door(22)
# d2 = Door(33)
# print(d1 + d2)
# print(len(d1))
# # print(type(d1))
# # print(d1.__class__)
# print(*dir(d1), sep='\n')
# print(d1.number)
# print(d1.colour)
# d1.open()
# print(d1.status)
# print(d1.colour)
# d1.close()
# d1.colouring()
# print(d1.status)
# print(d1.colour)



#

#

#

#

#
#
# door1 = Door(338990798)
# door2 = Door(111)
# print(*dir(door1), sep='\n')
# print(door1.__class__)
# print(type(door1))
# print(door1)
# print(door1 + door2)
# print(len(door1))
# print(door1.status)
# door1.close()
# print(door1.status)
# door1.open()
# print(door1.status)
# print(door1.colour)
# door1.coloured()
# print(door1.colour)



#

#

#

#

#
# #
# d1 = Door(222, 'open')
# d2 = Door(333, 'open')
# print('d1+d2  :   ', d1+d2)
# print('d1.number  :', d1.number)
# print('d1.color   :', d1.colour)
# print('d1.status  :', d1.status)
# d1.close()
# print('d1.status  :', d1.status)
# d1.status = ':-)'
# print('d1.status  :', d1.status)
#
#
#
# d1 = Door(15, 'closed')
# d2 = Door(16, 'open')
# print('the door', d1.number, 'is', d1.colour, 'and', d1.status)
# print('the door', d2.number, 'is', d2.colour, 'and', d2.status)
# d1.open()
# d2.close()
# print('the door', d1.number, 'is', d1.colour, 'and', d1.status)
# print('the door', d2.number, 'is', d2.colour, 'and', d2.status)
# # print(dir(d1))
# print(d1)
# print(d1+d2)
# print(len(d1))
# print(d2.__class__)
#
#
# class SecurityDoor(Door):
#     colour = 'grey'
#
#     def __init__(self, number, status='closed', locked=True):
#         Door.__init__(self, number, status)
#         self.locked = locked
#         # self.colour = super().colour
#
#     def open(self):
#         if not self.locked:
#             self.status = 'open'
#
#
#
#
# print(d1)
# print(d2)
# d3 = SecurityDoor(999)
# print(d3)
# d3.locked = False
# d3.open()
# print(d3)

#

#
#     # def __str__(self):
#     #     return Door.__str__(self)
#     #     return 'the door ' + str(self.number) + ' is ' + self.colour + ' and ' + self.status
#
# #
# #
# d3 = SecurityDoor(17, 'closed')
# print(d3)
# d3.open()
# print(d3)
# d3.locked = False
# d3.open()
# d3.colour = 'white'
# # print(d3.colour)
# # print(d3)
# d3.close()
# # print(d3)

#
##################################################################
#################################################################
################# Методы __init__, __str__, __repr__ ############
#################################################################
#
# class Human:
#     def __init__(self, sex, age):
#         self.sex = sex
#         self.age = age
#
#     def __str__(self):
#         return 'Human: ' + self.sex + ' ' + str(self.age) + ' years old'
#
#     def __repr__(self):
#         return 'Human(' + self.sex + ',' + str(self.age) + ')'
#
# a1 = Human('man', 28)
# a2 = Human('woman', 25)
# print(*dir(a1), sep='\n')
# print(a1)
# print([a1, a2])






# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#                НАСЛЕДОВАНИЕ
#############################################
#
# class Human:
#
#     def __init__(self, name='NoName', surname='NoSurname', age=18):
#         self.age = str(age)
#         self.name = name
#         self.surname = surname
#
#     def __repr__(self):
#         return ('=====', self.name + ' ' + self.surname + ' ' + str(self.age))
#
#     def __str__(self):
#         return ('=str=   ' + self.name + ' ' + self.surname + ' ' + str(self.age))
#
#
# n1 = Human('Ivan', 'Popov', 22)
# print(n1.name, n1.surname, n1.age, type(n1))
# print(n1)
#
#
# class Student(Human):
#
#     def __init__(self, name='NoName', surname='NoSurname', age=18, group=222):
#         Human.__init__(self, name, surname, age)
#         self.group = group
#
#
# n2 = Student()
# n3 = Student()
#
# print(n2.group, n2.name, n2.surname, n2.age)
# print(n3.group, n3.name, n3.surname, n3.age)
#
# n3.name = 'John'
# n3.surname = 'Kozlov'
# n3.age = 55
# print(n3)
# n3 = Student(name='John', surname='Kozlov', age=55)
# print(n3.group, n3.name, n3.surname, n3.age, type(n3))
# n3.group = 9999
#
# print(n3.group, n3.name, n3.surname, n3.age)


############################################################


######################################################
############ Stack ###################################
######################################################
#
# class Stack:
#     def __init__(self):
#         self.number = None
#
#     def inp(self, x):
#         self.number = [x, self.number]
#
#     def pop(self):
#         assert self.number is not None, 'Stack is empty'
#         x = self.number[0]
#         self.number = self.number[1]
#         return x
#
# a = Stack()
# a.inp(input('Input element : '))
# a.inp(input('Input element : '))
# a.inp(input('Input element : '))
# a.inp(input('Input element : '))
#
# print(type(a))
# print(a.number)
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# # print(a.pop())


#
# class Stack:
#     def __init__(self):
#         self.number = None
#
#     def inp(self, x):
#         if self.number:
#             self.number = [x] + self.number
#         else:
#             self.number = [x]
#
#     def pop(self):
#         if not self.number:
#             return 'Stack is empty'
#         x = self.number[0]
#         self.number = self.number[1:]
#         return x
#
# a = Stack()
# for i in range(1, 5):
#     print(i)
#     a.inp(i)
# print(type(a))
# print(a.number)
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())




#######################################################################
############ Атрибуты и методы Class ##################################
#############     ИНКАПСУЛЯЦИЯ      ###################################
#######################################################################


# class StudentUniver:
#     animal = 'Human'
#     def __init__(self, hight, age):
#         self.hight = hight
#         self.age = age
#
#     def _health_(self, health='good'):
#         self.health = health
#         return self.health
#
#
#     def __average__(obj1, obj2):
#         return (obj1.hight + obj2.hight)/2
#
#
#
# a1 = StudentUniver(186, 18)
# a2 = StudentUniver(178, 21)
#
# print('a1.animal   :', a1.animal)
# print('a2.animal   :', a2.animal)
# print('a1.hight    :', a1.hight)
# print('a1.hight - a2.hight :', a1.hight - a2.hight)
# print('(a1.age + a2.age)/2 :', (a1.age + a2.age)/2)
# a2.animal = 'Man'
# a1.hight = 188
# print('a1.animal   :', a1.animal)
# print('a2.animal   :', a2.animal)
# print('a1.hight    :', a1.hight)
# print('a1.hight - a2.hight :', a1.hight - a2.hight)
# StudentUniver.animal = 'Got'
# print('a1.animal   :', a1.animal)
# print('a2.animal   :', a2.animal)
# print('=' * 80)
# a3 = StudentUniver(176, 20)
# print('a1.animal   :', a1.animal)
# print('a2.animal   :', a2.animal)
# print('a3.animal   :', a3.animal)
#
#
#
# # print(dir(a1))
# a1.health = 'bed'
# print('a1.health    :', a1.health)
# a1._health_() # вылечить!!!
# print('a1.health    :', a1.health)
# print('StudentUniver.__average__(a1, a2)  :', StudentUniver.__average__(a1, a2))


######################################################
### School ###########################################
###     ПОЛИМОРФИЗМ     ##############################
######################################################
class SchoolMember:
    count_members = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        SchoolMember.count_members += 1
        print('(Создан SchoolMember: {0})'.format(self.name))

    def tell(self):
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        SchoolMember.count_members += 1
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))


class Student(SchoolMember):

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        SchoolMember.count_members += 1
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))


t1 = Teacher('Mrs. Shevchenko', 35, 20000)
t2 = Teacher('Mrs. Koval', 40, 30000)
s1 = Student('Petrov', 20, 75)
s2 = Student('Hmara', 19, 95)

print()

members = [t1, s1, t2, s2]
for member in members:
    member.tell()
