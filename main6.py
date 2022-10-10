

# class Transport:
#     def __init__(self, name, marka, year):
#         self.__name = name
#         self.__marka = marka
#         self.__year = year
#
#     def getMarka(self):
#         return self.__marka
#
#     def getYear(self):
#         return self.__year
#
#     def getName(self):
#         return self.__name
#
#     def setName(self, newName):
#         self.__name = newName
#
#     def start(self):
#         print(f"{self.getName()} is starting!")
#
#     def stop(self):
#         print(f"{self.getName()} stoped!")
#
#
# class Car(Transport):
#     def __init__(self, name, marka, year, speed, capacity):
#         super().__init__(name, marka, year)
#         self.__speed = speed
#         self.__capacity = capacity
#
#     def getSpeed(self):
#         return self.__speed
#
#     def getCapacity(self):
#         return self.__capacity
#
#     def setSpeed(self, newSpeed):
#         self.__speed = newSpeed
#
#     def setCapacity(self, newCapacity):
#         self.__capacity = newCapacity
#
#     def play_music(self):
#         print(f"Music is playing")
#
#
# class Track(Transport):
#     def __init__(self, name, marka, year, speed, capacity):
#         super().__init__(name, marka, year)
#         self.__speed = speed
#         self.__capacity = capacity
#
#     def getSpeed(self):
#         return self.__speed
#
#     def getCapacity(self):
#         return self.__capacity
#
#     def setSpeed(self, newSpeed):
#         self.__speed = newSpeed
#
#     def setCapacity(self, newCapacity):
#         self.__capacity = newCapacity
#
#
# tesla = Car("Tesla", "S", 2022, "240km/h", 4)
# bmw = Car("BMW", 240, 2022, "250km/h", 4)
# kamaz = Track("Kamaz", 'kamaz', 2019, '100km/h', 20)
#
# bmw.start()
# tesla.start()
# kamaz.start()
#
# bmw.stop()
# tesla.stop()
# kamaz.stop()

# """HOMEWORK"""
#
#


# class Transport:
#
#     def __init__(self, name, model, data):
#         self.__name = name
#         self.__model = model
#         self.__data = data
#
#     def getName(self):
#         return self.__name
#
#     def getModel(self):
#         return self.__model
#
#     def getData(self):
#         return self.__data
#
#     def setName(self, newName):
#         self.__name = newName
#
#     def setModel(self, newModel):
#         self.__model = newModel
#
#     def setData(self, newData):
#         self.__data = newData
#
#     def info(self):
#         print(f'Name: {self.getName()}\n'
#               f'Model: {self.getModel()}\n'
#               f'Data: {self.getData()}'
#               )
#
#     def connect(self):
#         print(f'{self.getName()} can connect trailer.\n'
#               f'***************************************\n')
#
#     def pilot(self):
#         print(f'{self.getName()} has autopilot')
#
#
# class Track(Transport):
#     def __init__(self, name, model, data, country):
#         super(). __init__(name, model, data)
#         self.__country = country
#
#     def getCountry(self):
#         return self.__country
#
#     def setCountry(self, newCountry):
#         self.__country = newCountry
#
#     def drive(self):
#         print(f"{self.getName()} is driving!")
#
#     def info(self):
#         super().info()
#         print(f'Country: {self.getCountry()}')
#
#
# class Car(Transport):
#     def __init__(self, name, model, data, body):
#         super().__init__(name, model, data)
#         self.__body = body
#
#     def getBody(self):
#         return self.__body
#
#     def setBody(self, newBody):
#         self.__body = newBody
#
#     def drive(self):
#         print(f"{self.getName()} is driving!")
#
#     def info(self):
#         super().info()
#         print(f'Body: {self.getBody()}')
#
#
# class Airplane(Transport):
#     def __init__(self, name, model, data, firstFlight):
#         super().__init__(name, model, data)
#         self.__firstFlight = firstFlight
#
#     def getFirstFlight(self):
#         return self.__firstFlight
#
#     def setFirstFlight(self, newFirstFlight):
#         self.__firstFlight = newFirstFlight
#
#     def info(self):
#         super().info()
#         print(f'First Flight: {self.getFirstFlight()}')
#
#     def fly(self):
#         print(f'{self.getName()} is flying')
#
#
# track = Track('Man', 'TGA 18.480', '10.01.2002', 'Germany')
# track.setData('20.09.2001')
# print(f'CHARACTERISTC {track.getName()}:')
# track.info()
# track.connect()
#
# toyota = Car('Toyota', 'Camry 75', '02.02.2020', 'Sedan')
# toyota.setModel('Corolla')
# print(f'CHARACTERISTC {toyota.getName()}:')
# toyota.info()
# toyota.drive()
# toyota.pilot()
# toyota.connect()
#
# airplane = Airplane('Boeing', '737 MAX', '30.08.2011', '29.01.2016')
# airplane.setFirstFlight('13.07.2015')
# print(f'CHARACTERISTC {airplane.getName()}:')
# airplane.info()
# airplane.fly()



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

    def set_road_speed(self, newRoad_speed):
        self.__road_speed = newRoad_speed


class Track(Transport):
    def __init__(self, name, marka, type, speed, gross_vehicle_weight):
        super().__init__(name, marka, type, speed)

        self.__gross_vehicle_weight = gross_vehicle_weight

    def get_gross_vehicle_weight(self):
        return self.__gross_vehicle_weight

    def set_gross_vehicle_weight(self, newGross_vehicle_weight):
        self.__gross_vehicle_weight = newGross_vehicle_weight

    def info_transport(self):
        super().info_transport()
        print(f"Gross_vehicle_weight: {self.__gross_vehicle_weight}\n"
              f"--------------------------------------\n")


class Car(Transport):
    def __init__(self, name, marka, type, speed, mechanic_automatic):
        super().__init__(name, marka, type, speed)

        self.__mechanic_automatic = mechanic_automatic

    def get_mechanic_automatic(self):
        return self.__mechanic_automatic

    def set_mechanic_automatic(self, newMechanic_automatic):
        self.__mechanic_automatic = newMechanic_automatic

    def info_transport(self):
        super().info_transport()
        print(f"Mechanic_automatic: {self.__mechanic_automatic}\n"
              f"--------------------------------------\n")


class Aircraft(Transport):
    def __init__(self, name, marka, type, speed, including_engine):
        super().__init__(name, marka, type, speed)

        self.__including_engine = including_engine

    def get_including_engine(self):
        return self.__including_engine

    def set_including_engine(self, newIncluding_engine):
        self.__including_engine = newIncluding_engine

    def info_transport(self):
        super().info_transport()
        print(f"Including_engine: {self.__including_engine}\n"
              f"--------------------------------------\n")

    def fly(self):
        print(f"{self.get_name()} is flying")

track = Track("Грузовик", "Type", "Седельный тягач", "Кузов специального назначения",  "18 тонн")
track.info_transport()

car = Car("BMW", "BMW E34", "car", "375 км/ч.", "automatic")
car.info_transport()

aircraft = Aircraft("Самолёт", "Штурмовик Су-25", "Воздушный транспорт", "900 км/ч.", "трёхдвигательные (Як-42, DC-10)")
aircraft.fly()
aircraft.info_transport()