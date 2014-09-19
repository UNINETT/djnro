from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from accounts.models import *
from edumanage.forms import *
import logging
import os

logger = logging.getLogger(__name__)
from django.views.decorators.cache import never_cache

@never_cache
def activate(request, activation_key):
	raise Exception('Activation not implemented')

