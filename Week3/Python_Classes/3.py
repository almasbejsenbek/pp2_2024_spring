def solve(numheads, numlegs):
    for numheads_chicken in range(numheads + 1):
        numheads_rabbit = numheads - numheads_chicken
        if numlegs == numheads_chicken*2 + numheads_rabbit*4:
            return numheads_rabbit, numheads_chicken
    return None
numhead = int(input())
numleg = int(input())
result = solve(numhead, numleg)
print(result)
