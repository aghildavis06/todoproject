
from . import views

from django.urls import path


urlpatterns = [
    path('',views.home,name='name'),
    path('details',views.details,name='details'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('classlistview/',views.Tasklistview.as_view(),name='classlistview'),
    path('classdetailview/<int:pk>/',views.TaskDetailview.as_view(),name='classdetailview'),
    path('classupdateview/<int:pk>/',views.TaskUpdateview.as_view(),name='classupdateview'),
    path('classdeleteview/<int:pk>/',views.TaskDeleteview.as_view(),name='classdeleteview')
     
]