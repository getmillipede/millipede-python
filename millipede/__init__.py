#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Print a gorgeous millipede
"""

from __future__ import print_function

from argparse import ArgumentParser
import os
import sys


__version__ = '0.2'


def millipede(size, comment=None, reverse=False):
    """
    Output the millipede
    """
    padding_offsets = [2, 1, 0, 1, 2, 3, 4, 4, 3]

    head = "    ╔⊙ ⊙╗\n" if reverse else "    ╚⊙ ⊙╝\n"
    body = "".join([
        "{}{}\n".format(
            " " * padding_offsets[(x + 3 * int(reverse)) % 9],
            "╔═(███)═╗" if reverse else "╚═(███)═╝"
        )
        for x in range(size)
    ])

    output = ""
    if reverse:
        output += body + head
        if comment:
            output += "\n" + comment + "\n"
    else:
        if comment:
            output += comment + "\n\n"
        output += head + body

    return output


def api_post(message, url, name, data=None, login=None, passwd=None):
    """ Send `message` to `phone_number` using the Rentabiliweb SMS API.
    It requires to have a contract with Rentabiliweb, valid credentials and to
    send the message from a whitelisted IP address.
    """
    try:
        import requests
    except ImportError:
        print('requests is required to do api post.', file=sys.stderr)
        sys.exit(1)

    post_data = {name : message}
    if data:
        for var in data:
            key, value = var.split('=')
            post_data[key] = value

    response = requests.post(
        url,
        data=post_data,
        auth=(login, passwd)
    )

    if response.status_code != 200:
        raise RuntimeError('Unable to post data')


def main():
    """
    Entry point
    """
    parser = ArgumentParser(description='Millipede generator')
    parser.add_argument('size', metavar='s',
                        type=int,
                        help='the size of the millipede')
    parser.add_argument('comment', metavar='c',
                        help='the comment', nargs="?")
    parser.add_argument('-r', '--reverse',
                        action='store_true',
                        help='reverse the millipede')
    parser.add_argument(
        '--http-host',
        metavar="The http server to send the data",
        help='Send the millipede via an http post request'
    )
    parser.add_argument(
        '--http-auth',
        metavar='user:pass',
        help='Used to authenticate to the API ',
        default=os.environ.get('HTTP_AUTH')
    )
    parser.add_argument(
        '--http-data',
        metavar='key=value',
        nargs='*',
        help='Add additional HTTP POST data'
    )
    parser.add_argument(
        '--http-name',
        metavar='name',
        help='The json variable name that will contain the millipede'
    )

    args = parser.parse_args()

    out = millipede(args.size, comment=args.comment, reverse=args.reverse)

    if args.http_host:
        if args.http_auth:
            try:
                login, passwd = args.http_auth.split(':')
            except ValueError:
                parser.error(
                    "Credentials should be a string like "
                    "`user:pass'"
                )
        else:
            login=None
            passwd=None

        api_post(out, args.http_host, args.http_name, args.http_data, login=login, passwd=passwd)

    print(out, end='')
