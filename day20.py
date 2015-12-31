#!/usr/bin/env python

def total_factors(n):
  fact = set(x for tup in ([i, n//i]
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
  total = 0
  for f in fact:
    if f * 50 >= n:
      total += f *11
  return total

x = 786240
while True:
  if total_factors(x) >= 34000000:
    print x
    break
  x += 1