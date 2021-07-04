import argparse

parser = argparse.ArgumentParser(
    prog='MyProgram',
    description='Process Some Integers.',
)

parser.add_argument('-s', '--src', nargs='?', help='src help', required=False, default=argparse.SUPPRESS)
parser.add_argument('-n', '--num_workers', nargs='?', type=int, default=4, required=False)
parser.add_argument('bar', nargs='+', type=int, help='bar help')
args = parser.parse_args()