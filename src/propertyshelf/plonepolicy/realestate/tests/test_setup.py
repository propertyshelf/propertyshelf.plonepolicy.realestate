# -*- coding: utf-8 -*-
"""Test Setup of propertyshelf.plonepolicy.realestate."""

# python imports
import unittest2 as unittest

# local imports
from propertyshelf.plonepolicy.realestate.testing import PLONEPOLICY_REALESTATE_INTEGRATION_TESTING


class TestSetup(unittest.TestCase):
    """Setup Test Case for propertyshelf.plonepolicy.realestate."""
    layer = PLONEPOLICY_REALESTATE_INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer['portal']

    def test_propertyshelf_plonepolicy_base_installed(self):
        """Test that propertyshelf.plonepolicy.base is installed."""
        qi = self.portal.portal_quickinstaller
        self.assertTrue(qi.isProductInstalled('propertyshelf.plonepolicy.base'))

    def test_plone_mls_listing_installed(self):
        """Test that plone.mls.listing is installed."""
        qi = self.portal.portal_quickinstaller
        self.assertTrue(qi.isProductInstalled('plone.mls.listing'))
