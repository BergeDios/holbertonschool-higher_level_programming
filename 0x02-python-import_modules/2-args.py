#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv[1:])
    print("{:d} {:s}{:s}".format(count,
                                 "argument" if (count) == 1 else "arguments",
                                 "." if (count) == 0 else ":"))
    for counter, argument in enumerate(argv[1:]):
        print("{:d}: {:s}".format(counter + 1, argument))
