from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    content2 = models.TextField(verbose_name="Contenido 2")
    image = models.ImageField(verbose_name="Imagen", upload_to="about")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de adición")

    class Meta:
        verbose_name = "about"
        verbose_name_plural = "acercade"
        ordering = ['-created']

    def __str__(self):
        return self.title


