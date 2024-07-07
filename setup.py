"""Setup for the random-dict package."""
import os
import re
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf8') as f:
    long_description = f.read()


def read(*parts):
    with open(os.path.join(here, *parts), 'r', encoding='utf8') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


__version__ = find_version("random_dict", "__version__.py")

test_deps = ['pytest', 'pytest-cov', 'coveralls',
             'validate_version_code', 'codacy-coverage', "tqdm"]

extras = {
    'test': test_deps,
}

setup(
    name='random_dict',
    version=__version__,
    description="Simple python package to generate random dictionaries of given types.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/LucaCappelletti94/random_dict",
    author="Luca Cappelletti",
    author_email="cappelletti.luca94@gmail.com",
    # Choose your license
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    tests_require=test_deps,
    extras_require=extras,
)
