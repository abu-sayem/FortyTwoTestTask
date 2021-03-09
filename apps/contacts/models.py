from django.db import models


class Contact(models.Model):
    """ Contact model contains user information """

    name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    contacts = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    jabber = models.EmailField(blank=True)
    skype = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    other_contacts = models.TextField(blank=True)

    def __str__(self):
        return self.name + ' ' + self.last_name


class Log(models.Model):
    """ Log model contains HTTP requests information """

    path = models.CharField(max_length=255, blank=True)
    method = models.CharField(max_length=255, blank=True)
    user = models.CharField(max_length=255, blank=True)
    browser = models.CharField(max_length=255, blank=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.path + ', ' + self.user + ', ' + self.browser
