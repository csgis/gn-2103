# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
    try:
        from pip._internal.download import PipSession
        pip_session = PipSession()
    except ImportError:  # for pip >= 20
        from pip._internal.network.session import PipSession
        pip_session = PipSession()
except ImportError:  # for pip <= 9.0.3
    try:
        from pip.req import parse_requirements
        from pip.download import PipSession
        pip_session = PipSession()
    except ImportError:  # backup in case of further pip changes
        pip_session = 'hack'

from distutils.core import setup

from setuptools import find_packages

# Parse requirements.txt to get the list of dependencies
inst_req = parse_requirements('requirements.txt',
                              session=pip_session)
REQUIREMENTS = [str(r.req) if hasattr(r, 'req') else r.requirement if not r.is_editable else ''
                for r in inst_req]

setup(name='GeoNode',
      version=__import__('geonode').get_version(),
      description="Application for serving and sharing geospatial data",
      long_description=open('README.md').read(),
      classifiers=[
          "Development Status :: 4 - Beta"],
      python_requires='>=2.7, <3',
      keywords='',
      author='GeoNode Developers',
      author_email='dev@geonode.org',
      url='http://geonode.org',
      license='GPL',
      packages=find_packages(),
      package_data={
          '': ['*.*'], # noqa
          '': ['static/*.*'], # noqa
          'static': ['*.*'],
          '': ['templates/*.*'], # noqa
          'templates': ['*.*'],
      },
      include_package_data=True,
      install_requires=REQUIREMENTS,
      zip_safe=False
      )
