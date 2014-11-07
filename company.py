# This file is part internetdomain_alert module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pyson import Bool, Eval
from trytond.pool import PoolMeta

__all__ = ['Company']
__metaclass__ = PoolMeta


class Company:
    'Company'
    __name__ = 'company.company'
    idomain = fields.Boolean('Send Email')
    idomain_template = fields.Many2One('electronic.mail.template', 'Template',
        states={
        'required': Bool(Eval('idomain')),
        },
        depends=['idomain'])

