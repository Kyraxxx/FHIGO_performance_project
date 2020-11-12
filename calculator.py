import json


class Presetting(object):

    def __init__(self, MAP, RPM, GPH, TAS, RNG):
        self.map = MAP
        self.rpm = RPM
        self.gph = GPH
        self.tas = TAS
        self.rng = RNG


def lookup_alt(alt: int) -> list:
    key = alt - alt % 2500
    if key == 0:
        key = 2500
    with open('performance.txt') as f:
        file = f.read()
    perf_dict = json.loads(file)
    return perf_dict[str(key)]


def best_eco(altitude: int) -> Presetting:
    perf_array = lookup_alt(altitude)
    perf_array.sort(key=lambda line: line[-1], reverse=True)
    high_economy = [param for param in perf_array if param[-1] == perf_array[0][-1]]
    if len(high_economy) > 1:
        high_economy.sort(key=lambda line: line[-2], reverse=True)
        high_economy = [param for param in high_economy if param[-2] == high_economy[0][-2]]
    best_economy = sorted(high_economy, key=lambda line: line[1])[0]
    return Presetting(best_economy[0], best_economy[1], best_economy[2], best_economy[3], best_economy[4])


def best_spd(altitude: int) -> Presetting:
    perf_array = lookup_alt(altitude)
    perf_array.sort(key=lambda line: line[-2], reverse=True)
    high_speed = [param for param in perf_array if param[-2] == perf_array[0][-2]]
    if len(high_speed) > 1:
        high_speed.sort(key=lambda line: line[-1], reverse=True)
        high_speed = [param for param in high_speed if param[-1] == high_speed[0][-1]]
    best_speed = sorted(high_speed, key=lambda line: line[1])[0]
    return Presetting(best_speed[0], best_speed[1], best_speed[2], best_speed[3], best_speed[4])
