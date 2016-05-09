


def generate_mdp_files(map, actions, T, filename):
    f = open(filename, "w")
    f.write("grid " + str(len(map[0])) + " " + str(len(map)) + "\n")

    f.write("obstacle ")
    for x in range(len(map[0])):
        for y in range(len(map)):
            if (map[x][y] == "1"):
                f.write("(" + str(x) + "," + str(y) + ") ")
    f.write("\n")

    for x in range(len(map[0])):
        for y in range(len(map)):
            if ((map[x][y] == "0") or (map[x][y] == "S")):
                f.write("(" + str(x) + "," + str(y) + ") -0.05\n")
            elif (map[x][y] == "G"):
                f.write("(" + str(x) + "," + str(y) + ") 1 Terminal\n")

    for x in range(len(map[0])):
        for y in range(len(map)):
            for a in actions:
                states = T((x, y), a)
                for s in states.keys():
                    f.write((str((x,y))+ " " + str(a) + " " + str(s) + \
                             " " + str(states[s])+"\n").replace(", ", ","))
    f.close()
                    


    
