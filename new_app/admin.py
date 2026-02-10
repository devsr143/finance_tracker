from django.contrib import admin
from django.contrib.auth.models import User

from new_app.models import Transaction

admin.site.register(Transaction)