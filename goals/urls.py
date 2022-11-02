from django.urls import path

from goals.views import GoalCategoryCreateView, GoalCategoryListView, GoalCategoryView, GoalCreateView, GoalListView, \
    GoalView, GoalCommentCreateView, GoalCommentListView, GoalCommentView

from goals.views import BoardCreateView, BoardListView, BoardView



urlpatterns = [

    path("board/create", BoardCreateView.as_view(), name="board-create"),
    path("board/list", BoardListView.as_view(), name="board-list"),
    path("board/<pk>", BoardView.as_view(), name="board-detail"),

    path("goal_category/create", GoalCategoryCreateView.as_view(), name="category-create"),
    path("goal_category/list", GoalCategoryListView.as_view(), name="category-list"),
    path("goal_category/<pk>", GoalCategoryView.as_view(), name="category-detail"),

    path("goal/create", GoalCreateView.as_view(), name="goal-create"),
    path("goal/list", GoalListView.as_view(), name="goal-list"),
    path("goal/<pk>", GoalView.as_view(), name="goal-detail"),

    path("goal_comment/create", GoalCommentCreateView.as_view(), name="create-comment"),
    path("goal_comment/list", GoalCommentListView.as_view(), name="comment-list"),
    path("goal_comment/<pk>", GoalCommentView.as_view(), name="comment-detail"),
]
