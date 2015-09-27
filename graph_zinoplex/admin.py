from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(GraphTreeNode)
admin.site.register(GraphLink)
admin.site.register(GraphNode)