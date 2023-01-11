from django.contrib import admin
from .models import ToDoList
from .models import Questions, Item
from. models import Features
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Features)
admin.site.register(Item)

# 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和
 
admin.site.register(Questions)