# SPDX-License-Identifier: MIT
# Copyright © 2021 André Santos

###############################################################################
# Imports
###############################################################################

from typing import Any, Dict, Final

from pathlib import Path

from hplrv_ros.rclpy import generate_node as generate_rclpy
from hplrv_ros.rospy import generate_node as generate_rospy

###############################################################################
# Constants
###############################################################################

KEY: Final[str] = 'haros_plugin_hplrv'

EMPTY_DICT: Final[Dict[Any, Any]] = {}

################################################################################
# Plugin Entry Point
################################################################################


def package_analysis(iface, pkg):
    if not pkg.nodes:
        iface.log_debug(f'package {pkg.name} has no nodes')
        return
    for node in pkg.nodes:
        if not _has_parsed_properties(node):
            iface.log_debug(
                f'"{node.node_name}" has no parsed properties')
            continue
        topics: Dict[str, str] = _get_node_topics(node)
        filename: str = node.node_name.replace('/', '.')
        try:
            _gen_monitors(iface, node.hpl_properties, topics, filename)
        except Exception as e:
            iface.log_error(repr(e))


def configuration_analysis(iface, config):
    if not _has_parsed_properties(config):
        iface.log_debug(f'"{config.name}" has no parsed properties')
        return
    settings = config.user_attributes.get(KEY, EMPTY_DICT)
    _validate_settings(iface, settings)
    topics: Dict[str, str] = _get_config_topics(config)
    try:
        _gen_monitors(iface, config.hpl_properties, topics, config.name)
    except Exception as e:
        iface.log_error(repr(e))


################################################################################
# Helper Functions
################################################################################


def _validate_settings(_iface, _settings):
    pass


def _get_node_topics(node) -> Dict[str, str]:
    topics: Dict[str, str] = {}
    for call in node.advertise + node.subscribe:
        name: str = call.full_name
        rostype: str = call.rostype or ''
        if not '/' in rostype:
            continue
        topics[name] = rostype
    return topics


def _get_config_topics(config) -> Dict[str, str]:
    topics: Dict[str, str] = {}
    for topic in config.topics:
        name: str = topic.rosname.full
        rostype: str = topic.type
        if '?' in name or '?' in rostype:
            continue
        topics[name] = rostype
    return topics


def _has_parsed_properties(target) -> bool:
    for p in target.hpl_properties:
        if not isinstance(p, str):
            return True
    return False


def _gen_monitors(iface, properties, topics, filename: str):
    iface.log_debug(f'{properties}\n{topics}')

    # ROS1
    code: str = generate_rospy(properties, topics)
    path: Path = Path(f'{filename}_rosrv.py')
    path.write_text(code, encoding='utf8')
    mode: int = path.stat().st_mode
    mode |= (mode & 0o444) >> 2
    path.chmod(mode)
    iface.export_file(filename)

    # ROS2
    code = generate_rclpy(properties, topics)
    path = Path(f'{filename}_ros2rv.py')
    path.write_text(code, encoding='utf8')
    mode = path.stat().st_mode
    mode |= (mode & 0o444) >> 2
    path.chmod(mode)
    iface.export_file(filename)
