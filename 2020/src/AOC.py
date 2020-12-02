class aoc:

    def __init__(self, data):
        self.data = data
        self.med = int(len(data)/2)


    def _01a(self, sum):
        self.data.sort()
        start = 0
        end = len(self.data)-1
        
        while (start != self.med):
            if (self._01ax(start, end) < sum):
                start += 1
            elif (self._01ax(start, end) > sum):
                end -= 1
            else:
                break

        return self.data[start], self.data[end]


    def _01ax(self, start, end):
        return self.data[start] + self.data[end]


    def _01b(self, sum):
        self.data.sort()

        for x in range(len(self.data)):
            l = x+1
            r = len(self.data)-1
            
            while (l < r):
                if (self._01bx(x, l, r) == sum):
                    return self.data[x], self.data[l], self.data[r]
                elif (self._01bx(x, l, r) > sum):
                    r -= 1
                else:
                    l += 1


    def _01bx(self, x, y, z):
        return self.data[x] + self.data[y] + self.data[z]


    def _02a(self):
        count = 0
        for i in range(0, len(self.data)):
            dist = self.data[i].split()
            amt = dist[0].split("-")
            char = dist[1].strip(":")
            password = list(dist[2])
            hold = 0
            for x in range(len(password)):
                if (char == password[x]):
                    hold += 1

            if (int(amt[0]) <= hold <= int(amt[1])):
                count += 1


        return count


    def _02b(self):
        count = 0
        for i in range(0, len(self.data)):
            dist = self.data[i].split()
            amt = dist[0].split("-")
            char = dist[1].strip(":")
            password = list(dist[2])
            if (char == password[int(amt[0])-1] and 
                char != password[int(amt[1])-1] or
                char != password[int(amt[0])-1] and 
                char == password[int(amt[1])-1]):
                count += 1

        return count
