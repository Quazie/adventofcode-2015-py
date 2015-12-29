#!/usr/bin/env python

import sys

# TODO: wget this for perfect solution
input_str = list("hepxxyzz")

min_char = ord('a')
max_char = ord('z')

def is_valid(cur_str):
  pos = 0
  found_run = False
  has_pairs = 0
  pair_end = -1
  for c in cur_str:

    # Password can't contain confusing chars
    if c in ['i', 'o', 'l']:
      return False

    # Password must contain a run
    if pos > 1:
      if ord(cur_str[pos]) - 2 == ord(cur_str[pos-2]):
        if ord(cur_str[pos]) -1 == ord(cur_str[pos-1]):
          found_run = True

    # Password must contain non-overlapping pairs
    if pos > 0:
      if cur_str[pos] == cur_str[pos-1]:
        if pos-1 != pair_end:
          pair_end = pos
          has_pairs += 1

    pos += 1
  return found_run and has_pairs > 1

def update_index(cur_str, index):
  # TODO: safety check index
  c = cur_str[index]
  if ord(c) is max_char:
    cur_str[index] = 'a'
    update_index(cur_str, index-1)
  else:
    cur_str[index] = chr(ord(cur_str[index]) + 1)

cur_str = input_str
update_index(cur_str, -1)
while not is_valid(cur_str):
  update_index(cur_str, -1)
print "".join(cur_str)
