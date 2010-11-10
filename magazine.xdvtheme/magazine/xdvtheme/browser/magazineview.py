from zope.interface import implements, Interface

from Products.Five import BrowserView
# from Products.CMFCore.utils import getToolByName
# from magazine.xdvtheme import pdpMessageFactory as _


class IMagazineView(Interface):
    """
    Policy Document view interface
    """


class MagazineView(BrowserView):
    """
    Policy Document browser view
    """
    implements(IMagazineView)
