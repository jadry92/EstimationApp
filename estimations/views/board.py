"""
    Board Views
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

# Django
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

# Forms
from estimations.forms import BoardForm

# Models
from estimations.models import Board


class ListBoardsView(LoginRequiredMixin, ListView):
    """
    This View show all Boards
    """

    model = Board
    template_name = "estimation/board/list.html"
    pk_url_kwarg = "project_pk"
    context_object_name = "boards"

    def get_context_data(self, **kwargs):
        """
        Add project ID int he context
        """
        context = super().get_context_data(**kwargs)
        context["project_id"] = self.kwargs.get(self.pk_url_kwarg)
        return context

    def get_queryset(self):
        """
        get all the boards for the project
        """
        project_id = self.kwargs.get(self.pk_url_kwarg)
        queryset = Board.objects.filter(project=project_id)
        return queryset


class CreateBoardView(LoginRequiredMixin, CreateView):
    """
    This View create a new Board
    """

    template_name = "estimation/board/create.html"
    pk_url_kwarg = "project_pk"
    form_class = BoardForm

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
        url = reverse("estimations:list_boards", kwargs={"project_pk": self.kwargs.get(self.pk_url_kwarg)})
        return url

    def form_valid(self, form):
        """
        Save the new board
        """
        project_id = self.kwargs.get(self.pk_url_kwarg)
        board_instance = form.save(commit=False)
        print(board_instance)
        print(project_id)
        board_instance.project_id = project_id
        board_instance.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        """
        Adding project_id to the form
        """
        kwargs = super().get_form_kwargs()
        project_id = self.kwargs.get(self.pk_url_kwarg)
        kwargs.update({"project_id": project_id})
        return kwargs


class DeleteBoardView(LoginRequiredMixin, DeleteView):
    """
    This View delete a Board
    """

    model = Board
    template_name = "estimation/board/delete.html"
    pk_url_kwarg = "board_pk"

    def get_success_url(self):
        """
        create success full url
        """
        url = reverse("estimations:list_boards", kwargs={"project_pk": self.kwargs.get("project_pk")})
        return url

    def get_context_data(self, **kwargs):
        """
        Add project ID int he context
        """
        context = super().get_context_data(**kwargs)
        context["project_id"] = self.kwargs.get("project_pk")
        return context


class EditBoardView(LoginRequiredMixin, UpdateView):
    """
    This view to edit a Board
    """

    model = Board
    form_class = BoardForm
    pk_url_kwarg = "board_pk"
    template_name = "estimation/board/edit.html"

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
        url = reverse("estimations:list_boards", kwargs={"project_pk": self.kwargs.get("project_pk")})
        return url
