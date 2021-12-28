class Simulation(object):
    def __init__(self, initial_fish_list):
        self.fish = initial_fish_list

    def count_fish(self):
        return len(self.fish)

    def run(self, target_days):
        while target_days:
            fish = self.fish
            for f in fish:
                f.advance_day()
                if f.r_days < 0:
                    new_fish = f.spawn()
                    self.fish.append(new_fish)
            target_days -= 1
        return self.count_fish()


class LFish(object):
    # setting this to 8 was resulting in off-by-one errors
    NEW_FISH_DAYS = 9
    RESET_DAYS = 6

    def __init__(self, remaining_days):
        self.r_days = remaining_days

    def __repr__(self):
        return f'<Fish: {self.r_days}>'

    def spawn(self):
        self.r_days = self.RESET_DAYS
        return LFish(self.NEW_FISH_DAYS)

    def advance_day(self):
        self.r_days -= 1
    

def read_initial_state():
    with open('inputs/input6.txt') as fh:
        txt = fh.read()
        fish = [LFish(int(i)) for i in txt.split(',')]
    return fish


def simulate_lanternfish(target_days):
    sim = Simulation(read_initial_state())
    fish_count = sim.run(target_days)
    return fish_count


def run():
    return simulate_lanternfish(80)
        

_runner = run
