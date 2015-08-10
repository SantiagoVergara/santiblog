from django.db import models


# Create your models here.

class Categoria(models.Model):
    titulo_txt = models.CharField('Titulo', max_length=20)
    def __str__(self):
        return self.titulo_txt

class Post(models.Model):
    class Meta:
        ordering=['-fecha_pub']
    
    titulo_txt = models.CharField('Titulo', max_length=20)
    fecha_pub = models.DateTimeField('date published', auto_now_add=True)
    txt_resumen = models.CharField('Resumen', max_length=50)
    txt_cont = models.TextField('Contenido')
    categoria = models.ForeignKey(Categoria)
    
    def __str__(self):
        return self.titulo_txt
                                
class Coment(models.Model):
    fecha_pub = models.DateTimeField('date published', auto_now_add=True)
    titulo_txt = models.CharField('Titulo del Comentario', max_length=20)
    coment_txt = models.TextField('Comentatrio', max_length=100)
    published = models.BooleanField(u'Publicado?', default=True)
    post = models.ForeignKey(Post)
    def __str__(self):
        return self.titulo_txt
