# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

def match_ends(words):
    return len(list(filter(lambda w: (len(w)>1 and w[0]==w[len(w)-1]), words)))
    

def front_x(words):
    def compare(a,b):
        if a[0]=='x' and b[0]!='x':
            return -1
        if a[0]!='x' and b[0]=='x':
            return 1
        else:
            if a<b:
                return -1
            elif b<a:
                return 1
            else:
                return 0
    words.sort(cmp=compare)
    return words



def sort_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])
       
#empty    

def remove_adjacent(nums):
    return [nums[i] for i in range(len(nums)) if i==0 or nums[i-1]!=nums[i]]


def linear_merge(list1, list2):
    return sorted(list1 + list2)
   
