import json


class Presetting(object):

    def __init__(self, MAP, RPM, GPH, TAS):
        self.map = MAP
        self.rpm = RPM
        self.gph = GPH
        self.tas = TAS


def preset_calculator(altitude: int) -> Presetting:
    key = altitude - altitude % 2500
    if key == 0:
        key = 2500
    with open('performance.txt') as f:
        file = f.read()
    perf_dict = json.loads(file)
    perf_array = perf_dict[str(key)]
    perf_array.sort(key=lambda line: line[-1], reverse=True)
    high_economy = [param for param in perf_array if param[-1] == perf_array[0][-1]]
    if len(high_economy) > 1:
        high_economy.sort(key=lambda line: line[-2], reverse=True)
        high_economy = [param for param in high_economy if param[-2] == high_economy[0][-2]]
    best_economy = sorted(high_economy, key=lambda line: line[1], reverse=True)[0]
    return Presetting(best_economy[0], best_economy[1], best_economy[2], best_economy[3])


if __name__ == '__main__':
    while True:
        usr_input = input("Enter the cruising altitude\n")
        try:
            alt = int(usr_input)
            if alt < 0 or alt > 15000:
                raise ValueError
            break
        except ValueError:
            print("Value Error! The altitude must be a whole number between 0 and 15000")
    preset = preset_calculator(alt)
    print("At {}ft in standard conditions, no wind:\n"
          "PRESETTING: {} in.Hg {} RPM {} USG/H TAS {} kts".format(alt, preset.map, preset.rpm, preset.gph, preset.tas))
