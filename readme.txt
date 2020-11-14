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
        main function with input control
        look in the performance file for altitude table
        presetting corresponding to the best economy
            CRITERIA:
            Biggest Range
            (if equal) Fastest
            (if equal) Lowest RPM
        presetting corresponding to the best economy
            CRITERIA:
            Fastest
            (if equal) Biggest Range
            (if equal) Lowest RPM
        range remaining
        cost index integration v.1:
            input a ci between 0 (most range) and 100 (fastest)
    Planned:
        cost index integration v.2:
            input a fuel cost, a time cost as well as a cruise distance
    ###Possible extensions###
        custom presetting when inputted an altitude that isn't in the table (linear regression)
        TB20 port