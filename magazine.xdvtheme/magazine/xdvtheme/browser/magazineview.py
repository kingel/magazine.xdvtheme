from zope.interface import implements, Interface

from Products.Five import BrowserView

from plone.app.contentlisting.interfaces import IContentListing

from Acquisition import aq_inner
from zope.component import getUtility
from Products.CMFPlone.interfaces import IPloneSiteRoot

from collective.contentleadimage.config import IMAGE_FIELD_NAME
from collective.contentleadimage.config import IMAGE_CAPTION_FIELD_NAME
from collective.contentleadimage.leadimageprefs import ILeadImagePrefsForm


class IMagazineView(Interface):
    """
    Policy Document view interface
    """


class MagazineView(BrowserView):
    """
    Policy Document browser view
    """
    implements(IMagazineView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def results(self):
        return IContentListing(self.context.getFolderContents())

    @property
    def prefs(self):
        portal = getUtility(IPloneSiteRoot)
        return ILeadImagePrefsForm(portal)

    def tag(self, obj, css_class='tileImage'):
        context = aq_inner(obj)
        field = context.getField(IMAGE_FIELD_NAME)
        titlef = context.getField(IMAGE_CAPTION_FIELD_NAME)
        if titlef is not None:
            title = titlef.get(context)
        else:
            title = ''
        if field is not None:
            if field.get_size(context) != 0:
                scale = self.prefs.desc_scale_name
                return field.tag(context, scale=scale,
                                 css_class=css_class, title=title)
        return ''
