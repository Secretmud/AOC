def _1a():
    with open("day1a.txt", "r") as f:
        max = 0
        tmp = 0
        for line in f.readlines():
            if line == "\n":
                max = tmp if tmp > max else max
                tmp = 0
            else:
                tmp += int(line)

        print(max)


_1a()

def _1b():
    with open("data/day1", "r") as f:
        tmp = 0
        top3 = {1: 0, 2: 0, 3: 0}
        for line in f.readlines():
            if line == "\n":
                print(tmp)
                if tmp > top3[1]:
                    top3[1] = tmp
                elif tmp > top3[2]:
                    top3[2] = tmp
                elif tmp > top3[3]:
                    top3[3] = tmp

                tmp = 0
            else:
                tmp += int(line)
        max = 0
        for k,v in top3.items():
            max += int(v)

        print(max)

_1b()
