
def printpermutations(lst):
    ans = []
    pp(lst, [], ans)
    print(ans)


def pp(lst, prefix, other):
    if (len(prefix) == len(lst)):
        #print(prefix)
        other.append(prefix)
    for i in lst:
        if i not in prefix:
            pp(lst, prefix + [i], other)
