


def generate_mdp_files(map, actions, T, filename):
    f = open(filename, "w")

    # Grid size
    f.write("grid " + str(len(map[0])) + " " + str(len(map)) + "\n")

    # Obstacles
    f.write("obstacle ")
    for x in range(len(map[0])):
        for y in range(len(map)):
            if (map[x][y] == "1"):
                f.write("(" + str(x) + "," + str(y) + ") ")
    f.write("\n")

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
                    


# Sample world

w = [['S', '0', '0', '0'],
     ['0', '1', '0', '0'],
     ['0', '1', '0', 'G'],
     ['0', '0', '0', '0']]

actions = [(0,1),(1,0),(0,-1),(-1,0)]

T = lambda x, a: {x:0.2, (x[0]+a[0],x[1]+a[1]):0.8}

filename = "C:/Users/gcruz/Documents/test.mdp"

generate_mdp_files(w, actions, T, filename)
