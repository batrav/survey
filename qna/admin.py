from django.contrib import admin
from .models import Survey
# Register your models here.


class SurveyAdmin(admin.ModelAdmin):
    # list_filter = ("author", "date", "tags")
    # prepopulated_fields = {"slug":("title",)}
    list_display = ("pk","first_name","last_name")

admin.site.register(Survey, SurveyAdmin)