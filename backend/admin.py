from __future__ import unicode_literals
from django.contrib import admin
from backend.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
User=get_user_model()
# Register your models here.
admin.site.register(Season)
admin.site.register(Round)
admin.site.register(Section)
admin.site.register(User,UserAdmin)
admin.site.register(Question)
admin.site.register(Evaluator)
admin.site.register(Candidates)
admin.site.register(Candidate_score)
admin.site.register(Candidate_round)


