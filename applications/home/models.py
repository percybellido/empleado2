from django.db import models

class Prueba(models.Model):
    titulo=models.CharField(max_length=30)
    subtitulo=models.CharField(max_length=30)
    cantidad=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.titulo + '-'+ self.subtitulo+ '-'+self.cantidad
