from django.urls import path

from . import views

# recipes:recipe
app_name = "recipes"

urlpatterns = [
    path('', views.home, name="home"),  # Home
    path('recipes/<int:id>/', views.recipe, name="recipe"),  # Recipes
    path('recipes/category/<int:category_id>/',
         views.category, name="category"),  # Category
]
