import argparse

parser = argparse.ArgumentParser(
    description='Example for arguments parsers',
    epilog='You can put in example usage here',
)

#required arguments
parser.add_argument('--firstName', type=str, required=True)
parser.add_argument('--lastName', type=str, required=True)

#optional arguments
parser.add_argument('--age', type=int, help='specify how old you are here')

args = parser.parse_args()

print('Hello,', args.firstName, args.lastName, 'You are', args.age, 'Years Old')