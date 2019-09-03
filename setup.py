#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from setuptools import setup

install_requires = [
'matplotlib',
'scipy',
'scikit-image',
'scikit-learn',
'xlrd',
'xlsxwriter',
'csv',
'numpy',
'PyQt5',
'PIL']

setup(name='Macrophage Analysis Toolkit',
      version='1.0',
      description='A tool to quantify macrophage presence',
      author='Alexander Winkle',
      author_email='Hund.1@osu.edu',
      install_requires=install_requires
      )

