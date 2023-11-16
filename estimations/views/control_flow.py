"""
    Control flow views
"""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView

# Form
from estimations.forms import ControlFlowForm, ExtraItemsForm, IO_controllerForm

# Models
from estimations.models import ControlFlow, Item


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


class CreateControlFlowView(LoginRequiredMixin, TemplateView):
    """
    This view create a new control flow
    """

    template_name = "estimation/control_flow/create.html"
    pk_url_kwarg = "project_pk"

    def get_context_data(self, **kwargs):
        """
        Add project ID int he context
        """
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs.get(self.pk_url_kwarg)
        context["project_id"] = project_id
        context["fan_list"] = Item.objects.filter(project=project_id, item_type="fan")
        return context

    def get_success_url(self):
        """
        Return to the project detail
        """
        project_id = self.kwargs.get(self.pk_url_kwarg)
        return reverse("estimations:list_control_flows", kwargs={"project_pk": project_id})

    def post(self, request, *args, **kwargs):
        """
        Create a new control flow
        """
        print(request.POST)
        cf = {}

        cf["project"] = self.kwargs.get(self.pk_url_kwarg)
        fans_id = request.POST.getlist("fan-selected")
        cf["notes"] = request.POST.get("notes")
        io_list = []
        io_count = 1
        extra_item_list = []

        while True:
            if request.POST.getlist(f"IO-{io_count}-name"):
                break

            io_data = {}
            io_data["name"] = request.POST.getlist(f"IO-{io_count}-name")

            io_data["io_type"] = request.POST.getlist(f"IO-{io_count}-type")
            io_data["amount"] = request.POST.getlist(f"IO-{io_count}-amount")
            print(io_data)
            if request.POST.get(f"IO-{io_count}-extra"):
                extra_item = {}
                extra_item["name"] = io_data["name"]
                extra_item["amount"] = io_data["amount"]
                extra_item_list.append(extra_item)

            io_list.append(io_data)

            io_count += 1

        # IO
        io_list_id = []
        for io_data in io_list:
            form = IO_controllerForm(io_data)
            if form.is_valid():
                instance = form.save()
                io_list_id.append(instance.id)
            else:
                return self.render_to_response(self.get_context_data(form=form))

        # Extra items
        extra_item_list_id = []
        for extra_item in extra_item_list:
            form = ExtraItemsForm(extra_item)
            if form.is_valid():
                instance = form.save()
                extra_item_list_id.append(instance.id)
            else:
                return self.render_to_response(self.get_context_data(form=form))

        # Save the control flow
        cf["extra_items"] = extra_item_list_id
        cf["IO_controller"] = io_list_id

        form = ControlFlowForm(cf)
        if form.is_valid():
            instance = form.save()
            cf_id = instance.id
        else:
            return self.render_to_response(self.get_context_data(form=form))

        # Add the fans to the control flow
        for fan_id in fans_id:
            fan = Item.objects.get(id=fan_id)
            fan.control_flow = cf_id
            fan.save()

        return HttpResponseRedirect(self.get_success_url())
