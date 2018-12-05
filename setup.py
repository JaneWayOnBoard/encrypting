
from setuptools import setup

__project__ = "encrypting"
__version__ = "0.0.1"
__description__ = "a Python module from the Raspberry Projects to encrypt a message with Ceasar's cypher"
__packages__ = ["encryptingAlphabet"]
__author__ = "Raspberry"
__classifiers__ = "classifiers"


setup(
    name = __project__,
    version = __version__,
    description = __description__,
    packages = __packages__,
    author = __author__,
    classifiers = __classifiers__,

)

"""Create a list of classifiers and pass it to the set up function"""

__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Education",
    "Programming Language :: Python :: 3",
]

"""Create a list of keywords and pass it to the set up function"""
"""to do"""
