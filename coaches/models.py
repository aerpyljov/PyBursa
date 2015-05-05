from django.conf import settings
from django.db import models


class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField()
    gender_choises = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=gender_choises, default='M')
    phone = models.CharField(max_length=18, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    skype = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.user)

    def admin_thumbnail(self):
        if self.image:
            return u'<img src="%s" width="100" />' % (self.image.url)
        else:
            return '(No image)'
    admin_thumbnail.short_description = 'Image'
    admin_thumbnail.allow_tags = True

    def admin_name(self):
        if self.user:
            return u'%s %s' % (self.user.last_name, self.user.first_name)
        else:
            return '(No name)'
    admin_name.short_description = 'Name'
    admin_name.allow_tags = True

    def admin_email(self):
        if self.user:
            return self.user.email
        else:
            return '(No email)'
    admin_email.short_description = 'Email'
    admin_email.allow_tags = True

    class Meta:
        verbose_name_plural = "coaches"
