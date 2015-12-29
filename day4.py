#!/usr/bin/env python
import md5

input_str = "yzbqklnj"

key = {
  '0':0,
  '1':0,
  '2':0,
  '3':0,
  '4':0,
  '5':0
}
def is_valid_answer(answer):
  for val in key:
    if not (str(answer[int(val)]) is str(key[val])):
      return False

  return True

count = 0
while (not is_valid_answer(md5.new(input_str+str(count)).hexdigest())):
  count += 1
print count
