import sys
import random


# output: Bit-map representation
# 1 -> obstacle
# 0 -> free
# S -> start
# G -> goal
def get_map(rows, cols, obstacle_density):
  map = []
  for i in range(rows):
    map.append([])
    for j in range(cols):
      if random.random() < obstacle_density:
        map[i].append("1")
      else:
        map[i].append("0")

  start = (random.randint(0, rows-1), random.randint(0, cols-1))
  while (map[start[0]][start[1]] == "1"):
    start = (random.randint(0, rows-1), random.randint(0, cols-1))


  goal = (random.randint(0, rows-1), random.randint(0, cols-1))
  while (map[goal[0]][goal[1]] == "1" or goal == start):
    goal = (random.randint(0, rows-1), random.randint(0, cols-1))

  map[start[0]][start[1]] = "S"
  map[goal[0]][goal[1]] = "G"

  return map


def get_transition(rows, cols, wind_strength):
  return ""


# rows are separated by ##
# each element in a row is separated by #
def map_to_str(map):
  res = ""
  for i in map:
    for j in i:
      res += j + "#"
    res+= "#"
  return res

if (len(sys.argv) != 5):
  print "Usage: random_test.py rows columns obstacle_density wind_strength"
  exit(1)


rows = int(sys.argv[1])
cols = int(sys.argv[2])
obstacle_density = float(sys.argv[3])
wind_strength = int(sys.argv[4])

            
map = get_map(rows, cols, obstacle_density)
print map_to_str(map)

transition = get_transition(rows, cols, wind_strength)