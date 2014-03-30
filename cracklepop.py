#!/usr/bin/env python

def main():

    for i in range(0, 101):

        output = "%s " % i

        if i % 3 == 0:
            output += "Crackle"
        if i % 5 == 0:
            output += "Pop"

        print output


if __name__ == "__main__":
    main()
