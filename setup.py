from setuptools import find_packages, setup

setup(
    name='otia',
    packages=find_packages(include=['otia']),
    version='0.1.0',
    description='ok this is a piece of trash',
    author='team OTIA',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)