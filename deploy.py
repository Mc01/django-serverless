#!/usr/bin/env python


def run(event, context):
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'migrate'])
    print('Deployed!')
