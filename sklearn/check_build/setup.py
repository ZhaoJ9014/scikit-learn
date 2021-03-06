# Author: Virgile Fritsch <virgile.fritsch@inria.fr>
# License: BSD Style.

import numpy
from os.path import join


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('check_build', parent_package, top_path)
    config.add_extension('_check_build',
                         sources=['_check_build.c'],
                         include_dirs=[numpy.get_include()])

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
