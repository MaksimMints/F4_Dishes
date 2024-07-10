from dishes.models import Dishes
from .serializers import CategoriesSerializer, DishesSerializer, RecipeSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView

class Recipe_view(ReadOnlyModelViewSet):
    queryset = Dishes.objects.all()
    #print(queryset)
    serializer_class = RecipeSerializer


class Categories_view(ReadOnlyModelViewSet):
    queryset = Dishes.objects.values('categoryType').distinct()
    serializer_class = CategoriesSerializer


# @api_view(['GET'])
# def dishes_view(request):
#     if request.method == 'GET':
#         dishes = Dishes.objects.filter(categoryType=request.query_params['category'])
#         serializer = DishesSerializer(dishes, many=True)
#         return Response(serializer.data)

class DishesView(ListAPIView):
    serializer_class = DishesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # метод извлекает блюда на основе категории, предоставленной в запросе.
    def get_queryset(self):
        category = self.request.query_params.get('category')
        if category:
            return Dishes.objects.filter(categoryType=category)
        return Dishes.objects.none()

    # метод возвращает данные или сообщение об ошибке, если категория не указана или блюда не найдены.
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=200)
        return Response({"error": "Category not provided or no dishes found"}, status=400)