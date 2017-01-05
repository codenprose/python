def slam_dunk(player, defender=''):
    if defender:
        print("Ooooo, Poster Material! Nice play {}. Sorry {}.".format(player, defender))
    else:
        print("Nice Play %s!" % player)

player = input("Who dunked the ball? ")
defender = input("Did someone get dunked on ? ")
slam_dunk(player, defender)

def average(num1, num2):
    return (num1 + num2) / 2

avg = average(120, 47)
# print(avg)
