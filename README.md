# tlopo_flat
A package to flatten JSON and YAML structures making it easier to grep and diff


# How to Install

It's as simple as `pip install tlopo_flat`

# How to use

We cause use two ways, the executable module to quickly flatten json or yaml files or programmatically in python code: 

Executable module:

```python
python -mtlopo_flat --help
python -mtlopo_flat < file.yaml
```

In code:
```python
#! /usr/bin/env python
from tlopo_flat import Flat

data = {"nested_level_1": {"nested_level_2": { "nested_level_3" : "the values is here"}}}
print(Flat(separator=' -> ').to_string(data))
```
