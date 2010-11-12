from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import ISchemaExtender
from Products.Archetypes.public import SelectionWidget, DisplayList
from collective.folderishpage.interfaces import IATFolderishDocument

from Products.Archetypes.public import StringField
from archetypes.schemaextender.field import ExtensionField


class MyStringField(ExtensionField, StringField):
    """A trivial field."""


class PageExtender(object):
    adapts(IATFolderishDocument)
    implements(ISchemaExtender)

    fields = [
        MyStringField("magazine_part",
        vocabulary=DisplayList((("thema", "thema"),
                                ("collectie", "collectie"),
                                ("interview", "interview"),
                                ("lifestyle", "lifestyle"),
                                ("interactie", "interactie"),
                                ("nieuw", "nieuw"),
                                )),
        widget=SelectionWidget(
            label="Magazine onderdeel",
            format='select'
            )),
            ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
