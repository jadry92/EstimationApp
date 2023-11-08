"""
    Estimation urls
"""

# Django
from django.urls import path

# Views Board
from estimations.views.board import CreateBoardView, ListBoardsView

# Views Control Flow
from estimations.views.control_flow import CreateControlFlowView, ListControlFlowsView

# Views Items
from estimations.views.item import CreateItemView, ListItemsView

# Views Project
from estimations.views.project import CreateProjectView, DetailProjectView, ListProjectsView

app_name = "estimations"
urlpatterns = [
    path("", view=ListProjectsView.as_view(), name="list_projects"),
    path("new/", view=CreateProjectView.as_view(), name="create_project"),
    path("project/<int:project_pk>/", view=DetailProjectView.as_view(), name="detail_project"),
    path("project/<int:project_pk>/edit/", view=CreateProjectView.as_view(), name="edit_project"),
    path("project/<int:project_pk>/delete/", view=CreateProjectView.as_view(), name="delete_project"),
    # Boards
    path("project/<int:project_pk>/boards/", view=ListBoardsView.as_view(), name="list_boards"),
    path("project/<int:project_pk>/new-board/", view=CreateBoardView.as_view(), name="create_board"),
    path("project/<int:project_pk>/board/<int:board_pk>/", view=DetailProjectView.as_view(), name="detail_board"),
    path("project/<int:project_pk>/board/<int:board_pk>/edit/", view=CreateProjectView.as_view(), name="edit_board"),
    path(
        "project/<int:project_pk>/board/<int:board_pk>/delete/",
        view=CreateProjectView.as_view(),
        name="delete_board",
    ),
    # Items
    path("project/<int:project_pk>/items/", view=ListItemsView.as_view(), name="list_items"),
    path("project/<int:project_pk>/new-item/", view=CreateItemView.as_view(), name="create_item"),
    path("project/<int:project_pk>/item/<int:item_pk>/", view=CreateProjectView.as_view(), name="detail_item"),
    path("project/<int:project_pk>/item/<int:item_pk>/edit", view=CreateProjectView.as_view(), name="edit_item"),
    path("project/<int:project_pk>/item/<int:item_pk>/delete", view=CreateProjectView.as_view(), name="delete_item"),
    # Control
    path("project/<int:project_pk>/control-flows/", view=ListControlFlowsView.as_view(), name="list_control_flows"),
    path(
        "project/<int:project_pk>/new-control-flow/", view=CreateControlFlowView.as_view(), name="create_control_flow"
    ),
    path(
        "project/<int:project_pk>/control-flow/<int:control_flow_pk>/",
        view=CreateProjectView.as_view(),
        name="detail_control_flow",
    ),
    path(
        "project/<int:project_pk>/control-flow/<int:control_flow_pk>/edit",
        view=CreateProjectView.as_view(),
        name="edit_control_flow",
    ),
    path(
        "project/<int:project_pk>/control-flow/<int:control_flow_pk>/delete",
        view=CreateProjectView.as_view(),
        name="delete_control_flow",
    ),
    # Extra Items
]
