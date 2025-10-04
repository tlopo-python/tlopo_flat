import yaml
import sys
from tlopo_flat import Flat
import argparse

parser = argparse.ArgumentParser(description="Flattens JSON and YAML structures")
parser.prog = 'python -mtlopo_flat'
parser.add_argument("-s", '--separator', help="Key separator, default= ' | '", default=" | ")
args = parser.parse_args()

separator = args.separator


d = yaml.safe_load(sys.stdin.read())
print(Flat(separator=separator).to_string(d))
