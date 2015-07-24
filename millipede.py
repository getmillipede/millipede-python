#!/usr/bin/env python3


class millipede:

    def __init__(self, size, comment=None, reverse=False):
        self._padding_offsets = [2, 1, 0, 1, 2, 3, 4, 4, 3]

        head = "    ╔⊙ ⊙╗\n" if reverse else "    ╚⊙ ⊙╝\n"
        body = "".join([
            "{}{}\n".format(
                " " * self._padding_offsets[(x + 3) % 9 if reverse else x % 9],
                "╔═(███)═╗" if reverse else "╚═(███)═╝"
            )
            for x in range(size)
        ])

        self._millipede = ""
        if reverse:
            self._millipede += body + head
            if comment:
                self._millipede += "\n" + comment
        else:
            if comment:
                self._millipede += comment + "\n\n"
            self._millipede += head + body

    def __str__(self):
        return self._millipede

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Millipede generator')
    parser.add_argument('size', metavar='s', type=int, help='the size of the millipede')
    parser.add_argument('comment', metavar='c', type=str, help='the comment', nargs="?")
    parser.add_argument('-r', '--reverse', action='store_true', help='reverse the millipede')
    args = parser.parse_args()

    print(millipede(args.size, comment=args.comment, reverse=args.reverse))
