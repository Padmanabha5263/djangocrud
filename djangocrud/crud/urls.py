from django.urls import path
from crud.views import CustomerView

urlpatterns = [
    path("customers/",CustomerView.as_view(), name="listview"),
    path("customers/<str:id>",CustomerView.as_view(), name="listdetailedView"),
]
