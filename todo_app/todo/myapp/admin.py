from django.contrib import admin
from .models import Item
from django.http import HttpResponse
import csv
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    search_fields=['title']
    list_filter=['priority']
    list_display=['title','description','created_date','todo_task_date','modified_date','priority']
    actions = ['download_csv']

    def download_csv(self, request, queryset):

        f = open('some.csv','w')
        writer = csv.writer(f)
        writer.writerow(['title','description','created_date','todo_task_date','modified_date','priority'])
        for s in queryset.all():
            writer.writerow([s.title, s.description, s.created_date, s.todo_task_date, s.modified_date,s.priority])

        f.close()

        f = open('some.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response

admin.site.register(Item,ItemAdmin)
