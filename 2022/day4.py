def ranges(r):
    return tuple(map(int, r.split("-")))


def _04a(file: str):
    """
    ...456...
    ....5....
    """
    data = open(file).read().splitlines()

    contained = 0
    part_of = 0
    for d in data:
        one, two = d.split(",")
        one = ranges(one)
        two = ranges(two)
        if one[0] <= two[0] and one[1] >= two[1]:
            contained += 1
        elif two[0] <= one[0] and two[1] >= one[1]:
            contained += 1
        
        if one[1] >= two[0] and one[0] <= two[1]:
            part_of += 1
    
    return contained, part_of


def test_04a():
    file="testdata/day4"
    assert _04a(file) == (2, 4)

if __name__ == "__main__":
    print(_04a('data/day4'))