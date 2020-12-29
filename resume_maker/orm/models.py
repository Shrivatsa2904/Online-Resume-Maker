from django.db import models

# Create your models here.
class persondetails(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=127)
    phone = models.CharField(max_length=127)
    email = models.CharField(max_length=127)
    linkedin = models.CharField(max_length=127, blank=True)
    github = models.CharField(max_length=127, blank=True)
    dob =  models.CharField(max_length=127, blank=True)
    address = models.CharField(max_length=127, blank=True)
    father = models.CharField(max_length=127, blank=True)
    summary =  models.TextField(max_length=2047, blank=True)

    def __unicode__(self):
        return "{}: {} at {} ({})".format(self.name,
                                          self.phone,
                                          self.email,
                                          self.linkedin,
                                          self.github,
                                          self.dob,
                                          self.address,
                                          self.father,
                                          self.summary)

class education(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name =  models.CharField(max_length=127)
    start =   models.CharField(max_length=127)
    end =  models.CharField(max_length=127)
    score =  models.CharField(max_length=127)
    subject = models.CharField(max_length=127, blank=True)
    location = models.CharField(max_length=127, blank=True)

    class meta:
        db_table = 'edudb'

    def __unicode__(self):
        return "{}: {} at {} ({})".format(self.name,
                                          self.start,
                                          self.end,
                                          self.score,
                                          self.subject,
                                          self.location
                                         )


class projects(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title =  models.CharField(max_length=127)
    description =  models.TextField(max_length=2047, blank=True)
    tech = models.CharField(max_length=127, blank=True)

    class meta:
        db_table = 'projectdb'

    def __unicode__(self):
        return "{}: {} at {} ({})".format(self.title,
                                          self.description,
                                          self.tech)


class internships(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    company =  models.CharField(max_length=127)
    start = models.CharField(max_length=127, blank=True)
    to = models.CharField(max_length=127, blank=True)
    description =  models.TextField(max_length=2047, blank=True)

    def __unicode__(self):
        return "{}: {} at {} ({})".format(self.company,
                                          self.start,
                                          self.to,
                                          self.description)


class certifications(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title =  models.CharField(max_length=127, blank=True)
    source = models.CharField(max_length=127, blank=True)

    def __unicode__(self):
        return "{}: {} at {} ({})".format(self.title,
                                          self.source)

class technical(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    languages =  models.CharField(max_length=127, blank=True)
    tools =  models.CharField(max_length=127, blank=True)
    familiar = models.CharField(max_length=127, blank=True)

    def __unicode__(self):
        return "{}: {} at {} ({})".format(self.languages,
                                          self.tools,
                                          self.familiar)