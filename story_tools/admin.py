from story_tools.models.frame import Frame
from django.contrib import admin


class FrameAdmin(admin.ModelAdmin):
    list_display = ('id', 'map', 'title')
    list_filter = ('map',)
    search_fields = ('map__title', 'title', 'description',)


admin.site.register(Frame, FrameAdmin)
