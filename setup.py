from setuptools import setup, find_packages
from movies.version import __version__

def get_requirements():
    import os
    path =  os.path.join(os.path.abspath(os.curdir), 'requirements.txt')
    with open(path) as reqs:
        lines = reqs.readlines()
        lines = [x.strip() for x in lines]
    return lines 

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='movies',
    version=__version__,
    author='Krishnanand Singh',
    author_email='krishnanand91@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements(),
    extras_require={
        'tests': tests_require,
    }
)