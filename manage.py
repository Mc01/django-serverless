#!/usr/bin/env python
import os
import sys

import django


def run(event, context):
    """
    Lambda entry point
    """
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'runserver'])


if __name__ == '__main__':
    """
    Local entry point
    """
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
