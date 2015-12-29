#!/usr/bin/env python

import sys

# TODO: wget this for perfect solution
input_str = "1113222113"

cur_str = input_str
for x in range(50):
  new_str = ""
  cur_num = -1
  cur_count = 0
  for c in cur_str:

    if int(c) is cur_num:
      cur_count += 1
    else:
      if not cur_num is -1:
        new_str += str(cur_count) + str(cur_num)

      cur_count = 1
      cur_num = int(c)
  new_str += str(cur_count) + str(cur_num)
  cur_str=new_str
print len(cur_str)
