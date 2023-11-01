"""
    Estimation Views
"""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, FormView, ListView

# Form
from Estimation.forms import ItemForm

# Models
from Estimation.models import Item


class ListItemsView(LoginRequiredMixin, ListView):
    """
    This View show all Items
    """

    model = Item
    template_name = "estimation/item/list.html"
    pk_url_kwarg = "project_pk"
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        """
        Add project ID int he context
        """
        context = super().get_context_data(**kwargs)
        context["project_id"] = self.kwargs.get(self.pk_url_kwarg)
        return context

    def get_queryset(self):
        """
        get all the items for the project
        """
        project_id = self.kwargs.get(self.pk_url_kwarg)
        queryset = Item.objects.filter(project=project_id)
        return queryset


class CreateItemView(LoginRequiredMixin, CreateView):
    """
    This View create a new Item
    """

    template_name = "estimation/item/create.html"
    pk_url_kwarg = "project_pk"
    form_class = ItemForm

    def get_context_data(self, **kwargs):
        """
        Add project ID int he context
        """
        context = super().get_context_data(**kwargs)
        context["project_id"] = self.kwargs.get(self.pk_url_kwarg)
        return context

    def get_success_url(self):
        """
        create success full url
        """
        url = reverse("estimation:list_items", kwargs={"project_pk": self.kwargs.get(self.pk_url_kwarg)})
        return url

    def form_valid(self, form):
        """
        Save obj if form is valid
        """

        obj = form.save(commit=False)
        project_id = self.kwargs.get(self.pk_url_kwarg)
        obj.project_id = project_id
        obj.save()

        return super().form_valid(form)
