from django.contrib import admin
from .models import Jobs
# Register your models here.
class JobsAdmin(admin.ModelAdmin):
    list_display = ['JobID','Title','Skills','Description']
    list_filter = ['Title']
    class Meta:
        model=Jobs
admin.site.register(Jobs,JobsAdmin)
