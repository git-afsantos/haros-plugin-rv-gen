# -*- coding: utf-8 -*-

#Copyright (c) 2021 André Santos
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It"s nice, because now 1) we have a top level
# README file and 2) it"s easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# Courtesy of https://stackoverflow.com/a/36693250
def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


extra_files = package_files("haros_plugin_rv_gen/templates")
extra_files.append("haros_plugin_rv_gen/plugin.yaml")


setup(
    name = "haros_plugin_rv_gen",
    version = "0.1.0",
    author = "André Santos",
    author_email = "andre.f.santos@inesctec.pt",
    description = "HAROS plugin to generate runtime monitors.",
    #long_description = read("README.rst"),
    license = "MIT",
    keywords = "ros runtime-monitoring runtime-verification",
    url = "https://github.com/git-afsantos/haros-plugin-rv-gen",
    packages = find_packages(),
    #entry_points = {"console_scripts": ["haros = haros.haros:main"]},
    package_data = {"haros_plugin_rv_gen": extra_files},
    install_requires = [
        "Jinja2>=2.10.0"
    ],
    zip_safe = True
)
