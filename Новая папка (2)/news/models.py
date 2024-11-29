from django.db import models

# Категории новостей (например, "Политика", "Спорт")
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Теги (например, "Украина", "Футбол")
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Новости
class News(models.Model):
    title = models.CharField(max_length=200)  # Заголовок
    content = models.TextField()  # Текст новости
    publication_date = models.DateTimeField(auto_now_add=True)  # Дата публикации
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)  # Картинка
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Категория
    tags = models.ManyToManyField(Tag, blank=True)  # Теги

    def __str__(self):
        return self.title
