from rest_framework.viewsets import ModelViewSet
from .models import News, Category, Tag
from .serializers import NewsSerializer, CategorySerializer, TagSerializer

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all().order_by('-publication_date')
    serializer_class = NewsSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
