import uuid

def create_car(name, model, year, brand, color):
    car = {
        "Id": str(uuid.uuid4()),
        "Name": name,
        "Model": model,
        "Year": year,
        "Brand": brand,
        "Color": color
    }
    return car



if __name__ == '__main__':
    car = create_car("C300","SSM3","1989","Chrysler","blue")
