#!/usr/bin/env python

# TODO: wget this for perfect solution
input_str = '''#...##......#......##.##..#...##......##.#.#.###.#.#..#..#......####..#......###.#.#....#..##..###..
####..#.#...#....#.#####.##.##.#..#.......#....#.##...###.###..#.#.#........#..#.#.##...##..#.####.#
...#..##...#.#.###.#.###..#.##.####.###...#...........#.###..##.#.##.#.###...#.#..###....#.###.#..#.
.#...##...####.#..#.....#..#...#.#.##...#...##..#.#.###....#..###.....##..#.###..###.....##..###...#
..##.#####....##..#.#..##.##..######...#..###.######.....#..##...#.#..##..##..#..#..#..##.#.#.#.#...
.###.###.###...##...##..###..##.###.#.....##..##.#.#########...##..##.#..##.#..##..####..#.#.#.#####
#.#####..###.###.##.##.#...#.#.#.#..#.###...#..##.###.#...####.#..#.#.....###..#..####..#.#.#...##..
....#...##.....#....####.##.#.###..#.#.##..#.#...##.###.###..#.##..#.#.##..##..#.##.###..#.#.###.###
##.##...#.##...#.#..#.#..#...###...###.#..#..#.#####..###.#......#.....###.#####.#.#..#.#.#.##..#.#.
#.#..#.....#.....##.#..##...###..##...##...###.#.###.#..#.#.###...##..##..#.###...#.#######.#...#.#.
#.#.....####.#..#.##...#.##....#####.###.#.....#####....###..#........##..####...#...#.###....#..###
##.#.##..#.#.##.#.....##.#.....###.####.#..######.....####.#.#..##.#.##...#..#.#.....#.####.#.......
#..#..#.#..#.######.##..##.####.....##.#.##.#.######..#.#....#.#...#.#..#..#.#.###.#..#.#.#..#...###
####..####.#.#.###.....#.#.#.##..#.##.##.##.#..##..##.#.##.....#.#..#.####.....###.#..#.####.#.#..##
###.##..##.#.##..#..##...#.#####.##.#....##.####.#.##....#..###.#.#.##...#.....#.#.#.#.#..##.#.#..#.
......#..####...##.##...#.##.##...##..#..##.###..#...#..##...#.#....###.####...#.##.###.#.##.####.##
..#...#####.#.#..#.##....#..#...#..####.....###...##.###....#..#.###...#........#.#.##..#..#.#.....#
#######.#.#.###.###..######.##..#####.##.###.###....####.#..##.##...###.#..############.#.##....##.#
#.#...##.###.#.###..#.#.#.#.#.#..##..####.#..##.....#.##..#.##...##.#..##..#.#.#....##....##.#..#.#.
..#.#.####.....###..#######.#.#.#.#...##.#####.....##...##...##.###..######.###..#...####.#..###.###
.#.##....#.#.##..##.#.##.##..######...#.....#..#.#.#.#.....#.#..##.#.#.......#######....#.......#...
..###.##.##..##....#.###...#.....##..##......###...##..###.##...##.###.#.#.#.###.###.#.#...###..#...
.##.#.#...#...##.#.#...#..#..#.#...##.#.##...##..#....#.#..##.#..#.#..#.#.....#..#.#...#######.#.##.
...####....#.###.#..###..##...##..#.#.#.###...#..##.##.##..##.#...#..#.##.....#.#........#..#.#.####
.....##..###...#....#.#.#.#...###.###...#.#...#.#.####....#..####...###..#..######..##.##..###.#####
#####.##..#....###.###....##.....#.#..#....#.#####.##.#.####.#.##...#..###...###..##...#.###.#####..
###.##..........########.######....####.###.#..##...#.##.####.#.....##..#####..###...#####.....#.#.#
##..#####.##.#.#####.#.##.##..#.##....########.#####.#...#.###.##...#.###.#.#..#....##.#..#...#.#.#.
.##.#....#..#...#..#####..#..##.#......#..#....########...#..#...#.....####.#...##...#.###.#.#..##.#
.##.##.#.##.#.##...#.#.#..##.##.###.#..##..#...###.##.###.#####.#.###..#..###.#...#.###.#...#..#.#.#
.#..#..#.#..#..###..#....###.####.##.#.###.#.##.###.#.##.###.###...###...###.#...####...#.##.##.#.#.
###..##...###...#..##.#..#.#...##....###.##.##..#####....###..#..#....#..###.###.#...#.##...#.#.#..#
#....#.......##.....#.##...#..#.###.#.##..##..#.##..#.###..##.##...#####.#..#####..#####..#####....#
.####.####....###..###.#.##.####.##.#...####.#.###.#.....#...####..#####.###..#.#.###.##.##...##..#.
####..##...##.########...##..###..#..###.##.#.#.#........#.#####.#...#.###.####.#..####..#.#.#....##
###.#..#...###.#..#..#.###...##..###.##.#.#...#..#...####..##....#.#..#..##.#.#...#####.###.#..#.#.#
...##....#.###.#.#..##...##.###.#..#..#......#...#.#..####.#.##..######.####.#...#..#..#..##.#.#.##.
##.####.#...#..#.#.##..##.#.#.###..##...####......#..######.#......#.##.#....##...###.#.#..#......##
#.....#...#######.##.#..#.#...###.#..#.####....#.#.##.#.##...###..#...#.###.##..#.###..#.##...#####.
#####.##...#..#.#.#.......#.##..#####..#####...###..##.#.#..###.#.#####.####..#.#..##...#.##...#.###
.##.#..#######.###.#.####.....##...#.##.#.#..#...##....####......######.#..######.....##########.##.
##...#.#..#.##.###.#.#.#.##.###.##..##.##.##...#.#..###.#######..#.....#####..#....######.#..##..###
.#.#.###.....#..##..#.#..##..#.###...###.#..##...#...#.#####.#.#####..###.#..#...##..#.#..#..####...
.#......##..#.....####.###....##.###.....###.##........#.###.##..#..#.#######.#.######..##..###.....
..##.#.#..#.##...#.###.###...######..#..#.#..#....###.#.#....#..........#...##.##.##.#..##..#.#####.
###.###.#..#.##..##.#..#..##.....##.....#..#######.#..#.#.#.####.###..###.#.#..#.##.##.####.###.####
#.#.#..#....########.#..#..#...##..#.##..#.#..##..####...##.....#.##.#.#...########..#.###.#..#.#.##
.##.....#...#.#...##.##....###...##..#.####...#..#.#..#..#.##..#.###.##.####.##..####.....##.#.....#
....####.#.##.#.##.#..##.#.######.##.####..#...####.#..###.#.#..#..##.#.#.....##.#####.#.####...#.#.
#..#####.#####.....##....######..##....#..#.#.###.#####.....##.##.####.#...##...#.##.#.#####.##.#...
##.####..###.#....#...#.#.#.#.###.#####.#.####..####...####......##..#..#..#.#.##...########....#...
.###.#.#.#.#..####.##.#..######..#.#.###.....#.#......#.#.#.#..####.##...##.#####.#.##..##..#..#.#..
.....###...#...#.####.###.#.#.#.#.....#....#.####.###.##.##.##.#######......#.####......#....##.....
##..#..#.#.##..#...#..##.##.##..###.#....##.##....####.#.##.###....#.##.#.#.##...##.###...#..#..####
...#.#..##..##.#...##.##...#.#......#.#.##..###....####.##...#.#.###.#..#..#.####..##..##..#####.###
.##.##..##########.##...#.##.####.#.#######.##.#.##.##..#...##....########.###..##.##.##.#..##.#.#.#
#####.#....#.##..#.....#......##.##..#.##.###..##.......###..##.#.###.##.###....####.#..#.###..#.#.#
.#...#..#.##....##....#...####....#...#..#...####...########.###.#..##.#.#.##..###..#.#.###.....##.#
##..##.....###......#..###.##.####.##.####.#.#....#..#...#..#.#..#.###.#...#...#..##.##...#..#######
.....##..###..##...#####.#.#.....###.#.#..####...#.#.#..#..####..##.#..###.####.#....##..###....#..#
#.#.##.#....#.#####.#....##...#...##...##....#.#.......#....#..#...###.###.#.####..####....#.##.#.#.
..##...##..###.#.#.##.#..#....#.#.....##.###.#.###.###.....#...#.#..#######.#####..#.###...##......#
#......###..#....#.#..#.###.##.#...##..###.####.#.#....#.##..#.###..##.#..#####..##.###.....#..###..
##.#.##..##.###.#..##.....#.##.....###....##.####.######.#...#..###....#.#...#.##.....###....#..#.#.
.##.#.#.#.##..#.#.#..##..#.###.####....#..###.######..####.#.....###.##..#...###.#..######.##.#.##..
...##.####.#..##.#####.##.#...##..#..#...#.#.#.#####...#....#..###...#..#....#.#.##.#.######.#..####
..#.#.#.#...#.######.#.....#..#.#..###....#.#.########...#....#.#.##..#...##...#.#..#.#.###....##...
#####..#..##..#..##..#..#.#.##.#....#####.####.##.#.###..##..##....#.....#.#####.#...#.#####.##.#.#.
#.#..#####...####.###.###.....####.###.....##...##...#..#..#######.#.##....##..####.....##...#..#..#
#.#.###.#.#..##..#....#.#...#.#.##.##..#.##.....##...#.#..##.......##.#.###..#####.#.##....#.##.....
...#.......#....#.#.####.#.###.###..#....#..##.#..####........#.##..#...#.#...###.#..#.#.#...#...#..
...##.#####.##.#.###.##.##.#.##..##.#.#.#.#.#.##.#..##...##.#.#..#..##.##.#####.#.###...#####..#..#.
#######.#..#..#....##.#.#..####.#..#..###...#..#.......###.#.#.####....#.###...#.#.###.#.#.#.#..###.
..##.##.#.##.###....###.##.#.###.#...#....#.####..###..###.#.#..#...##.#.#.#..##.###..###.#.##...###
######..######..##..##.#.#.##.##.#..##..#.#.#.##..#.#...#...#.#.#..######.#..#.#.######..#......##.#
#.#####.....#.......#########..###.##...#...##.#.#..#...#####...#...#..#.###.#..#.#...###.#.#.#...#.
#....##....###...##.##.#...##.........##.#.#..#.#.##.#.######.#####..#..###.###.#...#.#.##.######...
#.#...###.#.###.##.#.######.#######.###.##..#.#.#...######.##.####.##..#.#.#.#......##..##.........#
..###..##....#.....##...#.#.###.#.#.....##.#...###.####.#...#...##..##.#.#.####..###...######....#.#
..###.#.##.####.#..#.##....##..#####....#..##.##.#..#######...#.####...##.#.#.##.........#....#....#
.##.#...#.####..#.#...#.##..######.##..##.#.###.##..###.###....##..#.##.##..##.#...###.##.##.###....
#...###.###.#..#....#.......#..#.....###..#.###.##.##....#.####.#.####.##..##..#..#.....#....##.#.#.
.##.#..#..#.##.......#.####.#######.....#.##.##.#.....#.#..#....######.#..###.##.##.....#.####..##.#
###..#.###.#..####.....##....#..####....#.##.##..#...######.#########...#.#....##...###.#..#.##...#.
#..###..##..#.#.##.###.#.#.##...###.#...##.##..#.###....###..#.#...#.###..######.#..#.###..#..#..#.#
.#........##.#.###..###.#.#.##.....##.##.#.#...##..#.##....###..#.#.#.#.##....#.##..#.#...###...#...
####.####..#....#.#.#..#..##.......##.####...###.##..#.#.##.#..##..######.......##.#.##..#...#.....#
..#..#..###..##.##..######.#..###..###.#.##..##.#..#####.#.#.#.##..#.##..##.##......####.#..........
...##.##..###.#...###....#.#.#.#.....#.##.....##...#...#......####...##.##....##.#..#.####.#..###.#.
..#.....####.#.###.#####..#..###..#..#.#...#####...###.###....#.###..#...#..#..#.#..#.##..##.#.#....
..##.#####...###.###.........#....##.####.##..#.#..#.#...#...##.##.##..#.#.##.########......#####...
...###.#.#..#...#.###.###.......##.###.#..#.##########...#..#.#.#.##.#.###...######..#.#...###.##...
.#.#.#######.#..##.##..##...#...####...#..#####.#..##...###.#.#...#.##...#......#..##.####..#.....##
.##.##.#.#......#######..###.....##.#.##..###......#....####...#.###.#.##.#........#..#....##.....##
#...#.###.#.##...##.####....#...#.###..#.#.....#.#....#.#.#.##...#.#..#####.#.#..#..#..#....#...####
.....##...###......#####..##.##.##...##.#.#####..##...#.#.#.#.###...###.##.####..#.#..#.#..#.####.##
#..#..##.#.##.#.##.#.#.#..###....###.##.#.##.#...#.#..#...#....###.#..#.#.######.#...####..#..##.#.#
#..#.#..#...###.#..##.#...#...##.#......#...#..#..####..##.....#.###...#.#..#.#....#.#####.##.###...
###....#.#..#.#..###..#.##......#...#..#..##.#..###..##..#..#.####..#...########..##.#.##.#.#.#...#.
.#.#.##.##.###..#...#.#....#..#.##..#.#.#.#.##.##.#####...#........####..###..####.#####..#.##.#.##.'''
input_str = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""

