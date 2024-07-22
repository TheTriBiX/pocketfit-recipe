from django.urls import path
from recipeservice import views

urlpatterns = [
    path('ingridients/create',views.IngredientsCreateView.as_view(), name='ingredients-create'),
    path('ingridients/<uuid:id>', views.IngredientsDetailView.as_view(), name='ingredients-detail'),
    path('ingridients/all', views.IngredientsListView.as_view(), name='ingredients-list'),
    path('ingridients/search', views.IngredientsSearchView.as_view(), name='ingredients-search'),
    path('ingridients/update/<uuid:id>', views.IngredientsUpdateView.as_view(), name='ingredients-update'),
    path('ingridients/delete/<uuid:id>', views.IngredientsDeleteView.as_view(), name='ingredients-delete'),
    path('ingridients/delete/all', views.IngredientsDeleteAll.as_view(), name='ingredients-bulk-delete'),
    ]