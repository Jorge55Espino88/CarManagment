from car import create_car
cars = []

def add_car():
    name = input("Name of car: ")
    model = input("Model of car: ")
    year = input("Year of car: ")
    brand = input("Brand of car: ")
    color = input("Color of car: ")

    try:
        car = create_car(name,model,year,brand,color)
        cars.append(car)
        print("Car created successfully")
    except Exception as e:
        print(f"Something went wrong: {e}")

def show_cars():
    print("List of cars:")
    for car in cars:
        print_car(car)

def print_car(car):
    id = car["Id"]
    name = car["Name"]
    model = car["Model"]
    year = car["Year"]
    brand = car["Brand"]
    color = car["Color"]
    print(f"""Id = {id}
Name = {name}
Model = {model}
Year = {year}
Brand = {brand}
Color = {color}
""")

def search_car():
    car_id = input("Please enter the Id of car: ")
    for car in cars:
        if car["Id"] == car_id:
            print_car(car)
            return

    print(f"Car with {car_id} not found")

def delete_car():
    id = input("Enter the Id of the car to delete: ")
    for car in cars:
        if car["Id"] == id:
            cars.remove(car)
            print("Car deleted successfully")
            return
    print("Car not found")

if __name__ == '__main__':
    add_car()
    add_car()
    show_cars()