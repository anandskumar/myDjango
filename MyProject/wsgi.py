"""
WSGI config for MyProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/home/anand/djangostack-1.11.5-0/apps/django/django_projects/MyProject')
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/anand/djangostack-1.11.5-0/apps/django/django_projects/MyProject/egg_cache")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyProject.settings")

application = get_wsgi_application()
