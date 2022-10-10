# from math import pi
#
# #  Полиморфизм
# """
#     Полиморфизм деген эмне?
#     Полиморфизм программалоодо абдан маанилүү идея. Ал ар кандай колдонуу учурларда ар
#     кандай типтерди көрсөтүү үчүн бир объектти (ыкма, оператор же объект) колдонуудан турат.
# """
#
# class Shape:
#     def __init__(self, lenght):
#         self.__lenght = lenght
#
#     def getLenght(self):
#         return self.__lenght
#
#     def set_lenght(self, newLenght):
#         self.__lenght = newLenght
#
#     def area(self):
#         pass
#
#     def fact(self):
#         print('Shape!')
#
#
# class Square(Shape):
#     def __init__(self, lenght):
#         super().__init__(lenght)
#
#     def area(self):
#         print(f"Square areas = {self.getLenght()**2}")
#
#     def fact(self):
#         print('Square')
#
#
# class Circle(Shape):
#     def __init__(self, lenght):
#         super().__init__(lenght)
#
#     def area(self):
#         print(f"Circle areas = {pi*(self.getLenght()/2)**2}")
#
#     def fact(self):
#         print('Circle')
#
#
# square = Square(100)
# circle = Circle(10)
#
# square.area()
# circle.area()

"""
    Тапшырма
    Бир класс жазып ООПнын 3 принсибин колдонуңуз
"""

# link https://youtu.be/aEOSBkzNImw

# class Building:
#     type = "School"
#     year = "2012-жылы"
#     city = "Bishkek"
#     pupils = 4000
#     floor = 5
#     gym = "Yes"
#     library = "Yes"
#
#     def info_building(self):
#         print(f"Type: {self.type}\n"
#               f"Year: {self.year}\n"
#               f"City: {self.city}\n"
#               f"Pupils: {self.pupils}\n"
#               f"Floor: {self.floor}\n"
#               f"Gym: {self.gym}\n"
#               f"Library: {self.library}")
#
#     def plays(self):
#         print("Children play in the gym.")
#
#     def sing(self):
#         print("Students sing in their free time.")
#
#     def read(self):
#         print("Reads interesting books")
#
#     def write(self):
#         print("They write")


# school = Building()
# school.info_building()
# school.plays()
# school.sing()
# school.read()
# school.write()
#
#
# class Building:
#     def __init__(self, type, year, city, pupils, floor):
#         self.__type = type
#         self.__year = year
#         self.__city = city
#         self.__pupils = pupils
#         self.__floor = floor
#
#
#     def info_building(self):
#         print(f"Type: {self.type}\n"
#               f"Year: {self.year}\n"
#               f"City: {self.city}\n"
#               f"Pupils: {self.pupils}\n"
#               f"Floor: {self.floor}\n"
#               f"Gym: {self.gym}\n"
#               f"Library: {self.library}")
#
#
#     def get_type(self):
#         return self.__type
#
#     def set_type(self, newType):
#         self.__type = newType
#
#     def get_year(self):
#         return self.__year
#
#     def set_year(self, newYear):
#         self.__year = newYear
#
#     def get_city(self):
#         return self.__city
#
#     def set_city(self, newCity):
#         self.__city = newCity
#
#     def get_pupils(self):
#         return self.__pupils
#
#     def set_pupils(self, newPupils):
#         self.__pupils = newPupils
#
#     def get_floor(self):
#         return self.__floor
#
#     def set_floor(self, newFloor):
#         self.__floor = newFloor
#
#
# class School(Building):
#     def __init__(self, type, year, city, pupils, floor, gym, library):
#         super().__init__(type, year, city, pupils, floor)
#         self.__gym = gym
#         self.__library = library
#
#     def get_gym(self):
#         return self.__gym
#
#     def set_gym(self, newGym):
#         self.__gym = newGym
#
#     def get_library(self):
#         return self.__library
#
#     def set_library(self, newLibrary):
#         self.__library = newLibrary
#
#     def info_building(self):
#         super().info_building()
#         print(f"Gym: {self.__gym}\n"
#               f"Library: {self.__library}")
#
#     def plays(self):
#         print("Children play in the gym.")
#
#     def sing(self):
#         print("Students sing in their free time.")
#
#     def read(self):
#         print("Reads interesting books")
#
#
# class House(Building):
#     def __init__(self, type, year, city, pupils, floor, garage):
#         super().__init__(type, year, city, pupils, floor)
#         self.__garage = garage
#
#     def get_garage(self):
#         return self.__garage
#
#     def set_garage(self, newGarage):
#         self.__garage = newGarage
#
#     def to_cook(self):
#         super(House, self).info_building()
#         print("Delicious food is always ready.")
#
#     def info_building(self):
#         super().info_building()
#         print(f"Garage: {self.__garage}\n")
#
#
# school = School("School", "2021-жылы", "Бишкек", "1999", "5", "Yes", "Yes")
#
#
#
# house = House("House", "2010-жылы", "Osh", "4", "2", "No")



# class Nod:
#
#     def __init__(self, a, b):
#         self.__a = a
#         self.__b = b
#
#     def get_a(self):
#         return self.__a
#
#     def set_a(self, Newa):
#         self.__a = Newa
#
#     def get_b(self):
#         return self.__b
#
#     def set_b(self, newB):
#         self.__b = newB
#
#     def min(self, a, b):
#         self.__a = a
#         self.__b = b
#
#         while a != b:
#             if a > b:
#                 a = a - b
#             else:
#                 b = b - a
#
#         print(a)
#
#
# a = Nod(20,5)
# a.min(30,6)


























# from math import pi
#
#
# class Shape:
#     def __init__(self, name):
#         self.name = name
#
#     def area(self):
#         pass
#
#     def fact(self):
#         return "I am a two-dimensional shape."
#
#     def __str__(self):
#         return self.name
#
#
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Square")
#         self.length = length
#
#     def area(self):
#         return self.length**2
#
#     def fact(self):
#         return "Squares have each angle equal to 90 degrees."
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius
#
#     def area(self):
#         return pi*self.radius**2