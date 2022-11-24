# Создайте абстрактный класс автомобиля Transport c абстрактными методами
# - start_engine
# - stop_engine
# - move
# - stop

# Унаследуйте от него три класса Boat, Car, Electroscooter
# для каждого из требуемых методов через print укажите какое-либо действие.
# К примеру start_engine -> print('Двигатель катера запущен')

# Создайте класс Person у которого будет один единственный метод use_transport.
# В данный метод в качестве параметра должен передаваться объект реализующий интерфейс Transport
# Метод для этого объекта должен запускать двигатель, двигаться куда-то, тормозить и глушить двигатель.
# Для текстовой анимации Вы можете использовать любые фразы, или воспользоваться нашей подборкой:
# Boat:
#    - Катер громко затарахтел
#    - Двигатель катера чихнул напоследок и заглох
#    - Катер быстро набирает скорость
#    - Катер остановился
# Car:
#    - Машина заурчала двигателем
#    - Машина стоит с заглушенным двигателем
#    - Машина едет к цели назначения
#    - Машина остановилась
# Electroscooter:
#    - Мигнул светодиодом
#    - Мигнул светодиодом дважды
#    - Прохожие в ужасе разбегаются от очередного камикадзе
#    - Торможение об стену прошло успешно


# Корректным решением будет когда экземпляр класса Person смог использовать все три различных транспорта

# в решении класс Transport должен быть унаследован от ABC
# все методы Transport должны быть помечены декоратором @abstractmethod
# Классы Boat, Car, Electroscooter должны быть унаследованы от Transport

# экземпляр класса Person должен поочередно взаимодействовать с объектами Car, Boat, Electroscooter

# код должен выполняться не выбрасывая исключений

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def start_engine(self): 
        ...
    
    @abstractmethod
    def stop_engine(self): 
        ...
    
    @abstractmethod
    def move(self): 
        ...

    @abstractmethod
    def stop(self): 
        ...

class Boat(Transport): 
    def start_engine(self):
        print("Boat start engine")
        
    def stop_engine(self):
        print("Boat stop engine")
    
    def move(self):
        print("Boat move...")
    
    def stop(self):
        print("Boat stop")
 
class Car(Transport): 
    def start_engine(self):
        print("Car start engine")
        
    def stop_engine(self):
        print("Car stop engine")
    
    def move(self):
        print("Car move...")
    
    def stop(self):
        print("Car stop")

class Electroscooter(Transport): 
    def start_engine(self):
        print("Electroscooter start engine")
        
    def stop_engine(self):
        print("Electroscooter stop engine")
    
    def move(self):
        print("Electroscooter move...")
    
    def stop(self):
        print("Electroscooter stop")


class Person:
    
    def use_transport(self, transport: Transport):
        transport.start_engine()
        transport.move()
        transport.stop()
        transport.stop_engine()

# Отрезок кода для самопроверки.
# Запустите его, после того как выполните задание
if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikadze = Electroscooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 10)
    person.use_transport(car)
    print('=' * 10)
    person.use_transport(kamikadze)