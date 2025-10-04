import yaml
import sys
from tlopo_flat import Flat

d = yaml.safe_load(sys.stdin.read())

print(Flat(separator=".").to_string(d))
