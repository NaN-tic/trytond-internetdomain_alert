#This file is part internetdomain_alert module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
{
    'name': 'Internet Domain Alert',
    'name_ca_ES': 'Alertas dominis internet',
    'name_es_ES': 'Alerta dominis internet',
    'version': '2.4.0',
    'author': 'Zikzakmedia',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''Email in renewals domain''',
    'description_ca_ES': '''Correu electrónic en les renovacions de domini''',
    'description_es_ES': '''Correo electrónico en las renovaciones de dominio''',
    'depends': [
        'internetdomain',
        'electronic_mail_template',
    ],
    'xml': [
        'company.xml',
        'internetdomain_alert.xml',
    ],
    'translation': [
        'locale/ca_ES.po',
        'locale/es_ES.po',
    ]
}
