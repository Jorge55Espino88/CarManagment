from datetime import datetime

class Car:
    car_counted = 0
    CAR_TYPES = ["Sedan", "Hatchback", "SUV", "Pickup", "Sports Car"]

    def __init__(self, name, model, year, brand, color, number_doors, motor, type):
        if not name:
            raise ValueError("Name cannot be empty")
        if not model:
            raise ValueError("Model cannot be empty")
        if not isinstance(year, int):
            raise ValueError("Year must be an integer")
        elif year < 1900 or year > datetime.now().year:
            raise ValueError("Year must be between 1900 and current year")
        if not brand:
            raise ValueError("Brand cannot be empty")
        if not color:
            raise ValueError("Color cannot be empty")
        if not isinstance(number_doors, int):
            raise ValueError("Number doors must be an integer")
        elif number_doors < 2 or number_doors > 4:
            raise ValueError("Number doors must be between 2 and 4")
        if not motor:
            raise ValueError("Motor cannot be empty")
        if not type:
            raise ValueError("Type cannot be empty")
        elif type not in Car.CAR_TYPES:
            raise ValueError("Invalid type of car. Type must be one of the following: " + ", ".join(Car.CAR_TYPES))

        self.__name = name
        self.__model = model
        self.__year = year
        self.__brand = brand
        self.__color = color
        self.__number_doors = number_doors
        self.__motor = motor
        self.__type = type

        date_created = datetime.now()
        id_suffix = f"{name[:3].lower()}{model[:3].lower()}{str(year)[-2:]}"
        date_string = f"{date_created.year}{date_created.month:02d}{date_created.day:02d}"
        Car.car_counted += 1
        self.__id = f"{date_string}-{id_suffix}-{Car.car_counted}"

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self.__name = value

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, value):
        if not value:
            raise ValueError("Model cannot be empty")
        self.__model = value

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year must be an integer")
        elif value < 1900 or value > datetime.now().year:
            raise ValueError("Year must be between 1900 and current year")
        self.__year = value

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, value):
        if not value:
            raise ValueError("Brand cannot be empty")
        self.__brand = value

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, value):
        if not value:
            raise ValueError("Color cannot be empty")
        self.__color = value

    @property
    def number_doors(self):
        return self.__number_doors
    @number_doors.setter
    def number_doors(self, value):
        if not isinstance(value, int):
            raise ValueError("Number door must be an integer")
        elif value < 2 or value > 4:
            raise ValueError("Number door must be between 2 and 4")
        self.__number_doors = value

    @property
    def motor(self):
        return self.__motor
    @motor.setter
    def motor(self, value):
        if not value:
            raise ValueError("Motor cannot be empty")
        self.__motor = value

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, value):
        if not value:
            raise ValueError("Type cannot be empty")
        elif value not in Car.CAR_TYPES:
            raise ValueError("Invalid type of car. Type must be one of the following: " + ", ".join(Car.CAR_TYPES))

    def __str__(self):
        return f"""Id: {self.__id}
Name: {self.__name}
Model: {self.__model}
Year: {self.__year}
Brand: {self.__brand}
Color: {self.__color}
Motor: {self.__motor}
Type: {self.__type}
Number doors: {self.__number_doors}"""
