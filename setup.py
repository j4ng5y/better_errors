from setuptools import setup, find_packages

setup(
    name='better_errors',
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='',
    long_description=open('README.md').read(),
    install_requires=[],
    url='https://github.com/j4ng5y/better_errors',
    author='Jordan Gregory',
    author_email='jordan@j4ng5y.dev'
)