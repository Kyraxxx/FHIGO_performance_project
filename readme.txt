_______________________________________ [ F-HIGO cruise presettings calculator] _______________________________________

This program uses the flight manual cruise performance tables to give the user a presetting based on several parameters.
These presettings are based on Best Performance criteria

How it works:
    First the user will input their cruise conditions (such as altitude)
    The program will then open a file containing the performance tables of the plane and load the presettings
    corresponding with the cruise conditions
    Then it will select the presetting with the best performance (the range)
    Then it will output this presetting to the user

list of functions:
    Implemented:
        main function with input and output
        input control
        look in the performance file
        extract presetting corresponding to the best performance
            CRITERIA:
            Biggest Range
            (if equal) Fastest
            (if equal) Biggest RPM (to avoid excessive torque)

    ###Possible extensions###
        range & time remaining calculation (new input: fuel remaining)
        custom presetting when inputted an altitude that isn't in the table (linear regression)
        choosing best performance vs. best speed (menu and 2 separate calulator functions in isolated file)
        cost index integration
        climb perf integration
        T/O & LDG dist. calculator integration