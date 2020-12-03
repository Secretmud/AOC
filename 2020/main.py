import datetime
from time import time
from src.AOC import *
import csv
import sys


def read(file):
    with open("input/" + file, newline="") as f:
        reader = csv.DictReader(f, fieldnames=['1'])
        result = []
        for row in reader:
            result.append(row['1'])

        return result


def main():
    date = datetime.datetime.now()
    date = date.strftime("%d")
    a = aoc(read("aoc"+date+".csv"))
    task1 = "_" + date + "a"
    task2 = "_" + date + "b"
    sum = 2020
    start = time()
    try:
        x = getattr(a, task1)() 
        t1 = time()
        print(f"ans: {x} time: {(t1-start)*1000:.5f}ms")
    except Exception as e:
        print("Error: ", sys.exc_info()[0])
    try:
        y = getattr(a, task2)()
        t2 = time()
        print(f"ans: {y} time: {(t2-t1)*1000:.5f}ms")
    except Exception as e:
        print("Error: ", sys.exc_info()[0])

if __name__ == "__main__":
    main()
