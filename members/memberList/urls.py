from django.urls import path
from .views import ContractCreateView, ContractDetailView

urlpatterns = [
    path("contract/new/", ContractCreateView.as_view(), name="contract-create"),
    path("contract/<int:pk>/", ContractDetailView.as_view(), name="contract-detail"),
]
