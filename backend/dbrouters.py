from review.models import Related, Place, Country

class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        """ reading SomeModel from otherdb """
        if model in (BlackMatch,Related):
            return 'review'
        else:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """ writing SomeModel to otherdb """
        if model in (BlackMatch,Related):
            return 'review'
        else:
            return 'default'
        return None
