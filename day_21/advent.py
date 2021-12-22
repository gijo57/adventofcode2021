with open('input.txt', 'r') as f:
    player1_init, player2_init = [int(x[-1]) for x in f.read().split('\n')]


def simulate_game(point_limit):
    die_cast = 0
    die_value = 1
    player1 = [player1_init, 0]
    player2 = [player2_init, 0]

    while (True):
        if (die_value > 100):
            die_value = 1
        for i in range(3):
            if (die_value > 100):
                die_value = 1
            player1[0] += die_value
            if (player1[0] > 10):
                player1[0] %= 10
            if (player1[0] == 0):
                player1[0] = 10
            die_value += 1
        for i in range(3):
            if (die_value > 100):
                die_value = 1
            player2[0] += die_value
            if (player2[0] > 10):
                player2[0] %= 10
            if (player2[0] == 0):
                player2[0] = 10
            die_value += 1
        player1[1] += player1[0]
        die_cast += 3
        if (player1[1] >= point_limit):
            break
        player2[1] += player2[0]
        die_cast += 3
        if (player2[1] >= point_limit):
            break
    return min(player1[1], player2[1]) * die_cast


answer1 = simulate_game(1000)
print(answer1)