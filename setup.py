from setuptools import setup, find_packages
import os
import evolutionaryModel

PACKAGE_PATH = os.path.abspath(os.path.join(__file__, os.pardir))

with open(os.path.join(PACKAGE_PATH, 'readme.rst')) as readme_file:
    readme = readme_file.read()

setup(
    name='evolutionaryModel',
    version=evolutionaryModel.__version__,
    packages=find_packages(),
    long_description=readme,
    author='Julien Milli',
    author_email='jmilli@eso.org',
    url='https://github.com/jmilou/evolutionary_model'
)
