from django.urls import path

from . import views

# 定义路由，将请求路径跟处理方法关联
urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add, name='add'),
    path('query', views.query, name = "query"),
    path('update', views.update, name = 'update'),
    path('delete', views.delete, name = 'delete')
]