"""
    Estimations Forms
"""

from django.core.exceptions import ValidationError

# Django
from django.forms import ModelForm

# Models
from estimations.models import Board, ControlFlow, ExtraItems, IO_controller, Item, Project


class IO_controllerForm(ModelForm):
    """
    IO Controller Form
    """

    class Meta:
        model = IO_controller
        fields = "__all__"


class ProjectForm(ModelForm):
    """
    Project Form
    """

    class Meta:
        model = Project
        fields = ["name", "description", "quote_number", "address"]


class ItemForm(ModelForm):
    """
    Item Form
    """

    def __init__(self, *args, **kwargs):
        self.project_id = kwargs.pop("project_id")
        super().__init__(*args, **kwargs)

    def clean_slug(self):
        """
        This method clear the slug field
        """
        slug = self.cleaned_data["slug"]
        if self.instance and self.instance.slug == slug:
            return slug

        exists = Item.objects.filter(slug=slug, project_id=self.project_id).exists()
        if exists:
            raise ValidationError("The slug already exists")

        return self.cleaned_data["slug"]

    class Meta:
        model = Item
        exclude = ["project", "control_flow"]


class ControlFlowForm(ModelForm):
    """
    Control Flow Form
    """

    class Meta:
        model = ControlFlow
        fields = "__all__"


class ExtraItemsForm(ModelForm):
    """
    Extra Items Form
    """

    class Meta:
        model = ExtraItems
        fields = "__all__"


class BoardForm(ModelForm):
    """
    Board Form
    """

    def __init__(self, *args, **kwargs):
        self.project_id = kwargs.pop("project_id")
        super().__init__(*args, **kwargs)

    def clean_name(self):
        """
        The name of the board must be unique
        """
        name = self.cleaned_data["name"]
        name = name.upper()
        if self.instance and self.instance.name == name:
            return name

        exists = Board.objects.filter(name=name, project_id=self.project_id).exists()
        if exists:
            raise ValidationError("The name already exists")

        return name

    class Meta:
        model = Board
        exclude = ["project", "total_amps"]
