import calculator


if __name__ == '__main__':
    print("F-HIGO cruise calculator\n")

    while True:
        usr_dist = input("Enter the cruise distance (in Nm)\n")
        try:
            distance = float(usr_dist)
            if distance < 0:
                raise ValueError
            break
        except ValueError:
            print("Value Error! The distance must be a value above 0Nm")

    while True:
        usr_alt = input("Enter the cruising altitude\n")
        try:
            alt = int(usr_alt)
            if alt < 0 or alt > 15000:
                raise ValueError
            break
        except ValueError:
            print("Value Error! The altitude must be a whole number between 0 and 15000")

    while True:
        usr_fuel = input("Enter the fuel cost (in €/USG)\n")
        try:
            fuel_cost = float(usr_fuel)
            if fuel_cost < 0:
                raise ValueError
            break
        except ValueError:
            print("Value Error! The fuel cost must be a value above 0€/USG")

    while True:
        usr_cost = input("Enter the hour cost (in €/hr)\n")
        try:
            time_cost = float(usr_cost)
            if time_cost < 0:
                raise ValueError
            break
        except ValueError:
            print("Value Error! The time cost must be a value above 0€/hr")

    cruise = calculator.cruise_planner(distance, alt, time_cost, fuel_cost)
    print(cruise)
    input("\npress ENTER to continue")
