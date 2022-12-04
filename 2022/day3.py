def rucsacks(data):
    rucsack = []
    for d in data:
        comp1 = d[0:len(d)//2]
        comp2 = d[len(d)//2:]
        rucsack.append([comp1, comp2])
    return rucsack

def _03a():
    data = open("data/day3").read().splitlines()

    r = rucsacks(data)
    upper = 38
    lower = 96
    score = 0
    for rucsack in r:
        for a in rucsack[0]:
            if a in rucsack[1]:
                score += ord(a) - upper if ord('A') <= ord(a) <= ord('Z') else ord(a) - lower
                break


    print(score)


def _03b():
    data = open("data/day3").read().splitlines()
    r = iter(data)
    upper = 38
    lower = 96
    score = 0

    for a,b,c in zip(r,r,r):
        for d in a:
            if d in b and d in c:
                score += ord(d) - upper if ord('A') <= ord(d) <= ord('Z') else ord(d) - lower
                break

    print(score)

_03a()
_03b()