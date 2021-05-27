"""Setup script for realpython-reader"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="config-to-object",
    version="1.0.0",
    description="A convinient .ini file to NamedTuple parser that supports type hinting",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/yannikkellerde/config_to_object",
    author="Yannik Keller",
    author_email="yannik@kelnet.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["config_to_object"],
    include_package_data=True,
    entry_points={"console_scripts": ["ini_typefile=config_to_object.load_code:command_line_config"]},
)