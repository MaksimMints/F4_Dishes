from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import Categories_view, DishesView, Recipe_view
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

router = DefaultRouter()
router.register('categories', Categories_view)
router.register('recipe', Recipe_view)

urlpatterns = [
    path('', include(router.urls)),
    path('dishes/', DishesView.as_view(), name='dishes'),
    path('openapi', get_schema_view(
         title="Your Project",
         description="Recipes_F4",
         version="1.0.0"
         ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]