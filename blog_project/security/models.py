# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from werkzeug.security import generate_password_hash, check_password_hash

# Create your models here.
class UserInfo(models.Model):
    password_hash = models.CharField(max_length=128)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
