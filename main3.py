
# class Human:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def drink(self):
#         print(f"{self.name} is drinking")
#
#     def walk(self):
#         print(f"{self.name} is walking.")
#
#
# belek = Human('Belek', 23)
# argen = Human('Argen', 23)
# nurgazy = Human('Nurgazy', 25)
# feruza = Human('Feruza', 19)

###  Кайталоо болуп жатат !!!!!

# print('=====================')
# print(belek.name)
# print(belek.age)
# belek.drink()
# print('=====================')
# print(argen.name)
# print(argen.age)
# argen.drink()
# print('=====================')
# print(nurgazy.name)
# print(nurgazy.age)
# nurgazy.drink()
# print('=====================')
# print(feruza.name)
# print(feruza.age)
# feruza.drink()
# print('=====================')
#
# def display_humans_info(humans):
#     for human in humans:
#         print(human.name)
#         print(human.age)
#         human.drink()
#         human.walk()
#         print('========================\n')

# def display_humans_info(humans):
#     i = 0
#     while i < len(humans):
#         print(humans[i].name)
#         print(humans[i].age)
#         humans[i].drink()
#         humans[i].walk()
#         print('========================\n')
#         i = i + 1
#
# humans = [belek, argen, nurgazy, feruza]
# display_humans_info(humans)

# class Tikburchtuk:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def ayant(self):
#         return self.x * self.y
#
# tikburchtuk = Tikburchtuk(4, 6)
# print(tikburchtuk.ayant())

# class Calculator:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def sum(self):
#         return self.y + self.x
#
#     def div(self):
#         return self.y/self.x
#
# calculator = Calculator(10, 20)
# ans = calculator.sum()
# print(ans)
# print(calculator.div())


# class Computer:
#
#     def __init__(self, marka, model):
#         self.marka = marka
#         self.model = model
#
#     def play_video(self):
#         print(f"{self.model} playing video")
#
#     def play_music(self):
#         print("play music")
#
# hp = Computer('HP', 'probook')
# hp.play_video()
# hp.play_music()
#
# asus = Computer('Asus', '600s')
# asus.play_video()
# asus.play_music()
#
# dell = Computer('Dell', '400')
# dell.play_video()
# dell.play_music()


# class Animal:
#     type_animal = "Cat"
#     name = "Мий мий"
#     age = 1
#     color_cat = "white"
#     types_of_cat = "Балийская кошка"
#
#     def info_animal(self):
#         print(f"type_animal: {self.type_animal}\nname: {self.name}\nage: {self.age}\n"
#               f"color_cat: {self.color_cat}\ntypes_of_cat: {self.types_of_cat}")
#
#
# cat = Animal()
# cat.info_animal()


class Animal:

    def __init__(self, type_animal, name, age, color, types, voice):
        self.type_animal = type_animal
        self.name = name
        self.age = age
        self.voice = voice
        self.color = color
        self.types = types

#     def display_info(self):
#         print(f"Type: {self.type_animal}\n"
#               f"Name: {self.name}\n"
#               f"Age: {self.age}\n"
#               f"Color: {self.color}\n"
#               f"Types: {self.types}\n"
#               )
#
#     def voice_func(self):
#         print(self.voice)
#
#     def run(self):
#         print("Running.")
#
#     def drink(self):
#         print(f"{self.name} is Drinking")
#
#
# dog = Animal("dog", "Боби", 2, "black", "Акита-ину", "Gaf-Gaf")
# bird = Animal("bird", "Eurasian bittern", 1.5, "green", "Фламингообразные", "CHip-chip")
# cat = Animal("Cat", "Baris", 1, "Black", "Балийская кошка", 'miao-miao')
# eagel = Animal("Eagle", 'asdf', 1, "White", 'asdf', 'Chiik')
#
# animals = [dog, bird, cat, eagel]
#
#
# for animal in animals:
#     animal.display_info()
#     animal.drink()
#     animal.run()
#     animal.voice_func()
#     print("---------------------\n")

### жетүү ыкмалары ###
"""
    1.  public
    2.  protected
    3.  private
"""

