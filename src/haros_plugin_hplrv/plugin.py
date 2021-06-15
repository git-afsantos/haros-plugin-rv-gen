# -*- coding: utf-8 -*-

# SPDX-License-Identifier: MIT
# Copyright © 2021 André Santos

###############################################################################
# Imports
###############################################################################

from hplrv.rendering import TemplateRenderer


###############################################################################
# Constants
###############################################################################

KEY = 'haros_plugin_hplrv'

EMPTY_DICT = {}


################################################################################
# Plugin Entry Point
################################################################################

def configuration_analysis(iface, config):
    if not config.hpl_properties:
        return
    settings = config.user_attributes.get(KEY, EMPTY_DICT)
    _validate_settings(iface, settings)
    try:
        r = TemplateRenderer()
        code = r.render_node(config.hpl_properties)
        filename = config.name + '_rv.py'
        with open(filename, 'w') as f:
            f.write(code)
        iface.export_file(filename)
    except Exception as e:
        iface.log_error(repr(e))

def _validate_settings(iface, settings):
    pass
