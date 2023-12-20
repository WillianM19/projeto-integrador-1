from django.db import models

class Tags(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Tags"
    
class Postador(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    imagem_perfil = models.ImageField(upload_to='uploadedImages', null=True, blank=True)
    
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Postadores"

class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.CharField(max_length=100000) #Conta com tags html
    data_de_publicacao = models.DateField()
    postador = models.ForeignKey(Postador, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)    
    capa = models.ImageField(upload_to='publicacao_capa', null=True, blank=True)
    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name_plural = "Publicações"