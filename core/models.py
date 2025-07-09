from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

class BlogPost(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='blog/', blank=True, null=True)
    conteudo = RichTextUploadingField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    from django.db import models

class ProjetoPortfolio(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.titulo
    
class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    enviado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"
    
class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    assunto = models.CharField(max_length=150)
    email = models.EmailField()
    mensagem = models.TextField()
    enviada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.assunto})"
    

class Game(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='games/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
    
class GameImagem(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='galeria')
    imagem = models.ImageField(upload_to='games/galeria/')
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordem']

class Loja(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='lojas')
    nome = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return f"{self.nome} - {self.game.nome}"
