"""
Simple, given a string of words, 
eturn the length of the shortest word(s).

String will never be empty and 
you do not need to account for different data types.

Example: 
"bitcoin take over the world maybe who knows perhaps"), 3 --> over
"""

def find_short(s):
    return min(len(l) for l in s.split()) #split s into a list and search for the min word's length