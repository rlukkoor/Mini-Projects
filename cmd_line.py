import sys, argparse

print('Number of arguments:', len(sys.argv), 'arguments.')
print('List of arguments:', str(sys.argv))

parser = argparse.ArgumentParser()
parser.parse_args()