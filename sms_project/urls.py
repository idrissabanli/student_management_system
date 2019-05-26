from django.urls import path
# from .views import BaseIndexView

from sms_project import views

app_name = "core"

urlpatterns = [
    path('', views.DashBoard.as_view(), name="dashboard"),
    path('table/<int:id>/', views.TableView.as_view(), name="table"),
]