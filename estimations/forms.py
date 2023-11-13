"""
    Estimations Forms
"""

from django import forms

# Django
from django.forms import ModelForm

# Models
from estimations.models import Board, ExtraItems, Item, Project


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

    class Meta:
        model = Item
        exclude = ["project", "control_flow"]


class ControlFlowForm(forms.Form):
    """
    Control Flow Form
    """

    description = forms.Textarea()


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

    class Meta:
        model = Board
        fields = "__all__"
