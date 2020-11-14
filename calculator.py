import json


class Presetting(object):
    """

    Class used to store presettings from the performance file. Input a list [MAP, RPM, GPH, TAS, RNG]
    """
    def __init__(self, parameter_list: list):
        self.map = parameter_list[0]
        self.rpm = parameter_list[1]
        self.gph = parameter_list[2]
        self.tas = parameter_list[3]
        self.rng = parameter_list[4]

    def __eq__(self, other):
        return self.map == other.map and self.rpm == other.rpm and self.gph == other.gph

    def __repr__(self):
        return str([self.map, self.rpm, self.gph, self.tas, self.rng])

    def __str__(self):
        return str([self.map, self.rpm, self.gph])


def lookup_alt(alt: int) -> list:
    """

    This function looks into the performance file and extracts the list of lists corresponding to presettings
    corresponding to the specified altitude
    :param alt: cruise altitude (0 to 15000)
    :return: a list of lists corresponding of all altitude presettings
    """
    key = alt - alt % 2500
    if key == 0:
        key = 2500
    with open('performance.txt') as f:
        file = f.read()
    perf_dict = json.loads(file)
    return perf_dict[str(key)]


def remove_duplicates(perf_table: list, parameter: str) -> list:
    """

    This function takes a performance table which has been sorted according to the parameter specified
    It returns a table with the duplicates of the parameter removed
    :param perf_table: a list of lists corresponding to presettings (sorted by the parameter beforehand)
    :param parameter: 'spd' or 'rng'
    :return: a list of lists corresponding to presettings without duplicates of the parameter
    """
    if parameter == 'rng':
        ref = -1
        alt = -2
    elif parameter == 'spd':
        ref = -2
        alt = -1
    clean_list = []
    memory = perf_table[0]
    for line in perf_table:
        if memory[ref] != line[ref]:
            clean_list.append(memory)
            memory = line
        elif memory[alt] < line[alt] or memory[alt] == line[alt] and memory[1] > line[1]:
            memory = line
    clean_list.append(memory)
    return clean_list


def best_eco(altitude: int) -> Presetting:
    """

    This function takes the altitude and return the presetting corresponding to best economy
    If equal, return best range best speed
    If equal, return range best speed lowest RPM
    :param altitude: cruise altitude (0 to 15000)
    :return: economical presetting
    """
    perf_array = lookup_alt(altitude)
    perf_array.sort(key=lambda line: line[-1], reverse=True)
    high_economy = [param for param in perf_array if param[-1] == perf_array[0][-1]]
    if len(high_economy) > 1:
        high_economy.sort(key=lambda line: line[-2], reverse=True)
        high_economy = [param for param in high_economy if param[-2] == high_economy[0][-2]]
    best_economy = sorted(high_economy, key=lambda line: line[1])[0]
    return Presetting(best_economy)


def best_spd(altitude: int) -> Presetting:
    """

    This function takes the altitude and return the presetting corresponding to best speed
    If equal, return best speed best range
    If equal, return best speed best range lowest RPM
    :param altitude: cruise altitude (0 to 15000)
    :return: fast presetting
    """
    perf_array = lookup_alt(altitude)
    perf_array.sort(key=lambda line: line[-2], reverse=True)
    high_speed = [param for param in perf_array if param[-2] == perf_array[0][-2]]
    if len(high_speed) > 1:
        high_speed.sort(key=lambda line: line[-1], reverse=True)
        high_speed = [param for param in high_speed if param[-1] == high_speed[0][-1]]
    best_speed = sorted(high_speed, key=lambda line: line[1])[0]
    return Presetting(best_speed)


def cost_index(alt: int, ci: int) -> Presetting:
    """

    This functions takes an altitude and a cost index between 0 and 100 and return the best pre-setting accordingly
    Biaised toward range
    :param alt:  cruise altitude (0 to 15000)
    :param ci: cost index of the flight (0=eco to 100=fast)
    :return: presetting
    """
    perf_array = lookup_alt(alt)
    if ci > 50:  # speed case
        perf_array.sort(key=lambda line: line[-2])  # slowest to fastest
        clean_array = remove_duplicates(perf_array, 'spd')
    else:
        perf_array.sort(key=lambda line: line[-1], reverse=True)  # most to least endurance
        clean_array = remove_duplicates(perf_array, 'rng')
    index = int(ci*(len(clean_array)-1)/100)
    return Presetting(clean_array[index])


if __name__ == '__main__':
    alts = [2500, 5000, 7500, 10000, 12500, 15000]
    for alt in alts:
        print('{}ft 100ci test returns {}'.format(alt, best_spd(alt) == cost_index(alt, 100)))
        print('{}ft 0ci test returns {}'.format(alt, best_eco(alt) == cost_index(alt, 0)))

