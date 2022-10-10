"""
    1.  Класс жазыңыз 4 методу болсун,
        1-методу файл түзөт
        2-методу файлды өчүрөт(удалить)
        3-методу папка түзөт
        4-методу папканы өчүрөт


    2.  Dictionary түзүңүз ал атыңызды жана фамилияңызды ичинде камтысын
    аларды кайра экранга атты башка фамилияны башка, башкача айтканда 2 print
    колдонуп чыгарыңыз.

    3.  2 өлчөмдүү лист түзүп ичин 100 гө чейинки сандар менен толтуруңуз

    4.  жогорудагы толтурулган листтин ичинен жуп болгон сандарды экранга чыгарын

    5.  Колдонуучудан 3 сан сурап алып алардын эң чоңун табыныз

    6.  листти рандом сандар менен толтуруп аны сорттоп экранга чыгар,
    андан кийин кайра аралыштыр  (random модулун колдон)
"""

# 1-тапшырма
#
# import os
#
# class Oop:
#     def file_open(self):
#         with open("sabak.txt", "w") as file:
#             file.write("Hello")
#             print(file)
#
#     def file_close(self):
#         os.remove("sabak.txt")
#         print("Файл удалено")
#
#     def folder(self):
#         os.mkdir("folder")
#
#
# 2-тапшырма
#
# info = {"name": "Feruza", "surname": "Kairatbekova"}
# print(info)
# info["name"] = "Арзыбек"
# print(f"Аты озгорду: {info}")
# info["surname"] = "Асанов"
# print(f"Аты-жону озгорду: {info}")
#
# 3-тапшырма
#
# a = []
# for i in range(100):
#     print(a)
# 
#
#  4-тапшырма
#
# a = []
# for i in range(100):
#     if i % 2 == 0:
#         print(i)
#
#
# 5-тапшырма
#
# x = int(input("Бир санды жазыныз: "))
# y = int(input("Бир санды жазыныз: "))
# z = int(input("Бир санды жазыныз: "))
#
# if x>y>z and x>z :
#     print(f"Чон сан: {x}")
# elif x<y<z and x<z:
#     print(f"Чон сан: {z}")
# else:
#     print(f"Чон сан: {y}")
#
#
# 6-тапшырма
#
# import random
# my_list = [1, 5, 6, 10, 2, 89, 0, 15]
# my_list.sort()
# print(f"Сортировка болгон лист: {my_list}")
# random.shuffle(my_list)
# print(f"Рандом болгон лист: {my_list}")

# class Sorting:
#     def sort(self, list):
#         self.list = list()
#         i = 0
#         while i < list - 1:
#             j = 0
#             while j < list - 1 - i:
#                 if a[j] > a[j + 1]:
#                     a[j], a[j+1] = a[j+1], a[j]
#                 j += 1
#             i += 1
#         print(a)
#
# a = Sorting()
# a.sort(2,15,78,58,0,57,98)


class Sorting:
    def sort(self, list):
        self.a = list
        i = 0
        while i < len(a):
            j = 0
            while j < i + 1:
                if a[j] < a[i]:
                    a[i], a[j] = a[j], a[i]
        print(a)

a = [10, 56, 1, 98, 2, 3, 45]

obj = Sorting()
obj.sort(a)





