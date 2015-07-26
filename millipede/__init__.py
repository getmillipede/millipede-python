#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Print a gorgeous millipede
"""

from __future__ import print_function

from argparse import ArgumentParser
import os
import sys


__version__ = '2.0'
DEFAULT_SIZE = 20


def read_rcfile():
    """
    Try to read a rcfile from a list of paths
    """
    files = [
        '{}/.millipederc'.format(os.environ.get('HOME')),
        '/usr/local/etc/millipederc',
        '/etc/millipederc',
    ]
    for filepath in files:
        if os.path.isfile(filepath):
            with open(filepath) as rcfile:
                return parse_rcfile(rcfile)
    return {}

def parse_rcfile(rcfile):
    """
    Parses rcfile

    Invalid lines are ignored with a warning
    """
    def parse_bool(value):
        """Parse boolean string"""
        value = value.lower()
        if value in ['yes', 'true']:
            return True
        elif value in ['no', 'false']:
            return False
        else:
            raise ValueError('''Can't parse {}'''.format(value))

    valid_keys = {
        'size': int,
        'comment': str,
        'template': str,
        'reverse': parse_bool,
        'opposite': parse_bool,
        'position': int,
    }
    params = {}

    for linenum, line in enumerate(rcfile):
        line = line.strip()
        if not line or line[0] == '#':
            continue
        pos = line.find(' ')
        key = line[:pos]
        value = line[pos:].strip()
        if key in valid_keys.keys():
            try:
                params[key] = valid_keys[key](value)
            except ValueError:
                print('Ignoring line {} from rcfile'.format(linenum + 1),
                      file=sys.stderr)
    return params


def compute_settings(args, rc_settings):
    """
    Merge arguments and rc_settings.
    """
    settings = {}
    for key, value in args.items():
        if key in ['reverse', 'opposite']:
            settings[key] = value ^ rc_settings.get(key, False)
        else:
            settings[key] = value or rc_settings.get(key)

    if not settings['size']:
        settings['size'] = DEFAULT_SIZE
    return settings


#pylint: disable=too-many-arguments
def millipede(size, comment=None, reverse=False, template='default', position=0, opposite=False):
    """
    Output the millipede
    """
    padding_offsets = [2, 1, 0, 1, 2, 3, 4, 4, 3]
    padding_suite_length = len(padding_offsets)
    head_padding_extra_offset = 2

    if opposite:
        padding_offsets.reverse()

    position = position or 0

    templates = {
        'frozen': {'bodyr': '╔═(❄❄❄)═╗', 'body': '╚═(❄❄❄)═╝',
                   'headr': '╔⊙ ⊙╗', 'head': '╚⊙ ⊙╝'},
        'love': {'bodyr': '╔═(♥♥♥)═╗', 'body': '╚═(♥♥♥)═╝',
                 'headr': '╔⊙ ⊙╗', 'head': '╚⊙ ⊙╝'},
        'corporate': {'bodyr': '╔═(©©©)═╗', 'body': '╚═(©©©)═╝',
                      'headr': '╔⊙ ⊙╗', 'head': '╚⊙ ⊙╝'},
        'musician': {'bodyr': '╔═(♫♩♬)═╗', 'body': '╚═(♫♩♬)═╝',
                     'headr': '╔⊙ ⊙╗', 'head': '╚⊙ ⊙╝'},
        'bocal': {'bodyr': '╔═(🐟🐟🐟)═╗', 'body': '╚═(🐟🐟🐟)═╝',
                  'headr': '╔⊙ ⊙╗', 'head': '╚⊙ ⊙╝'},
        'ascii': {'bodyr': '|=(###)=|', 'body': '|=(###)=|',
                  'headr': '/⊙ ⊙\\', 'head': '\\⊙ ⊙/'},
        'default': {'bodyr': '╔═(███)═╗', 'body': '╚═(███)═╝',
                    'headr': '╔⊙ ⊙╗', 'head': '╚⊙ ⊙╝'},
        'inception': {'bodyr': '╔═(🐛🐛🐛)═╗', 'body': '╚═(🐛🐛🐛)═╝',
                      'headr': '╔⊙ ⊙╗', 'head': '╚⊙ ⊙╝'},
        'humancentipede': {'bodyr': '╔═(😷😷😷)═╗', 'body': '╚═(😷😷😷)═╝',
                           'headr': '╔⊙ ⊙╗', 'head': '╚⊙ ⊙╝'},
    }

    template = templates.get(template, templates['default'])

    head = "{}{}\n".format(
        " " * (padding_offsets[position % padding_suite_length] + head_padding_extra_offset),
        template['headr'] if reverse else template['head']
    )

    body_lines = [
        "{}{}\n".format(
            " " * padding_offsets[(x + position) % padding_suite_length],
            template['bodyr'] if reverse else template['body']
        )
        for x in range(size)
    ]

    if reverse:
        body_lines.reverse()

    body = "".join(body_lines)

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


def api_post(message, url, name, http_data=None, auth=None):
    """ Send `message` as `name` to `url`.
    You can specify extra variables in `http_data`
    """
    try:
        import requests
    except ImportError:
        print('requests is required to do api post.', file=sys.stderr)
        sys.exit(1)

    data = {name : message}
    if http_data:
        for var in http_data:
            key, value = var.split('=')
            data[key] = value

    response = requests.post(
        url,
        data=data,
        auth=auth
    )

    if response.status_code != 200:
        raise RuntimeError('Unable to post data')


def main():
    """
    Entry point
    """
    rc_settings = read_rcfile()
    parser = ArgumentParser(description='Millipede generator')
    parser.add_argument('-s', '--size',
                        type=int,
                        nargs="?",
                        help='the size of the millipede')
    parser.add_argument('-c', '--comment',
                        type=str,
                        help='the comment')
    parser.add_argument('-v', '--version',
                        action='version',
                        version=__version__)
    parser.add_argument('-r', '--reverse',
                        action='store_true',
                        help='reverse the millipede')
    parser.add_argument('-t', '--template',
                        help='customize your millipede')
    parser.add_argument('-p', '--position',
                        type=int,
                        help='move your millipede')
    parser.add_argument('-o', '--opposite',
                        action='store_true',
                        help='go the opposite direction')
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

    settings = compute_settings(vars(args), rc_settings)

    out = millipede(
        settings['size'],
        comment=settings['comment'],
        reverse=settings['reverse'],
        template=settings['template'],
        position=settings['position'],
        opposite=settings['opposite']
    )

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
            login = None
            passwd = None

        api_post(
            out,
            args.http_host,
            args.http_name,
            http_data=args.http_data,
            auth=(login, passwd)
        )

    print(out, end='')
