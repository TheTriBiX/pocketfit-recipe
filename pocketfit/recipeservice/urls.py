from django.urls import path
from recipeservice import views

urlpatterns = [
    path('ingridients/create',views.IngredientsCreateView.as_view(), name='ingredients-create'),
    path('igridients/<str:id>', views.IngredientsDetailView.as_view(), name='ingredients-detail'),
    path('ingridients/all', views.IngredientsListView.as_view(), name='ingredients-list'),
    path('ingridients/search', views.IngredientsSearchView.as_view(), name='ingredients-search'),
    path('ingridients/<str:id>', views.IngredientsUpdateView.as_view(), name='ingredients-update'),
    path('ingridients/<str:id>', views.IngredientsDeleteView.as_view(), name='ingredients-delete'),
    path('ingridients/bulk_delete', views.IngredientsBulkDeleteView.as_view(), name='ingredients-bulk-delete'),
    ]