from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Subject)


admin.site.register(Timetable)


class CoverageInline(admin.TabularInline):
    model = Coverage
    extra = 0

class ExamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['start_date', 'end_date']})
    ]

    inlines = [CoverageInline]

admin.site.register(Exam, ExamAdmin)


admin.site.register(Deadline)