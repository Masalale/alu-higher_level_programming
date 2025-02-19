#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    cnt = len(args)

    if cnt == 0:
        print("0 arguments.")
    elif cnt == 1:
        print("1 argument:")
        print("1: {}".format(args[0]))
    else:
        print("{} arguments:".format(cnt))
        for i in range(cnt):
            print("{}: {}".format(i + 1, args[i]))
