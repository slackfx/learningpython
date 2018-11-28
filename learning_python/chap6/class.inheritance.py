class Engine():
    def start(self):
        pass

    def stop(self):
        pass

class EletricEngine(Engine):
    pass

class V8Engine(Engine):
    pass

class Car():
    engine_cls = Engine

    def __init__(self):
        self.engine = self.engine_cls()

    def start(self):
        print('Starting engine {0} for car {1}...'.format(self.engine.__class__.__name__, self.__class__.__name__))
        self.engine.start()

    def stop(self):
        self.engine.stop()

class RaceCar(Car):
    engine_cls = V8Engine

class CityCar(Car):
    engine_cls = EletricEngine

class F1Car(RaceCar):
    engine_cls = V8Engine

car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()

cars = [car, racecar, citycar, f1car]

for car in cars:
    car.start()

cars2 = [(car, 'car'), (racecar, 'racecar'), (f1car, 'f1car')]
car_classes = [Car, RaceCar, F1Car]

for car2, car_name in cars2:
    for class_ in car_classes:
        belongs = isinstance(car2, class_)
        msg = 'is a' if belongs else 'is not a'
        print(car_name, msg, class_.__name__)
