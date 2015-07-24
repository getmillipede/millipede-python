#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Millipede generator')
parser.add_argument('size', metavar='s', type=int, help='the size of the millipede')
parser.add_argument('comment', metavar='c', type=str, help='the comment', nargs="?")
args = parser.parse_args()

if args.comment:
    print(args.comment, end="\n\n")

print("    ╚⊙ ⊙╝ ")
padding = 2
direction = -1
while (args.size):
    for i in range(0, padding):
        print(" ", end="")
    print("╚═(███)═╝")
    padding += direction

    if padding == 0:
        direction = 1
    elif padding == 4:
        padding = 3
        direction = -1
    args.size -= 1
