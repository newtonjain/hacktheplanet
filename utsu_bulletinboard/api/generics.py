from django.utils import timezone
from django.db import models


class ArchivableModel(models.Model):
    '''
    An abstract model class for models that are not meant to be deleted.
    Calling the delete() function on such models will result in archiving,
    which sets deleted_ts to current timestamp.

    Usage:
        class MyModel(ArchivableModel):
            ...
    '''
    deleted_ts = models.DateTimeField(
        blank=True, null=True, verbose_name='Deleted timestamp', editable=False
    )

    class Meta:
        abstract = True

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        return models.Model.__str__(self)

    def force_delete(self, *args, **kwargs):
        models.Model.delete(self, *args, **kwargs)

    def delete(self, *args, **kwargs):
        '''
        Note that overriding this function will not have effect on bulk_delete().
        ArchivableManager will take care of bulk_delete()
        '''
        self.deleted_ts = timezone.now()
        self.save()
