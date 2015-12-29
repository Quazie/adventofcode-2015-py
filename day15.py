#!/usr/bin/env python

import sys

# TODO: wget this for perfect solution
input_str = """Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8"""

ingredients = {}
recepies = {}

def get_score(recepie):
  tot_cap = 0
  tot_dur = 0
  tot_flav = 0
  tot_text = 0
  tot_cal = 0
  for i in recepie:
    count = recepie[i]
    tot_cap += count * ingredients[i]["capacity"]
    tot_dur += count * ingredients[i]["durability"]
    tot_flav += count * ingredients[i]["flavor"]
    tot_text += count * ingredients[i]["texture"]
    tot_cal += count * ingredients[i]["calories"]
  if tot_cap < 0 or tot_dur < 0 or tot_flav < 0 or tot_text < 0:
    return 0
  if tot_cal != 500:
    return 0
  else:
    return tot_cap * tot_dur * tot_flav * tot_text


def add_recepie(recepie):
  score = get_score(recepie)
  if score > 0:
    if score in recepies:
      recepies[score].append(recepie)
    else:
      recepies[score] = [recepie]

ingredient_list = input_str.splitlines()
def i(string):
  return int(string.split(",")[0])

def add_ingredient(name, cap, dur, flav, text, cals):
  ingredients[name] = {
  "name": name,
  "capacity": cap,
  "durability": dur,
  "flavor": flav,
  "texture": text,
  "calories": cals
  }

def try_recepie(attempt, start_index):
  count = 0
  for i in ingredients:
    count += attempt[i]

  if count > 99:
    add_recepie(attempt)
  else:
    pos = 0
    for i in ingredients:
      if pos >= start_index:
        new_attempt = attempt.copy()
        new_attempt[i] += 1
        try_recepie(new_attempt, pos)
      pos += 1

for item in ingredient_list:
  info = item.split(' ')
  name = info[0].split(":")[0]
  capacity = i(info[2])
  durability = i(info[4])
  flavor = i(info[6])
  texture = i(info[8])
  cals = int(info[10])
  add_ingredient(name, capacity, durability, flavor, texture, cals)

attempt = {}
for i in ingredients:
  attempt[i] = 0
try_recepie(attempt, 0)

for score in sorted(recepies):
  print "{1}: {0}".format(recepies[score], score)

