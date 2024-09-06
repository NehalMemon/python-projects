from django.urls import path
from . import views


urlpatterns = [
    path("split-evenly/", views.simple_bill_splitter, name='1_splitter'),
    path("spli-unevenly/", views.uneven_bill_splitter, name='2_splitter'),
    path("split-including-tip-tax/", views.tax_tip_bill_splitter, name='3_splitter'),
    path("split-with-discount/", views.discount_bill_splitter, name='4_splitter'),
    path("split-with-shared-items/", views.shared_item_splitter, name='5_splitter'),
]