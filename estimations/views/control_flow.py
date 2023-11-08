"""
    Control flow views
"""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, ListView

# Form
from estimations.forms import ControlFlowForm

# Models
from estimations.models import ControlFlow


class ListControlFlowsView(LoginRequiredMixin, ListView):
    """
    List all The projects
    """

    model = ControlFlow
    template_name = "estimation/control_flow/list.html"
    context_object_name = "control_flows"
    pk_url_kwarg = "project_pk"

    def get_context_data(self, **kwargs):
        """
        Add project ID int he context
        """
        context = super().get_context_data(**kwargs)
        context["project_id"] = self.kwargs.get("project_pk")
        return context

    def get_queryset(self):
        """
        get all the control flows for the project
        """
        project_id = self.kwargs.get("project_pk")
        queryset = ControlFlow.objects.filter(project=project_id)
        return queryset


class CreateControlFlowView(LoginRequiredMixin, CreateView):
    """
    This view create a new control flow
    """

    form_class = ControlFlowForm
    template_name = "estimation/control_flow/create.html"
    pk_url_kwarg = "project_pk"

    def get_context_data(self, **kwargs):
        """
        Add project ID int he context
        """
        context = super().get_context_data(**kwargs)
        context["project_id"] = self.kwargs.get(self.pk_url_kwarg)
        return context

    def get_success_url(self):
        """
        Return to the project detail
        """
        project_id = self.kwargs.get(self.pk_url_kwarg)
        return reverse("estimations:detail_project", kwargs={"project_pk": project_id})

    def form_valid(self, form):
        """
        Create the control flow row
        """
        cf_instance = form.save(commit=False)
        project_id = self.kwargs.get(self.pk_url_kwarg)
        cf_instance.project_id = project_id
        cf_instance.save()
        return super().form_valid(form)
