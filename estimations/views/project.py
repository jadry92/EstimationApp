"""
    Estimation Views
"""


# Django

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

# Form
from estimations.forms import ProjectForm

# Models
from estimations.models import Project


class ListProjectsView(LoginRequiredMixin, ListView):
    """
    List all The projects
    """

    model = Project
    template_name = "estimation/project/list.html"
    context_object_name = "projects"


class CreateProjectView(LoginRequiredMixin, CreateView):
    """
    Create A Project
    """

    form_class = ProjectForm
    template_name = "estimation/project/create.html"
    success_url = reverse_lazy("estimations:list_projects")

    def form_valid(self, form):
        """
        This method create the project after is validated in the form
        """

        project = form.save(commit=False)
        project.user = self.request.user
        project.save()
        return super().form_valid(form)


class DetailProjectView(LoginRequiredMixin, DetailView):

    """
    This view show all the data from the project
    """

    model = Project
    pk_url_kwarg = "project_pk"
    template_name = "estimation/project/detail.html"
