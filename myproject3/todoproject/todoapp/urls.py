from . import views
from django.urls import path
urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cpvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cpvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='cpvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='cpvdelete'),
    #path('details',views.details,name='details')
]
