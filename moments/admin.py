from django.contrib import admin
from .models import Status, Reply


# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ["text", "pub_time", "pics"]
    search_fields = ["text", "pics", "user__username"]
    date_hierarchy = "pub_time"
    list_filter = ["pics", "user"]


admin.site.register(Status, StatusAdmin)
admin.site.register(Reply)
