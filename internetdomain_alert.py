#This file is part internetdomain_alert module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool

import logging
import time
import datetime

class Domain(ModelSQL, ModelView):
    'Domain'
    _name = 'internetdomain.domain'

    def generate_mail_alert(self):
        """
        Generate Mail alert from renewals expire date.
        """
        pool = Pool()
        company_obj = pool.get('company.company')
        template_obj = pool.get('electronic.mail.template')

        cursor = Transaction().cursor
        context = Transaction().context.copy()

        companies = company_obj.search(['active','=',True])
        for company in company_obj.browse(companies):
            if not company.idomain_template:
                logging.getLogger('internetdomain').warning(
                    'Select template in this company.')
                return True

            context['language'] = company.lang and company.lang.code or 'en_US'
            idomain_alert_expire = company.idomain_alert_expire
            if not idomain_alert_expire:
                days_alert = [30] #30 days; default
            else:
                days_alert = idomain_alert_expire.split(',')
                days_alert = [int(x) for x in days_alert]

            for day in days_alert:
                date_expire = datetime.date.today()+datetime.timedelta(days=day)
                cursor.execute("select domain from internetdomain_renewal as a" \
                    " LEFT JOIN internetdomain_domain AS b" \
                    " ON b.id = a.domain" \
                    " where a.date_expire=%s AND b.company = %s AND b.active = True", \
                    (date_expire,company.id))
                res = cursor.fetchall()
                ids = [r[0] for r in res]
                for domain in self.browse(ids):
                    with Transaction().set_context(context):
                        template_obj.render_and_send(company.idomain_template.id, [domain.id])
                    logging.getLogger('internetdomain').info(
                        'Send email domain: %s' % domain.name)
        return True

Domain()
