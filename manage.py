#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

#  Copyright (c) 2025. aaron.
#
#  This program is under the GPL-3.0 license.
#  if you have not received it or the program has several bugs, please let me know:
#  <communicate_aaron@outlook.com>.
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'essay_correction.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
