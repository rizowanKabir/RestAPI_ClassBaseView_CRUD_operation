from django.contrib import admin
from .models import Learn_rset

# Register your models here.

@admin.register(Learn_rset)
class Lear_Admin(admin.ModelAdmin):
    list_display = ['id','teacher_name','course_name','course_duration','seat']
    

