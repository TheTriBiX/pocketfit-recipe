from django.urls import path, include
from recipeservice import views

urlpatterns = [
    path('ingredients/create',views.IngredientsCreateView.as_view(), name='ingredients_create'),
    path('ingredients/<uuid:id>', views.IngredientsDetailView.as_view(), name='ingredients_detail'),
    path('ingredients/all', views.IngredientsListView.as_view(), name='ingredients_list'),
    path('ingredients/search', views.IngredientsSearchView.as_view(), name='ingredients_search'),
    path('ingredients/update/<uuid:id>', views.IngredientsUpdateView.as_view(), name='ingredients_update'),
    path('ingredients/delete/<uuid:id>', views.IngredientsDeleteView.as_view(), name='ingredients_delete'),
    path('ingredients/delete/all', views.IngredientsDeleteAll.as_view(), name='ingredients_bulk_delete'),
    path('allergy/create/', views.AllergyCreateView.as_view(), name='allergy-create'),
    path('allergy/all/', views.AllergyListView.as_view(), name='allergy-list'),
    path('allergy/<int:id>/', views.AllergyDetailView.as_view(), name='allergy-detail'),
    path('allergy/search/', views.AllergySearchView.as_view(), name='allergy-search'),
    path('allergy/update/<int:id>/', views.AllergyUpdateView.as_view(), name='allergy-update'),
    path('allergy/delete/all/', views.AllergyDeleteAllView.as_view(), name='allergy-delete-all'),
    path('allergy/delete/<int:id>/', views.AllergyDeleteView.as_view(), name='allergy-delete'),
    path('user/allergy/', views.UserAllergyView.as_view(), name='user-allergy'),
    path('ingredients/category/create', views.IngredientsCategoryCreateView.as_view(), name='category-create'),
    path('ingredients/category/<uuid:id>', views.IngredientsCategoryDetailView.as_view(), name='category-detail'), # uuid
    path('ingredients/category/all', views.IngredientsCategoryListView.as_view(), name='category-list'),
    path('ingredients/category/search', views.IngredientsCategorySearchView.as_view(), name='category-search'),
    path('ingredients/category/update/<uuid:id>', views.IngredientsCategoryUpdateView.as_view(), name='category-update'),
    path('ingredients/category/delete/<uuid:id>', views.IngredientsCategoryDeleteView.as_view(), name='category-delete'),
    path('ingredients/category/delete/all', views.IngredientsCategoryDeleteAll.as_view(), name='category-delete-all') # Почему возвращает null
    ]