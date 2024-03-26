from django.contrib import admin
from .models import Question, Choice
# Register your models here.

admin.site.register(Question) #make polls modifiable
admin.site.register(Choice) #make polls modifiable