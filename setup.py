from setuptools import setup
setup(
	name = 'tlopo_flat',
	version = '0.1',
	description = 'A package to flatten JSON and YAML structures making it easier to grep and diff',
	packages = ['tlopo_flat'],
	install_requires = [
		'pyaml'
	]
)
__author__ = 'Tiago Lopo' 
