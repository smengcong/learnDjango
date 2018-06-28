from django.contrib import admin

from app01.models import *
# Register your models here.

# admin私人定制
class BookAdmin(admin.ModelAdmin):
    # 展示的字段信息
    list_display = ('id','name','price','pub_date')
    # 可编辑的字段
    list_editable = ('name','price')
    # 可以筛选的 水平或者垂直
    filter_vertical = ('authors',)
    # 分页
    list_per_page = 3
    # 可以搜索的字段
    search_fields = ('id','publish__name')
    # 按指定字段过滤
    list_filter = ('pub_date','publish')

# admin.site.register(Author)
# admin.site.register(Book,BookAdmin)
# admin.site.register(Publish)