#!/usr/bin/env python

import sys

# TODO: wget this for perfect solution
input_str = """50
44
11
49
42
46
18
32
26
40
21
7
18
43
10
47
36
24
22
40"""


bucket_list = input_str.splitlines()
int_bucket_list = []
for bucket in bucket_list:
  int_bucket_list.append(int(bucket))
success = []

def try_buckets(to_use, used, stat_pos):
  GOAL = 150

  val = 0
  for bucket in used:
    val += bucket
  if val > GOAL:
    return
  elif val == GOAL:
    success.append(used)
    print used
    return
  pos = 0
  for bucket in to_use:
    if pos >= stat_pos:
      new_used = used[:]
      new_used.append(bucket)
      new_to_use = to_use[:]
      new_to_use.remove(bucket)
      if len(new_used) < len(used):
        return False
      if len(to_use) < len(new_to_use):
        return False
      try_buckets(new_to_use, new_used, pos)
    pos += 1


try_buckets(int_bucket_list, [], 0)
wins = [bucket_list]
for win in success:
  if len(win) < len(wins[-1]):
    wins = [win]
  elif len(win) == len(wins[-1]):
    wins.append(win)
print len(wins)
