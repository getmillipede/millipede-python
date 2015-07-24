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


def send_sms(message, phone_number, api_login, api_passwd):
    """ Send `message` to `phone_number` using the Rentabiliweb SMS API.
    It requires to have a contract with Rentabiliweb, valid credentials and to
    send the message from a whitelisted IP address.
    """
    try:
        import requests
    except ImportError:
        print('requests is required to send SMS.', file=sys.stderr)
        sys.exit(1)

    api_url = 'https://sms.v3.eiole.com/send'

    response = requests.post(
        api_url,
        data={
            'phone': phone_number,
            'message': message
        },
        auth=(api_login, api_passwd)
    )
    data = response.json()

    if response.status_code != 200 or data['code'] != 0:
        raise RuntimeError('Unable to send the SMS')


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
        '--to',
        metavar="International phone number, starting with a `+'",
        help='Send the millipede by SMS to a phone number. Requires to have '
             'Rentabiliweb credentials.'
    )
    parser.add_argument(
        '--rentabiliweb-creds',
        metavar='user:pass',
        help='Used to authenticate against the Rentabiliweb API. '
             'Only used if --to is not empty.',
        default=os.environ.get('RENTABILIWEB_CREDS')
    )
    args = parser.parse_args()

    out = millipede(args.size, comment=args.comment, reverse=args.reverse)

    if args.to:
        if not args.rentabiliweb_creds:
            parser.error(
                '--to is set, but --rentabiliweb-creds is not and the '
                'environment variable RENTABILIWEB_CREDS is empty'
            )
        try:
            api_login, api_passwd = args.rentabiliweb_creds.split(':')
        except ValueError:
            parser.error(
                "Rentabiliweb credentials should be a string like "
                "`user:pass'"
            )

        send_sms(out, args.to, api_login, api_passwd)

    print(out, end='')
