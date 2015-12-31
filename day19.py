#!/usr/bin/env python

import sys
from sets import Set
import random

# TODO: wget this for perfect solution
input_str1 = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg"""
input_str2 = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"
rules = {}
answers_pt1 = Set([])
answers_pt2 = {}

def find_all(a_str, sub):
  start = 0
  while True:
    start = a_str.find(sub, start)
    if start == -1: return
    yield start
    start += 1

def add_replace_rule(key, replace):
  if key in rules:
    rules[key].append(replace)
  else:
    rules[key] = [replace]

def add_string(string, count):
  if len(string) > len(input_str2):
    print "WTF"
  if string in answers_pt2:
    if answers_pt2[string] > count:
      answers_pt2[string] = count
  else:
    answers_pt2[string] = count

rule_list = input_str1.splitlines()
for rule in rule_list:
  info = rule.split(" ")
  key = info[0]
  replace = info[2]
  add_replace_rule(replace, key)

for rule in rules:
  for replace in rules[rule]:
    indexes = list(find_all(input_str2, rule))
    for index in indexes:
       answers_pt1.add(input_str2[:index] + replace + input_str2[index + len(rule):])
print len(answers_pt1)

for x in range(1000):
  cur_str = input_str2
  count = 0
  while True:
    added = False
    keys = rules.keys()
    random.shuffle(keys)
    for rule in keys:
      for replace in rules[rule]:
        indexes = list(find_all(cur_str, rule))
        for index in reversed(indexes):
          new_str = cur_str[:index] + replace + cur_str[index + len(rule):]
          added = True
          count += 1
          break
        if added:
          break
      if added:
        break

    if new_str == cur_str:
      break
    cur_str = new_str

  if cur_str is "e":
    print"{0} {1}: This took {2} attempts".format(count, cur_str, x+1)
    break



