with open('input.txt', 'r') as f:
    fish = [int(x) for x in f.read().split(',')]


def run_timer(fish, days):
    remaining_days = days
    fish_timers = fish

    while (remaining_days):
        for i, fish in enumerate(fish_timers):
            if (fish == 0):
                fish_timers[i] = 6
                fish_timers.append(9)
            else:
                fish_timers[i] -= 1
        remaining_days -= 1
    return len(fish_timers)


def run_timer_optimized(fish, days):
    fish_dict = {x: 0 for x in range(9)}
    for f in fish:
        fish_dict[f] += 1
    for d in range(days):
        zero_energy = fish_dict[0]
        for k, v in fish_dict.items():
            if (k > 0):
                fish_dict[k-1] = v
        fish_dict[6] += zero_energy
        fish_dict[8] = zero_energy
    return sum(fish_dict.values())


answer1 = run_timer_optimized(fish, 18)
answer2 = run_timer_optimized(fish, 256)
print(answer1, answer2)
