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



def remove_AR(compound):
  step  = 0
  test_len = len(compound)
  while "Rn" in compound:
    for rule in rules:
      if "Rn" in rule:
        for replace in rules[rule]:
          indexes = list(find_all(compound, rule))
          if len(indexes) > 0:
            index = indexes[-1]
            compound = compound[:index] + replace + compound[index + len(rule):]
            step += 1
    if len(compound) == test_len:
      break;
    test_len = len(compound)
  return (compound, step)

def reduce_ar(compound):
  step  = 0
  test_str = compound
  while "Ar" in compound:
    found_one = False
    indexesAr = list(find_all(compound, "Ar"))
    indexesRn = list(find_all(compound, "Rn"))
    for x in range(len(indexesAr)):
      for rule in rules:
          for replace in rules[rule]:
            indexes = list(find_all(compound, rule))
            for index in indexes:
              if index > indexesRn[x] and index < indexesAr[x]:
                compound = compound[:index] + replace + compound[index + len(rule):]
                step += 1
                found_one = True
                break;
            if found_one:
              break;
          if found_one:
            break;

    if compound == test_str or found_one:
      break;
    test_str = compound
  return (compound, step)

def remove_dup(compound):
  step  = 0
  test_len = len(compound)
  while True:
    for rule in rules:
      if len(rule) is 4 and rule[0] == rule[2] and rule[1] == rule[3]:
        for replace in rules[rule]:
          indexes = list(find_all(compound, rule))
          if len(indexes) > 0:
            index = indexes[-1]
            compound = compound[:index] + replace + compound[index + len(rule):]
            step += 1
    if len(compound) == test_len:
      break;
    test_len = len(compound)
  return (compound, step)

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
    print"{0} {1}".format(count, cur_str)
    break

#indexes = list(find_all(input_str2, "Ar"))
#indexes.append(len(input_str2)-1)
#start = 0
#new_str = [{"s":"","count":0}]
#for index in indexes:
#  is_valid = False
#  test_str =  input_str2[start:index+2]
#  indexRn = list(find_all(test_str, "Rn"))
#  if len(indexRn) != 1:
#    if len(indexRn) is len(list(find_all(test_str, "Ar"))):
#      is_valid = True
#  else:
#    is_valid = True
#  if is_valid:
#    start = index+2
#  else:
#    if index == len(input_str2) -1:
#      print "failures"
#      break;
#    continue
#  print test_str
#
#  answers_pt2 = {}
#  add_string(test_str, 0)
#  step_count = 1
#  count = step_count
#  quick_pass = True
#  test_len = 1
#  while True:
#    answers_to_try = answers_pt2.copy()
#
#    for cur_str in answers_to_try:
#      added = False
#      for rule in rules:
#        for replace in rules[rule]:
#          indexes = list(find_all(cur_str, rule))
#          for index in indexes:
#            add_string(cur_str[:index] + replace + cur_str[index + len(rule):], count)
#            added = True
#      if added:
#        answers_pt2.pop(cur_str, None)
#    #print answers_pt2
#    count += 1
#    if answers_to_try == answers_pt2:
#      break
#    test_len = len(answers_pt2)
#    print len(answers_pt2)
#
#  num_ans = len(answers_pt2)
#  new_new_str = []
#  for ans in answers_pt2:
#    if num_ans == 1:
#      for x in range(len(new_str)):
#        new_str[x]["s"] += ans
#        new_str[x]["count"] += answers_pt2[ans]
#    elif num_ans == 0:
#      print "FAILURE"
#      exit(0)
#    else:
#      for x in range(len(new_str)):
#        new_new_str.append({"s":new_str[x]["s"] + ans,"count":answers_pt2[ans] + new_str[x]["count"]})
#      new_str = new_new_str
#
#print new_str


