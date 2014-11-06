#!/usr/bin/env python
# This file is part internetdomain_alert module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_depends


class InternetdomainAlertTestCase(unittest.TestCase):
    'Test Internet Domain Alert module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('internetdomain_alert')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        InternetdomainAlertTestCase))
    return suite
