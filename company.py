#This file is part internetdomain_alert module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool
from trytond.pyson import Bool, Eval

class Company(ModelSQL, ModelView):
    'Company'
    _name = 'company.company'

    idomain = fields.Boolean('Send Email')
    idomain_template = fields.Many2One('electronic.mail.template', 'Template',
        states={
        'required': Bool(Eval('idomain')),
        },
        depends=['vat_country'])

Company()
