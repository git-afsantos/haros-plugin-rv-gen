# SPDX-License-Identifier: MIT
# Copyright © 2023 André Santos

###############################################################################
# Imports
###############################################################################

from importlib.metadata import PackageNotFoundError, version  # pragma: no cover

###############################################################################
# Constants
###############################################################################

try:
    __version__ = version('haros_plugin_hplrv')
except PackageNotFoundError:  # pragma: no cover
    # package is not installed
    __version__ = 'unknown'
