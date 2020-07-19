


tar = 123
src = [1,2,3,4,100,25]

def op(src, l, r, o):
    if l == r:
        raise Exception("must be two different numbers")
    elif l > r:
        t = r
        r = l 
        l = t
    if o == 0:
        l = src[l]
        r = src[r]
        src.remove(l)
        src.remove(r)
        return [l + r] + src
    elif o == 1:
        l = src[l]
        r = src[r]
        src.remove(l)
        src.remove(r)
        return [l - r] + src
    elif o == 2:
        l = src[l]
        r = src[r]
        src.remove(l)
        src.remove(r)
        return [l * r] + src
    elif o == 3:
        l = src[l]
        r = src[r]
        src.remove(l)
        src.remove(r)
        if r == 0 or l % r != 0:
            return src
        else:
            return [l / r] + src

def unique(l): 
    return [list(x) for x in set(tuple(x) for x in l)]

def numbers(src):
    if len(src) == 1:
        return src[0]
    outcomes = []
    for o in [0,1,2,3]:
        for l in range(len(src)):
            for r in range(len(src)):
                if l != r:
                    outcomes.append(op(src[:], l, r, o))
    return unique(outcomes)
    
nodes = src[:]
for n in nodes:
    if len(node) > 1:
        nodes.append(numbers(n))