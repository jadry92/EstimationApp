"""
    Estimation Views
"""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

# Form
from estimations.forms import ItemForm

# Models
from estimations.models import Item, Project


class EditItemView(LoginRequiredMixin, UpdateView):
    """
    This view to edit a item
    """

    form_class = ItemForm
    model = Item
    pk_url_kwarg = "item_pk"
    template_name = "estimation/item/edit.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        project_id = self.kwargs.get("project_pk")
        kwargs.update({"project_id": project_id})

        return kwargs

    def get_context_data(self, **kwargs):
        """
        Add project ID int he context
        """
        context = super().get_context_data(**kwargs)
        context["project_id"] = self.kwargs.get("project_pk")
        return context

    def get_success_url(self):
        """
        create success full url
        """
        url = reverse("estimations:list_items", kwargs={"project_pk": self.kwargs.get("project_pk")})
        return url


class DeleteItemView(LoginRequiredMixin, DeleteView):
    """
    This View delete a Item
    """

    model = Item
    pk_url_kwarg = "item_pk"
    template_name = "estimation/item/delete.html"

    def get_success_url(self):
        """
        create success full url
        """
        url = reverse("estimations:list_items", kwargs={"project_pk": self.kwargs.get("project_pk")})
        return url

    def get_context_data(self, **kwargs):
        """
        Add project ID int he context
        """
        context = super().get_context_data(**kwargs)
        context["project_id"] = self.kwargs.get("project_pk")
        return context


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
        project = get_object_or_404(Project, pk=project_id)
        queryset = Item.objects.filter(project=project)
        return queryset


class CreateItemView(LoginRequiredMixin, CreateView):
    """
    This View create a new Item
    """

    template_name = "estimation/item/create.html"
    pk_url_kwarg = "project_pk"
    form_class = ItemForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        project_id = self.kwargs.get(self.pk_url_kwarg)
        kwargs.update({"project_id": project_id})
        return kwargs

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
        url = reverse("estimations:list_items", kwargs={"project_pk": self.kwargs.get(self.pk_url_kwarg)})
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
