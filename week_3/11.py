from itertools import permutations

def string_permutations(input_string):
    return [''.join(p) for p in permutations(input_string)]