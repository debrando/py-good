#!/usr/bin/env python
""" Slim yet handsome validation library (voluptuous 2) """

import setuptools

METADATA = dict(
    name='good',
    version='0.0.7',
    author='Mark Vartanyan',
    author_email='kolypto@gmail.com',

    url='https://github.com/kolypto/py-good',
    license='BSD',
    description=__doc__,
    long_description=open('README.rst').read(),
    keywords=['validation'],

    packages=setuptools.find_packages(),
    scripts=[],
    entry_points={},

    install_requires=[
        'six >= 1.7.3',
    ],
    extras_require={
    },
    include_package_data=True,
    test_suite='nose.collector',

    platforms='any',
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

try:
    import distutils.command.bdist_conda
    print("Conda distribution")
    METADATA.update(dict(
        distclass=distutils.command.bdist_conda.CondaDistribution,
        conda_import_tests=True,
        conda_command_tests=True,
        conda_buildnum=1,
    ))
except ImportError:
    print("Standard distribution")

if __name__ == '__main__':
    setuptools.setup(**METADATA)
