#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from pathlib import Path
from setuptools import setup, find_packages



full_name = "Cam Ratchford"
email = "cameron@ratchfordconsulting.com"
description = "A low code basic web scraper driven by yaml/json config files"
github_username = "camratchford"
package_name = "Generic Scraper"
package_slug_name = __package__


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    path = os.path.join(package, "__init__.py")
    init_py = open(path, "r", encoding="utf8").read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_long_description():
    """
    Return the README.
    """

    return open("README.md", "r", encoding="utf8").read()


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]


def get_requirements(file_path='requirements.txt'):
    full_path = Path.joinpath(Path.cwd(), file_path)

    try:
        with open(full_path, 'r', encoding="utf-8") as reader:
            req_list = [str(line) for line in reader.readlines()]
    except:
        # Required for requirements files made with powershell `pip freeze > requirements.txt`
        with open(full_path, 'r', encoding="utf-16") as reader:
            req_list = [str(line) for line in reader.readlines()]

    requirements_list = [line for line in req_list if line[0] != "#"]

    return requirements_list


env_marker_cpython = (
    "sys_platform != 'win32'"
    " and (sys_platform != 'cygwin'"
    " and platform_python_implementation != 'PyPy')"
)

env_marker_win = "sys_platform == 'win32'"
env_marker_below_38 = "python_version < '3.8'"

print(get_packages(f'{package_slug_name}'))

setup(
    name=package_name,
    version="0.0.1",
    url=f"https://github.com/{github_username}/{package_slug_name}",
    license="MIT",
    description=f"{description}",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author=f"{full_name}",
    author_email=f"{email}",
    packages=find_packages(__name__),

    include_package_data=True,
    python_requires=">=3.8",
    install_requires=get_requirements(),
    extras_require={"standard": {}},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Administrators",
        "License :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    entry_points={
        # 'console_scripts': {
        #     f'{package_slug_name} = {package_slug_name}.cli:run'
        # }
    },
    project_urls={
        "Funding": f"https://github.com/sponsors/{github_username}",
        "Source": f"https://github.com/{github_username}/{package_slug_name}",
        "Changelog": f"https://github.com/{github_username}/{package_slug_name}/blob/master/CHANGELOG.md",
    },
)