from datetime import datetime as dates

class Service:
    service_counter = 0

    def __init__(self, name, description, price):

        if not name:
            raise ValueError("Name cannot be empty")
        if not description:
            raise ValueError("Description cannot be empty")
        if not isinstance(price, float):
            raise ValueError("Price must be a float")
        elif price <= 0:
            raise ValueError("Price must be a positive float")

        self.__service_name = name
        self.__service_description = description
        self.__service_price = price

        date = dates.now()
        Service.service_counter += 1
        self.__service_id = F"{date.year}{date.month:02d}{date.day:02d}-{Service.service_counter}"

    @property
    def service_id(self):
        return self.__service_id

    @property
    def service_name(self):
        return self.__service_name
    @service_name.setter
    def service_name(self, value):
        if not value:
            raise ValueError("Service name cannot be empty")
        self.__service_name = value

    @property
    def service_description(self):
        return self.__service_description
    @service_description.setter
    def service_description(self, value):
        if not value:
            raise ValueError("Service description cannot be empty")
        self.__service_description = value

    @property
    def price(self):
        return self.__service_price
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("Service price must be a float")
        elif value < 0:
            raise ValueError("Service price must be a positive float")
        self.__service_price = value

    def __str__(self):
        return f"""Service ID: {self.__service_id}
Service name: {self.__service_name}
Service description: {self.__service_description}
Service price: ${self.__service_price:.2f}"""

if __name__ == '__main__':
    service1 = Service("Motor", "New Motor", 333.32)
    print(service1)


