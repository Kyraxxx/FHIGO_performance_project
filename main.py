import calculator


if __name__ == '__main__':
    while True:
        choice = input(
            "F-HIGO Performance calculator\n"
            "[1] Best economy\n"
            "[2] Best speed\n")
        if choice == '1' or choice == '2':
            break
        print("Wrong Input! Enter the number corresponding to the option you need")
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
        usr_fuel = input("Enter the fuel on board\n")
        try:
            fuel = float(usr_fuel)
            if fuel < 7 or fuel > 88:
                raise ValueError
            break
        except ValueError:
            print("Value Error! The FOB must be a value between 7 USG and 88 USG")
    if choice == '1':
        preset = calculator.best_eco(alt)
    if choice == '2':
        preset = calculator.best_spd(alt)
    remaining_range = int(((fuel - 7)/88)*preset.rng)
    print("At {}ft in standard conditions, no wind:\n"
          "PRESETTING: {} in.Hg {} RPM {} USG/H TAS {} kts\n"
          "Range before final reserve {} Nm"
          .format(alt, preset.map, preset.rpm, preset.gph, preset.tas, remaining_range))
    input("\npress ENTER to continue")
