from django.urls import path, include
from recipeservice import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('ingridients/create',views.IngredientsCreateView.as_view(), name='ingredients_create'),
    path('ingridients/<uuid:id>', views.IngredientsDetailView.as_view(), name='ingredients_detail'),
    path('ingridients/all', views.IngredientsListView.as_view(), name='ingredients_list'),
    path('ingridients/search', views.IngredientsSearchView.as_view(), name='ingredients_search'),
    path('ingridients/update/<uuid:id>', views.IngredientsUpdateView.as_view(), name='ingredients_update'),
    path('ingridients/delete/<uuid:id>', views.IngredientsDeleteView.as_view(), name='ingredients_delete'),
    path('ingridients/delete/all', views.IngredientsDeleteAll.as_view(), name='ingredients_bulk_delete'),
    path('allergy/create/', views.AllergyCreateView.as_view(), name='allergy-create'),
    path('allergy/all/', views.AllergyListView.as_view(), name='allergy-list'),
    path('allergy/<int:id>/', views.AllergyDetailView.as_view(), name='allergy-detail'),
    path('allergy/search/', views.AllergySearchView.as_view(), name='allergy-search'),
    path('allergy/update/<int:id>/', views.AllergyUpdateView.as_view(), name='allergy-update'),
    path('allergy/delete/all/', views.AllergyDeleteAllView.as_view(), name='allergy-delete-all'),
    path('allergy/delete/<int:id>/', views.AllergyDeleteView.as_view(), name='allergy-delete'),
    path('user/allergy/', views.UserAllergyView.as_view(), name='user-allergy'),
    ]