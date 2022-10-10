###    ООП   ###

"""
    Объектке багытталган программалоо (OOП) бул программалоо парадигмасы, мында компьютердик программанын
    ар кандай компоненттери реалдуу объекттерде моделделет. Объект - бул кандайдыр бир өзгөчөлүктөргө ээ
    болгон жана кандайдыр бир функцияны аткара алган нерсе.
"""

##  Кошумча булактар : https://python-scripts.com/object-oriented-programming-in-python#method-overloading

####  Класс  ####
"""
    Объектке багытталган программалоодо класс объект үчүн план катары иштейт.
    Классты үйдүн картасы катары кароого болот.Анын картасын карап эле үйдүн кандай экенин биле аласыз.

    NOTE:
        Класс өзү эч нерсени билдирбейт. Мисалы, картаны үй деп айтууга болбойт, ал чыныгы үй кандай болушу керек экенин гана түшүндүрөт.
"""


class Car:
    name = "c200"
    marka = "mercedes"
    model = 2008

    def start(self):
        print("Кыймылдаткычты от алдыруу")

    def stop(self):
        print("Кыймылдаткычты өчүрүү")


"""
    анын ыкмаларын жана атрибуттарын колдонуудан мурун класстын
    объектин түзүшүбүз керек экенин унутпаңыз.

    класс объектисин түзүү процесси инициализация деп аталат. Pythonдо класс 
    объектисин түзүү үчүн класстын атын теришибиз керек, андан кийин кашааларды ачып, 
    жабуу керек.

    Car классынын объектисин түзөлү.
"""

car_1 = Car()
car_2 = Car()

"""
    Бул скриптте биз Car классынын эки объектисин түздүк: 
    Алар car_1 жана car_2. Биз түзгөн объекттердин түрүн билүү үчүн, 
    биз type ыкмасын колдонобуз.
"""
# print(type(car_1))

"""
    Бул учурда, биз классыбызды жана ага тиешелүү объекттерди түздүк. 
    Эми класстын атрибуттарына жетүү жана класс объектисин колдонуу 
    менен класс ыкмасын чакырууга убакыт келди. Бул үчүн объекттин атын, 
    андан кийин чекит оператору менен сиз  атрибуттун же ыкманын аталышы
    жазып ошол атрибутка жете аласыз
"""


# print("Car классынын атрибуттарын текшерели: ")
# print(car_1.name)
# print(car_1.model)
# print(car_1.marka)
# car_1.start()
# car_1.stop()

# class Human:
#     name = 'Belek'
#     surname = 'Asrarov'
#     age = 23
#     gender = 'male'
#     height = '170 cm'
#
#     def say(self):
#         print(f"{self.name} is saying.")
#
#     def walk(self):
#         print(f"{self.name} is going.")
#
#     def drink(self):
#         print(f"{self.name} is drinking.")
#
# belek = Human()
# print(belek.name)
# print(belek.surname)
# print(belek.age)
# print(belek.height)
# belek.walk()
# belek.say()
# belek.drink()


# class People:
#     name = "Feruza"
#     surname = "kairatbekova"
#     age = 19
#     height = 160
#     gender = "woman"
#     place_of_study = "Manas university"
#
#     def display_info(self):
#         print(f"Name: {self.name}\nSurname: {self.surname}\n"
#               f"Age: {self.age}\nHeight: {self.height}\n"
#               f"Gender: {self.gender}\nPlace_of_stydy: {self.place_of_study}"
#               )
#
#     def to_sing(self):
#         print(f"{self.name} can sing")
#
#     def watch_series(self):
#         print(f"{self.name} loves to watch Korean drama")
#
#     def dance(self, dance):
#         print(f"{self.name} can dance {dance}")
#
#     def to_cook(self, food):
#         print(f"{self.name} is cooking {food}")
#
#
# fer = People()
# fer.display_info()
# fer.to_cook('Besh barmak')
# fer.dance('shuffle')

###  коструктор ###


# class People:
#
#     def __init__(self, newName, newSurname, newAge, newGender):
#         self.name = newName
#         self.surname = newSurname
#         self.age = newAge
#         self.gender = newGender
#
#
# feruza = People("Feruza", "Kayratbekova", 19, 'fmale')
# aydana = People("Aydana", "Begimatova", 22, 'fmale')
# belek = People("Belek", "Asrarov", 21, 'male')
#
# print(feruza.name)
# print(aydana.name)
# print(belek.name)

