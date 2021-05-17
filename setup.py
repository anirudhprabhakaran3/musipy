from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Python package to analyse songs'
LONG_DESCRIPTION = 'This python package helps analyse songs'


setup(
        name="musipy", 
        version=VERSION,
        author="Anirudh Prabhakaran",
        author_email="anirudhprabhakaran3@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
                'matplotlib',
                'numpy',
                'scipy',
        ],
)