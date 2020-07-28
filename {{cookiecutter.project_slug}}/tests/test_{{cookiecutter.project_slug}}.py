#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=redefined-outer-name
""" {{ cookiecutter.project_name }} Tests """
from __future__ import print_function, unicode_literals
from typing import TYPE_CHECKING
import pytest

from {{cookiecutter.project_slug}}.{{cookiecutter.project_slug}} import {{ cookiecutter.project_name.replace(' ', '_') }}

if TYPE_CHECKING:
    pass


@pytest.fixture
def {{cookiecutter.project_slug}}_fixture():
    return {{ cookiecutter.project_name.replace(' ', '_') }}.instantiate(name='name')


def test_instance_exception():
    with pytest.raises(ValueError):
        {{ cookiecutter.project_name.replace(' ', '_') }}('something')


def test_positive({{cookiecutter.project_slug}}_fixture):
    pass