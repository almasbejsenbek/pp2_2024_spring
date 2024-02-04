from itertools import permutations
def string():
    word = input()
    for perm in permutations (word):
        print("".join(perm))

string()