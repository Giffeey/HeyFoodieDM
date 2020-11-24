from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.ListCategory.as_view()),
    path('category/<int:pk>/', views.DetailCategory.as_view()),
    path('ingredientCategory/',views.ListIngredientCategory.as_view()),
    path('ingredientCategory/<int:pk>/', views.DetailIngredientCategory.as_view()),
    path('ingredient/',views.ListIngredient.as_view()),
    path('ingredient/<int:pk>/', views.DetailIngredient.as_view()),
    path('menu/', views.ListMenu.as_view()),
    path('menu/<int:pk>/', views.DetailMenu.as_view()),
    path('store/', views.ListStore.as_view()),
    path('store/<int:pk>/', views.DetailStore.as_view()),
    path('salesize/', views.ListSalesize.as_view()),
    path('salesize/<int:pk>/', views.DetailSalesize.as_view()),
    path('customer/', views.ListCustomer.as_view()),
    path('order/', views.ListOrder.as_view()),
    path('orderd/', views.ListOrderDetail.as_view()),
    path('payment/', views.ListPayment.as_view()),
    path('history/', views.ListHistory.as_view())
    
]