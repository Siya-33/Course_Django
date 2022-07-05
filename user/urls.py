from django.urls import path

from . import views

urlpatterns = [
    # path('', views.toLogin),
    path('', views.home,name='logout'),
    # path('login/', views.login, name='login'),
    path('index/', views.login, name='login'),
    path('optional/', views.optional, name='optional'),
    path('register_view/', views.register_view, name='register_view'),
    path('register/', views.register, name='register'),
    path('course/<int:pIndex>', views.choosed, name='course_choosed'),
    path('choose/<str:cno>', views.choose, name='choose'),
    # path('add/<str:cno_i> <str:cname_i> <str:ccredit_i> <str:cteacher_i> <str:cdeptno_i>', views.add, name='add')
    path('edit/', views.edit, name='edit'),
    path('editData/', views.editData, name='editData'),
    path('add/', views.add, name='add'),
    path('delete/<str:cno>', views.delete, name='delete'),
    path('drop/<str:cno>', views.drop, name='drop'),
    path('root/', views.root, name='root')
]
