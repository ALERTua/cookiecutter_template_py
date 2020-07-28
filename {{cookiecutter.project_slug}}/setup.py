#!/usr/bin/env python

"""The setup script."""
import os

# noinspection PyProtectedMember,PyCompatibility
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

cur_file_dir_path = os.path.dirname(os.path.abspath(__file__))

requirements = [
    "pendulum",
    "pathlib",
    "colorama",
    "colorlog",
    "future",
]
setup_requirements = []
test_requirements = [
    "setuptools",
    "pip",
    "wheel",
    "watchdog",
    "flake8",
    "tox",
    "coverage",
    "Sphinx",
    "twine",
#    "pendulum==2.0.3; python_version < '3'",  # fixed version
#    "pendulum; python_version >= '3'",  # fixed version
    "pendulum>=2.1.2",
    "pathlib",
    "colorama",
    "colorlog",
    "future",
    "zipp",
    "pytest",
    "enum; python_version < '3'",
]

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    python_requires='>=2.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        # 'Programming Language :: Python :: 3.8',
        # 'Programming Language :: Python :: 3.9',
    ],
    description="{{ cookiecutter.project_short_description }}",
    install_requires=requirements,
    license="{{ cookiecutter.open_source_license }}",
    long_description='%s\n\n%s' % (readme, history),
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
