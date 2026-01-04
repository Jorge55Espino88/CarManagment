import manager as mg

print("*** Car Manager ***")

name = input("Enter your namer: ")
exit = False


def manage_option(option):
    match option:
        case 1:
            mg.add_car()
        case 2:
            mg.show_cars()
        case 3:
            mg.search_car()
        case 4:
            mg.delete_car()
        case 5:
            print(f"See you soon {name}")
            return True
        case _:
            print("Invalid option")
            return False


while not exit:
    print(f"""Welcome to Car Manager!
    Here is your menu {name}:
    1. Create a new car
    2. Show all cars
    3. Search for a car
    4. Delete a car
    5. Exit
    """)
    try:
        option = int(input("Enter your option: "))
        manage_option(option)
    except ValueError:
        print("Invalid option")




