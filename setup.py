#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import setuptools
import BookerUtils

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    install_requires = fh.read().splitlines()

setuptools.setup(
    name="BookerUtils",
    version=BookerUtils.__version__,
    url="https://github.com/dracounion/BookerUtils",
    author=BookerUtils.__author__,
    author_email=BookerUtils.__email__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
    description="utils for iBooker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "ibooker",
        "utils",
    ],
    install_requires=install_requires,
    python_requires=">=3.6",
    # entry_points={
    #     'console_scripts': [
    #         "BookerUtils=BookerUtils.__main__:main",
    #         "btrans=BookerUtils.__main__:main",
    #     ],
    # },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
