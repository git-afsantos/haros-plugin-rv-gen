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

def package_analysis(iface, pkg):
    if not pkg.nodes:
        iface.log_debug('package {} has no nodes'.format(pkg.name))
        return
    r = TemplateRenderer()
    for node in pkg.nodes:
        if not node.hpl_properties:
            iface.log_debug('node {} has no properties'.format(node.node_name))
            continue
        try:
            code = r.render_rospy_node(node.hpl_properties)
            filename = node.node_name.replace('/', '.') + '.rv.py'
            with open(filename, 'w') as f:
                f.write(code)
            iface.export_file(filename)
        except Exception as e:
            iface.log_error(repr(e))

def configuration_analysis(iface, config):
    if not config.hpl_properties:
        iface.log_debug('config {} has no properties'.format(config.name))
        return
    settings = config.user_attributes.get(KEY, EMPTY_DICT)
    _validate_settings(iface, settings)
    try:
        r = TemplateRenderer()
        code = r.render_rospy_node(config.hpl_properties)
        filename = config.name + '.rv.py'
        with open(filename, 'w') as f:
            f.write(code)
        iface.export_file(filename)
    except Exception as e:
        iface.log_error(repr(e))

def _validate_settings(iface, settings):
    pass
