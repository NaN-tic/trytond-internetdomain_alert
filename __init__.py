# This file is part internetdomain_alert module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .company import *
from .internetdomain_alert import *


def register():
    Pool.register(
        Company,
        Domain,
        module='internetdomain_alert', type_='model')
