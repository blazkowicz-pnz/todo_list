from goals import views
from django.urls import path


urlpatterns = [
    path("goal_category/create", views.GoalCategoryCreateView.as_view(), name="category-create"),
    path("goal_category/list", views.GoalCategoryListView.as_view(), name="category-list"),
    path("goal_category/<pk>", views.GoalCategoryView.as_view(), name="category-detail"),

    path("goal/create", views.GoalCreateView.as_view(), name="goal-create"),
    path("goal/list", views.GoalListView.as_view(), name="goal-list"),
    path("goal/<pk>", views.GoalView.as_view(), name="goal-detail"),
]