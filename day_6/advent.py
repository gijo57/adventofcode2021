with open('input.txt', 'r') as f:
    fish = [int(x) for x in f.read().split(',')]
    days = 80


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


answer1 = run_timer(fish, days)
print(answer1)
