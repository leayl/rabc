from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=32)
    parent = models.ForeignKey("Menu", null=True, blank=True)

    def __str__(self):
        title_list = [self.title]
        p = self.parent
        while True:
            title_list.insert(0, p.title)
            p = p.parent
        return '-'.join(title_list)


class Permission(models.Model):
    title = models.CharField(max_length=32, unique=True)
    url = models.CharField(max_length=128, unique=True)
    menu = models.ForeignKey("Menu", null=True, blank=True)

    def __str__(self):
        return "{menu}----{permission}".format(menu=self.menu, permission=self.title)


class Role(models.Model):
    title = models.CharField(max_length=32, unique=True)
    permissions = models.ManyToManyField("Permission")

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    tel = models.CharField(max_length=11)
    roles = models.ManyToManyField("Role")

    def __str__(self):
        return self.name
