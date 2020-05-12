from mongoengine import Document, EmbeddedDocument, ReferenceField, \
        StringField, DateTimeField, ListField


class UserModel(Document):
    meta = {'collection': 'users'}
    username = StringField()
    firstname = StringField()
    lastname = StringField()
    locations = ListField(StringField())
    date = DateTimeField()
    password = StringField()

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    def __unicode__(self):
        return "%s %s" % (self.firstname, self.lastname)
