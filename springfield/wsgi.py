"""
WSGI config for springfield project.
"""

import os
import sys

print(">>> WSGI.py is being imported <<<")

# Force correct working directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE_DIR)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'springfield.settings')

from django.core.wsgi import get_wsgi_application

print(">>> Before get_wsgi_application() <<<")

application = get_wsgi_application()

print(">>> After get_wsgi_application() <<<")