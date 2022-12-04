def ranges(r):
    return tuple(map(int, r.split("-")))


def _04a(file: str):
    data = open(file).read().splitlines()
    contained = 0
    part_of = 0
    for d in data:
        one, two = d.split(",")
        one = ranges(one)
        two = ranges(two)
        s1 = set(range(one[0], one[1]+1)) if one[0] != one[1] else set(one)
        s2 = set(range(two[0], two[1]+1)) if two[0] != two[1] else set(two)

        if s1.issubset(s2) or s2.issubset(s1):
            contained += 1

        if s1.intersection(s2):
            part_of += 1
    
    return contained, part_of


def test_04a():
    file="testdata/day4"
    assert _04a(file) == (2, 4)

if __name__ == "__main__":
    print(_04a('data/day4'))