#This file is part internetdomain_alert module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta

import logging
import datetime

__all__ = ['Domain']
__metaclass__ = PoolMeta


class Domain:
    'Domain'
    __name__ = 'internetdomain.domain'

    @classmethod
    def generate_mail_alert(cls):
        """
        Generate Mail alert from renewals expire date.
        """
        pool = Pool()
        Company = pool.get('company.company')
        Template = pool.get('electronic.mail.template')
        cursor = Transaction().cursor
        context = Transaction().context.copy()

        for company in Company.search([('active', '=', True)]):
            if not company.idomain_template:
                logging.getLogger('internetdomain').warning(
                    'Select template in this company.')
                return True

            context['language'] = company.lang and company.lang.code or 'en_US'
            idomain_alert_expire = company.idomain_alert_expire
            if not idomain_alert_expire:
                days_alert = [30]  # 30 days; default
            else:
                days_alert = idomain_alert_expire.split(',')
                days_alert = [int(x) for x in days_alert]

            for day in days_alert:
                date_expire = datetime.date.today() + datetime.timedelta(days=day)
                cursor.execute("select domain from internetdomain_renewal as a"
                    " LEFT JOIN internetdomain_domain AS b"
                    " ON b.id = a.domain"
                    " where a.date_expire=%s AND b.company = %s AND b.active = True",
                    (date_expire, company.id))
                res = cursor.fetchall()
                ids = [r[0] for r in res]
                for domain in cls.browse(ids):
                    with Transaction().set_context(context):
                        Template.render_and_send(company.idomain_template.id, [domain])
                    logging.getLogger('internetdomain').info(
                        'Send email domain: %s' % domain.name)
        return True
