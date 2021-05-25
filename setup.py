from setuptools import setup, find_packages
from setuptools.command.install import install
import os


setup(
    name='slack2bm',
    version=open('VERSION').read().strip(),
    #version=__version__,
    author='Francesco De Carlo',
    author_email='decarlof@gmail.com',
    url='https://github.com/xray-imaging/slack2bm',
    packages=find_packages(),
    include_package_data = True,
    scripts=['bin/slack2bm'],
    description='cli to run a slack rob at 2-bm',
    zip_safe=False,
)