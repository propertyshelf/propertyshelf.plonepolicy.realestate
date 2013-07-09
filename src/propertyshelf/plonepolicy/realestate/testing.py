# -*- coding: utf-8 -*-
"""Test Layer for propertyshelf.plonepolicy.realestate."""

# zope imports
from plone.app.testing import (
    IntegrationTesting,
    PloneSandboxLayer,
    PLONE_FIXTURE,
    applyProfile,
)
from zope.configuration import xmlconfig


class PlonepolicyRealestate(PloneSandboxLayer):
    """Custom Test Layer for propertyshelf.plonepolicy.realestate."""
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        """Set up Zope for testing."""
        # Load ZCML
        import propertyshelf.plonepolicy.realestate
        xmlconfig.file(
            'configure.zcml', propertyshelf.plonepolicy.realestate,
            context=configurationContext,
        )

    def setUpPloneSite(self, portal):
        """Set up a Plone site for testing."""
        applyProfile(portal, 'propertyshelf.plonepolicy.realestate:default')


PLONEPOLICY_REALESTATE_FIXTURE = PlonepolicyRealestate()
PLONEPOLICY_REALESTATE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONEPOLICY_REALESTATE_FIXTURE, ),
    name='PlonepolicyRealestate:Integration',
)
