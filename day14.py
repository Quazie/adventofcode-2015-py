#!/usr/bin/env python

import sys

# TODO: wget this for perfect solution
input_str = """Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.
Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.
Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.
Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.
Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds."""

deers = {}

def add_deer(deer_name, speed, speed_time, rest):
  deers[deer_name] = {
  "speed": speed,
  "speed_time": speed_time,
  "rest": rest,
  "dist": 0,
  "speed_ct": speed_time,
  "rest_ct": 0,
  "points": 0}

def tick(deer):
  if deer["speed_ct"] > 0:
    deer["dist"] += deer["speed"]
    deer["speed_ct"] -= 1
    if deer["speed_ct"] is 0:
      deer["rest_ct"] = deer["rest"]
  else:
    deer["rest_ct"] -= 1
    if deer["rest_ct"] is 0:
      deer["speed_ct"] = deer["speed_time"]

def add_point():
  winners = []
  dist = 0
  for deer in deers:
    if deers[deer]["dist"] > dist:
      winners = [deer]
      dist = deers[deer]["dist"]
    elif deers[deer]["dist"] == dist:
      winners.append(deer)

  for deer in winners:
    deers[deer]["points"] += 1

deer_stats = input_str.splitlines()
for stat in deer_stats:
  info = stat.split(' ')
  deer = info[0]
  speed = int(info[3])
  speed_time = int(info[6])
  rest = int(info[-2])
  add_deer(deer, speed, speed_time, rest)

for deer in deers:
  print deers[deer]

for x in range(2503):
  for deer in deers:
    tick(deers[deer])
  add_point()

for deer in deers:
  print "{0} ran {1} for {2} points".format(deer, deers[deer]["dist"], deers[deer]["points"])