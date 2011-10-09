#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This file is part of the prometeo project.

This program is free software: you can redistribute it and/or modify it 
under the terms of the GNU Lesser General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

__author__ = 'Emanuele Bertoldi <emanuele.bertoldi@gmail.com>'
__copyright__ = 'Copyright (c) 2011 Emanuele Bertoldi'
__version__ = '0.0.2'

from django.core.urlresolvers import reverse
from django.db.models.signals import post_syncdb
from django.utils.translation import ugettext_noop as _

from prometeo.core.menus.models import *
from prometeo.core.notifications.models import Signature

from ..models import *

def fixtures(sender, created_models, **kwargs):
    """Installs fixtures for this application.
    """
    main_menu = Menu.objects.get(slug="main")

    # Menus.
    partners_menu = Menu.objects.create(
        slug="partners_menu",
        description=_("Main menu for partners app")
    )

    partner_menu = Menu.objects.create(
        slug="partner_menu",
        description=_("Main menu for partner model")
    )

    contact_menu = Menu.objects.create(
        slug="contact_menu",
        description=_("Main menu for contact model")
    )
    
    # Links.
    partners_link = Link.objects.create(
        title=_("Partners"),
        slug="partners",
        description=_("Customer & Supplier relationship management"),
        url=reverse("partner_list"),
        menu=main_menu
    )

    partner_list_link = Link.objects.create(
        title=_("Partners"),
        slug="partner-list",
        url=reverse("partner_list"),
        menu=partners_menu
    )

    contact_list_link = Link.objects.create(
        title=_("Contacts"),
        slug="contact-list",
        url=reverse("contact_list"),
        menu=partners_menu
    )

    partner_dashboard_link = Link.objects.create(
        title=_("Dashboard"),
        slug="partner-dashboard",
        url="{% url partner_detail object.pk %}",
        menu=partner_menu
    )

    partner_contacts_link = Link.objects.create(
        title=_("Contacts"),
        slug="partner-contacts",
        url="{% url partner_contacts object.pk %}",
        menu=partner_menu
    )

    partner_timeline_link = Link.objects.create(
        title=_("Timeline"),
        slug="partner-timeline",
        url="{% url partner_timeline object.pk %}",
        menu=partner_menu
    )

    contact_dashboard_link = Link.objects.create(
        title=_("Dashboard"),
        slug="contact-dashboard",
        url="{% url contact_detail object.pk %}",
        menu=contact_menu
    )

    contact_jobs_link = Link.objects.create(
        title=_("Jobs"),
        slug="contact-jobs",
        url="{% url contact_jobs object.pk %}",
        menu=contact_menu
    )
    
    # Signatures.
    partner_created_signature = Signature.objects.get_or_create(
        title=_("Partner created"),
        slug="partner-created"
    )

    partner_deleted_signature = Signature.objects.get_or_create(
        title=_("Partner deleted"),
        slug="partner-deleted"
    )

    # Creates first managed company.
    if Partner in created_models and kwargs.get('interactive', True):
        msg = "\nYou just installed Prometeo's partners system, which means you don't have " \
                "a default managed company defined.\nWould you like to create one now? (yes/no): "
        confirm = raw_input(msg)
        while 1:
            if confirm not in ('yes', 'no'):
                confirm = raw_input('Please enter either "yes" or "no": ')
                continue
            if confirm == 'yes':
                name = raw_input("Insert the company's name: ")
                vat = raw_input("Insert the VAT number (optional): ") or None
                email = raw_input("Insert the main email address (optional): ") or None
                url = raw_input("Insert the main URL address (optional): ") or None
                notes = raw_input("Insert additional notes (optional): ") or None
                if Partner.objects.create(name=name, vat_number=vat, email=email, url=url, notes=notes, is_managed=True):
                    print "Default managed company created successfully.\n"
            break
    
    post_syncdb.disconnect(fixtures)

post_syncdb.connect(fixtures)
