from manager import Manager

mg = Manager()
print("*** Car Manager ***")

name = input("Enter your namer: ")
exit = False


def manage_option(option):
    match option:
        case 1:
            mg.cm_add_car()
        case 2:
            mg.cm_show_cars()
        case 3:
            mg.cm_search_car()
        case 4:
            mg.cm_remove_car()
        case 5:
            mg.sm_add_service()
        case 6:
            mg.sm_show_services()
        case 7:
            mg.sm_search_services()
        case 8:
            mg.sm_remove_service()
        case 9:
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
    5. Create a new service
    6. Show services
    7. Search for a service
    8. Delete a service
    9. Exit
    """)
    try:
        option = int(input("Enter your option: "))
        manage_option(option)
    except ValueError:
        print("Invalid option")




