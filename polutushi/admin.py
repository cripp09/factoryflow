from django.contrib import admin
from .models import Polutushi

@admin.register(Polutushi)
class PolutushiAdmin(admin.ModelAdmin):
    list_display = ['ear_number', 'weight', 'weighing_datetime',
                    'comment', 'image']
    list_filter = ['weighing_datetime']
    # prepopulated_fields = {'slug': ('name',)}
    # actions = [import_from_csv]
