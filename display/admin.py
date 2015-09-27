from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Profile)
admin.site.register(Company)
admin.site.register(WorkExperience)
admin.site.register(PPI_scorecard)

# class ProfileAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
#
# admin.site.register(Question, QuestionAdmin)