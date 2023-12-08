"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        itemToString = str(item)
        if itemToString in frequencies:
            frequencies[itemToString] += 1
        else:
            frequencies[itemToString] = 1
    return frequencies
