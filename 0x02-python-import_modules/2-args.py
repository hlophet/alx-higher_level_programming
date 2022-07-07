#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv)

    if size == 1:
        print("0 arguments.")
    elif size == 2:
        print("{:d} argument:".format(size - 1))
    else:
        print("{:d} arguments:".format(size - 1))

    for i in range(1, size):
        print("{:d}: {:s}".format(i, sys.argv[i]))
