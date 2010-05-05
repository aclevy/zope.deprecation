##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.deprecation package

$Id$
"""

import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

name = 'zope.deprecation'
setup(
    name=name,
    version = '3.4.1dev',
    url='http://www.python.org/pypi/'+name,
    license='ZPL 2.1',
    description='Zope 3 Deprecation Infrastructure',
    author='Zope Foundation and Contributors',
    author_email='zope3-dev@zope.org',
    long_description=(
        read('README.txt')
        + '\n' +
        read('src', 'zope', 'deprecation', 'README.txt')
        + '\n' +
        read('CHANGES.txt')
        + '\n' +
        'Download\n'
        '########\n'
        ),

      package_dir = {'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['zope',],
      install_requires = 'setuptools',
      extras_require = dict(test=['zope.testing']),
      include_package_data = True,
      zip_safe = False,
      )