###   Тапшырма  ####

"""
    Animal классын түзүп келгиле
    1. Конструктору жок кандайдыр жаныбарга багытталсын
    2. Коструктору менен болсун ар кандай жаныбардын обектисин түзүү мүмкүнчүлүгү болсун (Универсалдуу)
    Экитен класстын талааларын жана методдорун жазгыла
"""

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
# cat = Animal()
# cat.info_animal()



# class Animal:
#
#     def __init__(self, type_animal, name, age, color_cat, types_of_cat):
#         self.type_animal = type_animal
#         self.name = name
#         self.age = age
#         self.color_cat = color_cat
#         self.types_of_cat = types_of_cat
#
# dog = Animal("dog", "Боби", 2, "black", "Акита-ину")
# bird = Animal("bird", "Eurasian bittern", 1.5, "green", "Фламингообразные")
#
# print(dog.type_animal, dog.name, dog.age, dog.color_cat, dog.types_of_cat)
# print(bird.type_animal, bird.name, bird.age, bird.color_cat, bird.types_of_cat)

# a = "Привет, мир!"
# print(f"str тиби: {a}")

# a = 12.5
# b = 4.0
# print(f"float тиби: {a + b}")

# a = 5
# b = 15
# print(f"Integer тиби: {a + b}")

# a = 10
# b = 0
# c = a > b
# print(f"bool тиби: {c}")

# a = [1, 2, 3, 4, 10, 145]
# a.append(5)
# print(a)
#
# b = {name: Feruza, surname: Kairatbekova, age: 19}
# print(b)
#
# c = (12, 3, 1, 56, 38, 49, 5, 5)
# print(c)
#
#
# v = {12, 3, 1, 56, 38, 49, 5, 5}
# print(v)

# def func(a):
#     print(a)
#
# func(5)

class Animal:
    def __init__(self, name, age, color, types):
        self.__name = name
        self.__age = age
        self.__color = color
        self.__types = types

    def info_animal(self):
        print(f"Name: {self.__name}\n"
              f"Age: {self.__age}\n"
              f"Color: {self.__color}\n"
              f"Types: {self.__types}\n"
              f"----------------------\n"
              )

    def get_name(self):
        return self.__name

    def set_name(self, newName):
        self.__name = newName

    def get_age(self):
        return self.__age

    def set_age(self, newAge):
        self.__age = newAge

    def get_color(self):
        return self.__color

    def set_color(self, newColor):
        self.__color = newColor

    def get_types(self):
        return self.__types

    def set_types(self, newTypes):
        self.__types = newTypes


class Dog(Animal):
    def __init__(self, name, age, color, types, run):
        super().__init__(name, age, color, types)
        self.__run = run

    def get_run(self):
        return self.__run

    def set_run(self, newRun):
        self.__run = newRun

    def info_animal(self):
        super().info_animal()
        print(f"Run: {self.__run}\n")

class Cat(Animal):
    def __init__(self, name, age, color, types, sleep):
        super().__init__(name, age, color, types)
        self.__sleep = sleep

    def get_sleep(self):
        return self.__sleep

    def set_sleep(self, newSleep):
        self.__sleep = newSleep

    def info_animal(self):
        super().info_animal()
        print(f"Sleep: {self.__sleep}\n"
              )


class Eagle(Animal):
    def __init__(self, name, age, color, types, fly):
        super().__init__(name, age, color, types)
        self.__fly = fly

    def get_fly(self):
        return self.__fly

    def set_fly(self, newFly):
        self.__fly = newFly

    def info_animal(self):
        super().info_animal()
        print(f"Fly: {self.__fly}\n"
              )


dog = Dog("Боби", "1", "white", "Акита-ину", "32 км/ч")
dog.info_animal()

cat = Cat("Боби", "1", "white", "Акита-ину", "32 км/ч")
cat.info_animal()

eagle = Eagle("Боби", "1", "white", "Акита-ину", "32 км/ч")
eagle.info_animal()