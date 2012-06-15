import os

setupargs = {}
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='komber',
    version='0.1',
    description='Helper library to ease the use of kombu.',
    long_description='',
    author='Christopher Grebs',
    author_email='christopher.grebs@native-instruments.de',
    url='',
    packages=['komber'],
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=['kombu'],
    tests_require=['nose', 'kombu'],
    test_suite="nose.collector",
    license='ISC',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ),
)
