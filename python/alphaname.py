#!/usr/bin/env python3

def process(name):
    tempArr = []
    retStr = ""
    for c in name:
        tempArr.append(c)

    tempArr.sort(key=str.lower)
    for c in tempArr:
        retStr += c
    print(retStr)

def main(argv):
    import argparse
    parser = argparse.ArgumentParser(description="Formats your name awesomely!")
    parser.add_argument("-n", "--name", dest='name',default= '', required=True,help='Insert name to format')
    args = parser.parse_args(argv)
    process(args.name)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])