# class Animal:
#
#     def __init__(self, type_animal, name, age, color, types, voice):
#         self.__type_animal = type_animal
#         self.__name = name
#         self.__age = age
#         self.__voice = voice
#         self.__color = color
#         self.__types = types
#
#     def get_types(self):
#         return self.__types
#
#     def set_types(self, types):
#         self.__types = types
#
#     def display_info(self):
#         print(f"Type: {self.__type_animal}\n"
#               f"Name: {self.__name}\n"
#               f"Age: {self.__age}\n"
#               f"Color: {self.__color}\n"
#               f"Types: {self.__types}\n"
#               )
#
#     def voice_func(self):
#         print(self.voice)
#
#     def run(self):
#         print("Running.")
#
#     def drink(self):
#         print(f"{self.name} is Drinking")
#
# dog = Animal("dog", "Боби", 2, "black", "Акита-ину", "Gaf-Gaf")
# print("Озгоргонго чейин")
# print(dog.get_types())
# print('Озгоргондон кийн')
# dog.set_types('Alabay')
# print(dog.get_types())


# class Human:
#
#     def __init__(self, argName, argAge):
#         self.__name = argName
#         self.__age = argAge
#
#     def set_age(self, argAge):
#         self.__age = argAge
#
#     def getAge(self):
#         return self.__age
#
#     def show_info(self):
#         print(self.__name)
#         print(self.__age)
#
#
# belek = Human("Belek", 22)
# belek.set_age(23)
# belek.show_info()
#
#
"""
    Компьютер классын түзүп, конструктору болсун, талааларына инкапсуляция принсибин колдонгула
    Функция жазыңыз ага аргумент берилгене ошону экранга чыгарып берсин
"""
# class Computer:
#     def __init__(self, name, marka, date, OC):
#         self.__name = name
#         self.__marka = marka
#         self.__date = date
#         self.__OC = OC
#
#     def info(self):
#         print(f"name: {self.__name}\n"
#               f"marka: {self.__marka}\n"
#               f"date: {self.__date}\n"
#               f"OC: {self.__OC}")
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, Asus):
#         self.__name = Asus
#
#     def get_marka(self):
#         return self.__name
#
#     def set_marka(self, newMarka):
#         self.__marka = newMarka
#
#     def get_date(self):
#         return self.__date
#
#     def set_date(self, newDate):
#         self.__date = newDate
#
#     def get_OC(self):
#         return self.__OC
#
#     def set_OC(self, newOC):
#         self.__OC = newOC
#
# asus = Computer("Asus", '600c', '19.09.2022', 'Windows')
# asus.set_OC('freeBSD')
# asus.set_date('20.12.2022')
# asus.set_marka('Hp')
# asus.set_name("MI")
# asus.info()

# def check_speed(speed):
#     if speed > 240:
#         print("Error !!!")
#     else:
#         return speed
#
# class Track:
#     def __init__(self, model, capacity, newSpeed):
#         self.__model = model
#         self.__capacity = capacity
#         self.__speed = check_speed(newSpeed)
#
#     def show_info(self):
#         print(f"Model: {self.__model}\n"
#               f"Capacity: {self.__capacity}\n"
#               f"Speed: {self.__speed}"
#               )
#
#     def getModel(self):
#         return self.__model
#
#     def getCapacity(self):
#         return self.__capacity
#
#     def getSpeed(self):
#         return self.__speed
#
#     def setModel(self, newModel):
#         self.__model = newModel
#
#     def setCapacity(self, newCapacity):
#         self.__capacity = newCapacity
#
#     def setSpeed(self, newSpeed):
#         self.__speed = newSpeed
#
#
# kamaz = Track("Kamaz", 60000 ,240)
# kamaz.show_info()






###  тапшырма  ###
"""
    Transport классын түзүңүз, конструктору болсун, талаалрын жана методдорун жазыңыз,
    инкапсуляция принсибин колдонуңуз, эң аз 3 обект түзүңүз.
"""


class Transport:
    def __init__(self, name, marka, type, speed):
        self.__name = name
        self.__marka = marka
        self.__type = type
        self.__road_speed = speed

    def info_transport(self):
        print(f"Name: {self.__name}\n"
              f"Marka: {self.__marka}\n"
              f"Type: {self.__type}\n"
              f"Road_speed: {self.__road_speed}\n"
              f"---------------------------------"
              )



    def get_name(self):
        return self.__name

    def set_name(self, newName):
        self.__name = newName

    def get_marka(self):
        return self.__marka

    def set_marka(self, newMarka):
        self.__marka = newMarka

    def get_type(self):
        return self.__type

    def set_type(self, newType):
        self.__type = newType

    def get_road_speed(self):
        return self.__road_speed

    def set_road_speed(self, newRoad_speed ):
        self.__road_speed = newRoad_speed


car = Transport("BMW", "BMW E34", "car", "375 км/ч.")
aircraft = Transport("Самолёт", "Штурмовик Су-25", "Воздушный транспорт", "900 км/ч. ")
train = Transport("поезд", "Фирменные поезда", "Перспективные виды транспорта", "38 км/ч,")



