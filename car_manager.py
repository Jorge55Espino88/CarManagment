from car import Car

class CarManager:
    def __init__(self):
        self.__cars = []

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError("car must be an instance of Car")
        self.__cars.append(car)
        return

    def get_cars(self):
        if not self.__cars:
            raise ValueError("No cars in list")
        return self.__cars

    def show_cars(self):
        if not self.__cars:
            print("No cars to show")
            return
        for car in self.__cars:
            print(car)

    def get_car_by_id(self, search_car_id):
        if not self.__cars:
            return None
        for car in self.__cars:
            if car.id == search_car_id:
                return car
        return None

    def remove_car(self, search_car_id):
        if not self.__cars:
            print("No cars to remove")
            return

        for car in self.__cars:
            if car.id == search_car_id:
                self.__cars.remove(car)
                print("Car removed successfully")
                return
        print("No car found")
        return

if __name__ == '__main__':
    car_manager = CarManager()
    car1 = Car(name="C300", model="45rf", year=2000,brand="Chrysler", color="red",number_doors=4, motor="VVFGV", type="SUV")
    car2 = Car(name="C400", model="45f", year=2010,brand="Chrysler", color="blue",number_doors=4, motor="VVFGV", type="SUV")

    car_manager.add_car(car1)
    car_manager.add_car(car2)
    print()
    car_manager.show_cars()
    print()
    car_manager.get_car_by_id("20260110-c4045f10-2")
    print()
    car_manager.remove_car("20260110-c4045f10-2")
