from django.contrib import admin
from users.models import User, JobSeeker, Company

# Register your models here.
admin.site.register(User)
admin.site.register(Company)
admin.site.register(JobSeeker)