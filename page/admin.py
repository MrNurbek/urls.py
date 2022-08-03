from django.contrib import admin
from page.models import *


class TableInline(admin.TabularInline):
    model = Fanlar


# Register your models here.
class TableAdmin(admin.ModelAdmin):
    inlines = [TableInline]


admin.site.register(Customuser)
admin.site.register(GroupName)
admin.site.register(SubjectName)
admin.site.register(Teacher)
admin.site.register(RoomNo)
admin.site.register(Table, TableAdmin)
admin.site.register(Fanlar)
