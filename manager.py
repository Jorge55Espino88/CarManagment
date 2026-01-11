from car import Car
from car_manager import CarManager
from service import Service
from service_manager import ServiceManager


class Manager:
    def __init__(self):
        self.car_manager = CarManager()
        self.service_manager = ServiceManager()

    def cm_add_car(self):
        print("Available car types:")
        for type_car in Car.CAR_TYPES:
            print(f"- {type_car}")

        while True:
            try:
                #Retrieve the data entered by the user
                name_var = input("Name of the car: ").strip()
                model = input("Model: ").strip()
                year = int(input("Year: ").strip())
                brand = input("Brand: ").strip()
                color = input("Color: ").strip()
                number_doors = int(input("Number of doors: ").strip())
                motor = input("Motor: ").strip()
                type_car = input("Type car: ").strip()

                car = Car(name_var, model, year, brand, color, number_doors, motor, type_car)
                self.car_manager.add_car(car)
                return
            except ValueError as e:
                print(f"Error: {e}")
            except KeyboardInterrupt as e:
                print(f"Operation cancelled")
                return

    def cm_show_cars(self):
        return self.car_manager.show_cars()

    def cm_search_car(self):
        # Retrieve the data entered by the user
        id_car = input("Enter car ID: ").strip()
        car = self.car_manager.get_car_by_id(id_car)
        if car:
            print(car)
        else:
            print("No car found")

    def cm_remove_car(self):
        # Retrieve the data entered by the user
        id_car = input("ID of the car: ").strip()
        cars = self.car_manager.get_cars()
        for car in cars:
            if car.id == id_car:
                self.car_manager.remove_car(car)
                print("Car removed successfully")
                return

        print("Car not found")
        return


    def sm_add_service(self):
        while True:
            try:
                # Retrieve the data entered by the user
                name_var = input("Name of the service: ").strip()
                description_var = input("Description: ").strip()
                price = float(input("Price: ").strip())

                service = Service(name_var, description_var, price)
                self.service_manager.add_service(service)
                return
            except ValueError as e:
                print(f"Error: {e}")
            except KeyboardInterrupt as e:
                print(f"Operation cancelled")
                return

    def sm_show_services(self):
        return self.service_manager.show_services()

    def sm_search_services(self):
        # Retrieve the data entered by the user
        id_var = input("Enter service ID: ").strip()
        service = self.service_manager.get_service_by_id(id_var)
        if service:
            print(service)
        else:
            print("No service found")


        print("No service found")
        return False

    def sm_remove_service(self):
        # Retrieve the data entered by the user
        id_var = input("ID of the service: ").strip()
        services = self.service_manager.get_services()
        for service in services:
            if service.id == id_var:
                self.service_manager.remove_service(service)
                print("Service removed successfully")
                return

        print("Service not found")
        return False

if __name__ == '__main__':
    manager = Manager()

    # Cars
    # manager.cm_add_car()
    # manager.cm_add_car()
    # print()
    # manager.cm_show_cars()
    # print()
    # manager.cm_search_car()
    # print()
    # manager.cm_remove_car()

    # Services
    manager.sm_add_service()
    print()
    manager.sm_add_service()
    print()
    print()
    manager.sm_show_services()
    print()
    print()
    manager.sm_search_services()
    print()
    print()
    manager.sm_remove_service()
    print()
