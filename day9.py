#!/usr/bin/env python

import sys

# TODO: wget this for perfect solution
input_str = """AlphaCentauri to Snowdin = 66
AlphaCentauri to Tambi = 28
AlphaCentauri to Faerun = 60
AlphaCentauri to Norrath = 34
AlphaCentauri to Straylight = 34
AlphaCentauri to Tristram = 3
AlphaCentauri to Arbre = 108
Snowdin to Tambi = 22
Snowdin to Faerun = 12
Snowdin to Norrath = 91
Snowdin to Straylight = 121
Snowdin to Tristram = 111
Snowdin to Arbre = 71
Tambi to Faerun = 39
Tambi to Norrath = 113
Tambi to Straylight = 130
Tambi to Tristram = 35
Tambi to Arbre = 40
Faerun to Norrath = 63
Faerun to Straylight = 21
Faerun to Tristram = 57
Faerun to Arbre = 83
Norrath to Straylight = 9
Norrath to Tristram = 50
Norrath to Arbre = 60
Straylight to Tristram = 27
Straylight to Arbre = 81
Tristram to Arbre = 90  """

connections = {}
paths = {}

def add_connection(start, end, dist):
  int_dist = int(dist)
  get_place(start)[end] = int_dist
  get_place(end)[start] = int_dist

def get_place(place):
  if not place in connections:
    connections[place] = {}
  return connections[place]

def add_path(route, dist):
  if dist in paths:
    paths[dist].append(route)
  else:
    paths[dist] = [route]

def try_path(cur_route, dist):
  if len(cur_route) == len(connections):
    add_path(cur_route, dist)
    return
  cur_stop = cur_route[-1]
  for place in connections[cur_stop]:
    if not place in cur_route:
      new_dist = dist + connections[cur_stop][place]
      new_route = cur_route[:]
      new_route.append(place)
      try_path(new_route, new_dist)



routes = input_str.splitlines()
for route in routes:
  route_info = route.split(' ')
  start = route_info[0]
  end = route_info[2]
  dist = route_info[4]
  add_connection(start, end, dist)

for place in connections:
  try_path([place], 0)

for distance in sorted(paths):
  print "{0}: {1}".format(paths[distance], distance)

