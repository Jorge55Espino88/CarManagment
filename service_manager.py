from service import Service

class ServiceManager:
    def __init__(self):
        self.__services = []


    def get_services(self):
        return self.__services

    def add_service(self, service):
        if not isinstance(service, Service):
            raise TypeError("service must be an instance of Service")
        self.__services.append(service)
        return True

    def show_services(self):
        if not self.__services:
            print("No services to show")
            return False
        for service in self.__services:
            print(service)
        return True

    def get_service_by_id (self, service_id):
        if not self.__services:
            print("No services to search")
            return None
        for service in self.__services:
            if service.service_id == service_id:
                return service
        print("No services found")
        return None

    def remove_service(self, service_id):
        if not self.__services:
            print("No services to remove")
            return
        for service in self.__services:
            if service.service_id == service_id:
                self.__services.remove(service)
                print("Service removed successfully")
                return
        print("No services found")
        return

if __name__ == '__main__':
    service_manager = ServiceManager()

    service_manager.add_service(Service("Motor", "New Motor", 333.32))
    service_manager.add_service(Service("Aceite", "Nivelado del aceite", 33.32))
    print()
    service_manager.show_services()
    print()