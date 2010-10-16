#!/usr/bin/env python

from distutils.core import setup, Extension
from setupext import options, levmar
import numpy as np

#LEVMAR_LIBDIR = '/Users/swilkins/Dropbox/Programming/Python/levmar-2.5'
#LEVMAR_INCDIR = '/Users/swilkins/Dropbox/Programming/Python/levmar-2.5'
#LEVMAR_LIBDIR = '/home/tardis/swilkins/C-C++/levmar-2.5'
#LEVMAR_INCDIR = '/home/tardis/swilkins/C-C++/levmar-2.5'
#LIBLINUX = ['levmar', 'm', 'blas', 'lapack']
#LIBMACOSX = ['levmar', 'm']

ext_modules = []
if options['build_levmar']:
    ext_modules.append(Extension('pyspec.pylevmar', ['src/pylevmar.c'],
                                 libraries = levmar['libraries'],
                                 extra_compile_args = ['-g'],
                                 library_dirs = levmar.library_dirs,
                                 include_dirs = levmar.include_dirs,
                                 depends = ['src/pylevmar.h']))

setup(name='pyspec',
      version='0.2',
      description='Python utilities for spec data analysis',
      author='Stuart Wilkins',
      author_email='stuwilkins@mac.com',
	  url='http://www.stuwilkins.com',
      packages=['pyspec', 'pyspec.ccd'],
      ext_modules = ext_modules
)
