# class Transport:
#     def __init__(self, name, marka, type, speed):
#         self.__name = name
#         self.__marka = marka
#         self.__type = type
#         self.__road_speed = speed
#
#     def info_transport(self):
#         print(f"Name: {self.__name}\n"
#               f"Marka: {self.__marka}\n"
#               f"Type: {self.__type}\n"
#               f"Road_speed: {self.__road_speed}\n"
#               f"---------------------------------"
#               )
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, newName):
#         self.__name = newName
#
#     def get_marka(self):
#         return self.__marka
#
#     def set_marka(self, newMarka):
#         self.__marka = newMarka
#
#     def get_type(self):
#         return self.__type
#
#     def set_type(self, newType):
#         self.__type = newType
#
#     def get_road_speed(self):
#         return self.__road_speed
#
#     def set_road_speed(self, newRoad_speed):
#         self.__road_speed = newRoad_speed
#
#
#
# class Track(Transport):
#     def __init__(self, name, marka, type, speed, gross_vehicle_weight):
#         super().__init__(name, marka, type, speed)
#
#         self.__gross_vehicle_weight = gross_vehicle_weight
#
#     def get_gross_vehicle_weight(self):
#         return self.__gross_vehicle_weight
#
#     def set_gross_vehicle_weight(self, newGross_vehicle_weight):
#         self.__gross_vehicle_weight = newGross_vehicle_weight
#
#     def info_transport(self):
#         super().info_transport()
#         print(f"Gross_vehicle_weight: {self.__gross_vehicle_weight}\n"
#               f"--------------------------------------\n")
#
#
# class Car(Transport):
#     def __init__(self, name, marka, type, speed, mechanic_automatic):
#         super().__init__(name, marka, type, speed)
#
#         self.__mechanic_automatic = mechanic_automatic
#
#     def get_mechanic_automatic(self):
#         return self.__mechanic_automatic
#
#     def set_mechanic_automatic(self, newMechanic_automatic):
#         self.__mechanic_automatic = newMechanic_automatic
#
#     def info_transport(self):
#         super().info_transport()
#         print(f"Mechanic_automatic: {self.__mechanic_automatic}\n"
#               f"--------------------------------------\n")
#
#
# class Aircraft(Transport):
#     def __init__(self, name, marka, type, speed, including_engine):
#         super().__init__(name, marka, type, speed)
#
#         self.__including_engine = including_engine
#
#     def get_including_engine(self):
#         return self.__including_engine
#
#     def set_including_engine(self, newIncluding_engine):
#         self.__including_engine = newIncluding_engine
#
#     def info_transport(self):
#         super().info_transport()
#         print(f"Including_engine: {self.__including_engine}\n"
#               f"--------------------------------------\n")
#
# track = Track("Грузовик", "Type", "Седельный тягач", "Кузов специального назначения", "18 тонн")
# car = Car("BMW", "BMW E34", "car", "375 км/ч.", "automatic")
# aircraft = Aircraft("Самолёт", "Штурмовик Су-25", "Воздушный транспорт", "900 км/ч.", "трёхдвигательные (Як-42, DC-10)")

a = input("Атынызды жазыныз: ")
a.power()
b = len(a)
print(b)







