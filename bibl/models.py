from django.db import models

# Create your models here.


class Author(models.Model):
    surname = models.CharField("Фамилия", max_length=20)
    name = models.CharField("Имя", max_length=20)
    lastname = models.CharField("Отчество", max_length=20)
    birthday = models.DateField("Дата рождения")
    deathday = models.DateField("Дата смерти", blank=True, null=True)

    def __str__(self):
        return "{} {}. {}.".format(self.surname, self.name[0], self.lastname[0])

    class Meta:
        verbose_name ="Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    title = models.CharField("Название книги", max_length=50)
    page_count = models.IntegerField("Число страниц")
    annotation = models.TextField("Аннотация")
    author = models.ForeignKey("Author", on_delete=models.CASCADE, verbose_name="Автор")
    genre = models.ManyToManyField("Genre", verbose_name="Жанр")

    def __str__(self):
        return "{} - {} с.".format(self.title, self.page_count)

    class Meta:
        verbose_name ="Книга"
        verbose_name_plural = "Книги"


class Genre(models.Model):
    title = models.CharField("Жанр", max_length=30)
    typeg = models.CharField("Группа жанра", max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ="Жанр"
        verbose_name_plural = "Жанры"
