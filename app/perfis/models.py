from django.db import models

class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/')
    curriculo = models.FileField(upload_to='curriculos/')

    def __str__(self):
        return self.nome
