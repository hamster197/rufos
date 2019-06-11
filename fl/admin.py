from django.contrib import admin

from fl.models import page, content



class page_content_vd(admin.StackedInline):
    model = content
    extra = 0
    readonly_fields = ['counter']
    fieldsets = (
            ('Video content', {
            'fields': ( 'title', 'video_url','video_sub_url','counter')
        }),)
    def get_queryset(self, request):
        return content.objects.filter(tip_contenta='video')



class page_content_ad(admin.StackedInline):
    model = content
    extra = 0
    readonly_fields = ['counter']
    fieldsets = (
            ('Audio content', {
            'fields': ( 'title', 'audio_url', 'counter')
        }),)
    def get_queryset(self, request):
        return content.objects.filter(tip_contenta='audio')

class page_content_tx(admin.StackedInline):
    model = content
    extra = 0
    readonly_fields = ['counter']
    fieldsets = (
            ('Text content', {
            'fields': ( 'title', 'text', 'counter')
        }),)
    def get_queryset(self, request):
        return content.objects.filter(tip_contenta='text')




class page_fields(admin.ModelAdmin):
    inlines = [page_content_vd, page_content_ad, page_content_tx]
    list_display = ['pk','title']
    search_fields = ['^title']


admin.site.register(page, page_fields)