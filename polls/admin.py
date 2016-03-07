from django.contrib import admin
from polls.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone',)
