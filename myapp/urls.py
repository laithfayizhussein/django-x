from django.urls import path
from .views import MyappListView, MyappDetailView, MyappCreateView, MyappUpdateView, MyappDeleteView

urlpatterns = [
    path('', MyappListView.as_view(), name='myapp_list'),
    path('<int:pk>/', MyappDetailView.as_view(), name='myapp_detail'),
    path('create/', MyappCreateView.as_view(), name='myapp_create'),
    path('<int:pk>/update/', MyappUpdateView.as_view(), name='myapp_update'),
    path('<int:pk>/delete/', MyappDeleteView.as_view(), name='myapp_delete'),
]