lights = [[{"cur": False, "next":False} for x in range(100)] for x in range(100)]
lights = [[{"cur": False, "next":False} for x in range(6)] for x in range(6)]

def reset():
  for col in lights:
    for row in col:
      row["cur"] = row["next"]

def tick():
  max_index = 99
  max_index = 5
  col_num = 0
  for col in lights:
    row_num = 0
    for row in col:
      count = -1 if lights[col_num][row_num]["cur"] else 0
      row_start = row_num
      row_end = row_num +1
      col_start = col_num
      col_end = col_num +1
      if row_num > 0:
        row_start -= 1
      if col_num > 0:
        col_start -= 1
      if row_num < max_index:
        row_end += 1
      if col_num < max_index:
        col_end += 1

      for y in range(row_start, row_end):
        for x in range(col_start, col_end):
          if lights[x][y]["cur"]:
            count += 1

      new_state = False
      if lights[col_num][row_num]["cur"]:
        if count == 3:
          new_state = True
      else:
        if count == 2 or count == 3:
          new_state = True
      lights[col_num][row_num]["next"] = new_state


      row_num += 1
    col_num += 1

initial_lights = input_str.splitlines()
col = 0
for light_strip in initial_lights:
  pos = 0
  for c in light_strip:
    setting = False
    if c == "#":
      setting = True
    lights[col][pos]["cur"] = setting
    pos += 1
  col += 1

for x in range(1):
  tick()
  reset()

count = 0
for col in lights:
  for row in col:
    if row["cur"]:
      count += 1
print count


