import argparse

parser = argparse.ArgumentParser(
    prog='MyProgram',
    description='Process Some Integers.',
)

parser.add_argument('-s', '--src', nargs='?', help='src help', required=False, default=argparse.SUPPRESS)
args = parser.parse_args()