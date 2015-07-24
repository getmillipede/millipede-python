#!/usr/bin/env python3


class millipede:
    def __init__(self, size, comment=None):
        self._millipede = ""
        if comment:
            self._millipede = comment + "\n\n"

        self._millipede += "    ╚⊙ ⊙╝ \n"
        padding = 2
        direction = -1
        while (size):
            for i in range(0, padding):
                self._millipede += " "
            self._millipede += "╚═(███)═╝\n"
            padding += direction

            if padding == 0:
                direction = 1
            elif padding == 4:
                padding = 3
                direction = -1
            size -= 1

    def __str__(self):
        return self._millipede

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Millipede generator')
    parser.add_argument('size', metavar='s', type=int, help='the size of the millipede')
    parser.add_argument('comment', metavar='c', type=str, help='the comment', nargs="?")
    args = parser.parse_args()

    print(millipede(args.size, args.comment))
