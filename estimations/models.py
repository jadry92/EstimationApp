"""
    estimations models
"""
from django.contrib.auth import get_user_model

# Django
from django.db import models

# User Model
User = get_user_model()


class Project(models.Model):
    """
    This table has the project information
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    quote_number = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Board(models.Model):
    """
    This table has the boards of the project
    """

    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="boards")
    name = models.CharField(max_length=255)
    total_amps = models.PositiveIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    """
    This table is the items that are going to be use in the project
    """

    PHASES_OP = [(0, "unknown"), (1, "240v/P1"), (2, "415v/3P"), (3, "24DC"), (4, "24AC")]

    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    item_type = models.CharField(max_length=255)

    voltage_supply = models.IntegerField(choices=PHASES_OP, default=0)
    power = models.DecimalField("Power (kW)", max_digits=10, decimal_places=2, blank=True, null=True)
    current = models.DecimalField("I (A)", max_digits=10, decimal_places=2, blank=True, null=True)

    control_flow = models.ForeignKey(
        "ControlFlow", on_delete=models.SET_NULL, related_name="items", null=True, blank=True
    )
    board = models.ForeignKey("Board", on_delete=models.CASCADE, related_name="items", null=True, blank=True)
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="items", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class ControlFlow(models.Model):
    """
    This table is the control flow for the items
    """

    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="control_flow")
    description = models.TextField(blank=True, null=True)
    extra_items = models.ManyToManyField("ExtraItems", related_name="control_flow", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class IO_controller(models.Model):
    """
    This table is the IO controller
    """

    IO = [
        ("DI", "Digital Input"),
        ("DO", "Digital Output"),
        ("AI", "Analog Input"),
        ("AO", "Analog Output"),
    ]

    amount = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=255)
    io_type = models.CharField(max_length=2, choices=IO, default="DI")


class ExtraItems(models.Model):
    """
    This tables is the extra sensors and actuators need it to the do the control
    """

    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
