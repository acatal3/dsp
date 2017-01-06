# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

def match_ends(words):
    count = 0 
    for x in words:
        if len(x) >1 and x[0] = x[-1]:
            count += 1 
    return count
    

def front_x(words):
    xwerds=[]
    werds=[]
    for word in words:
        if word[0] == 'x':
            xwerds.append(word)
        else:
            werds.append(word)
    xwerds.sort()
    werds.sort()
    return xwerds + werds
print front_x(['xyz','xaba', 'baba','abba','dank','xray'])



def sort_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])
       
#empty    

def remove_adjacent(nums):
    return [nums[i] for i in range(len(nums)) if i==0 or nums[i-1]!=nums[i]]


def linear_merge(list1, list2):
    return sorted(list1 + list2)
   
