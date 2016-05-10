
import random


def generate_mdp_files(map, T, filename, actions = [(0,1),(1,0),(0,-1),(-1,0)]):
    f = open(filename, "w")

    # Grid size
    f.write("grid " + str(len(map[0])) + " " + str(len(map)) + "\n")

    # Init
    for x in range(len(map[0])):
        for y in range(len(map)):
            if (map[x][y] == "S"):
                f.write("(" + str(x) + "," + str(y) + ")\n")
                
    # Obstacles
    for x in range(len(map[0])):
        for y in range(len(map)):
            if (map[x][y] == "1"):
                f.write("obstacle (" + str(x) + "," + str(y) + ")\n")

    # States and rewards
    for x in range(len(map[0])):
        for y in range(len(map)):
            if ((map[x][y] == "0") or (map[x][y] == "S")):
                f.write("(" + str(x) + "," + str(y) + ") -0.05\n")
            elif (map[x][y] == "G"):
                f.write("(" + str(x) + "," + str(y) + ") 1 Terminal\n")

    # Transitions
    for x in range(len(map[0])):
        for y in range(len(map)):
            for a in actions:
                states = T((x, y), a)
                for s in states.keys():
                    # str(tuple writes a blank space after the comma,
                    # so I get rid of it with replace
                    f.write((str((x,y))+ " " + str(a) + " " + str(s) + \
                             " " + str(states[s])+"\n").replace(", ", ","))
    f.close()



def sample_transition(map, wind_strength): #gridX, gridY, windX, windY):
    """
    gridX = number of x locations in grid
    gridY = number of y locations in grid
    windX = (low, high) the wind velocity has an x component between low and high
    windY = (low, high) the wind velocity has a y component between low and high
    """
    possible_directions = [(1,0),(0,1),(-1,0),(0,-1)]
    direction = possible_directions[random.randint(0, len(possible_directions)-1)]
    print "direction = ", direction
    wind = (wind_strength*direction[0], wind_strength*direction[1])
    print "wind = ", wind
    def T(s, a):
        newS = (s[0] + a[0], s[1] + a[1])
        states = []
        for vx in range(abs(wind[0])+1):
            for vy in range(abs(wind[1])+1):
                signX = (wind[0] >= 0)*2 - 1
                signY = (wind[1] >= 0)*2 - 1
                z = (newS[0]+vx*signX, newS[1]+vy*signY)
                z = (max(min(z[0], len(map[0])-1), 0),
                     max(min(z[1], len(map)-1), 0))
                states.append(z)

        states = list(set(states))
        
        prob = {}

        for z in states:
            prob[z] = 1.0/len(states)

        return prob

    return T


# Sample world

w = [['S', '0', '0', '0'],
     ['0', '1', '0', '0'],
     ['0', '1', '0', 'G'],
     ['0', '0', '0', '0']]

#actions = [(0,1),(1,0),(0,-1),(-1,0)]

T = lambda x, a: {x:0.2, (x[0]+a[0],x[1]+a[1]):0.8}

filename = "C:/Users/gcruz/Documents/test.mdp"

generate_mdp_files(w, T, filename)
