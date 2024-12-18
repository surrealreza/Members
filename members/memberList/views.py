from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .models import Contract
from .forms import ContractForm


class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = "contract_form.html"
    success_url = reverse_lazy("contract-detail")


class ContractDetailView(DetailView):
    model = Contract
    template_name = "contract_detail.html"
