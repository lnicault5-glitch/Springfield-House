#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# 💡 Force the correct project path into Python's import system
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
    sys.path.insert(0, os.path.join(BASE_DIR, "springfield"))

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'springfield.settings')
    print("DEBUG: Using settings file =", os.environ.get('DJANGO_SETTINGS_MODULE'))
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