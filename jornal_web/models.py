import re
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

class AppUserManager(BaseUserManager):
    def create_user(self, email, nome, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo de e-mail deve ser preenchido')
        
        if not nome:
            raise ValueError('O campo de nome deve ser preenchido')
        
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, nome, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo de e-mail deve ser preenchido')

        if not nome:
            raise ValueError('O campo de nome deve ser preenchido')

        user = self.create_user(email=email, nome=nome, password=password, **extra_fields)

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user

class Postador(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    imagem_perfil = models.ImageField()
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AppUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Postadores"

class Tags(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Tags"

class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = RichTextUploadingField() #Conta com tags html
    data_de_publicacao = models.DateField()
    postador = models.ForeignKey(Postador, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)    
    capa = models.ImageField(upload_to='publicacao_capa')
    
    def shortDescription(self):
        try:
            description = re.fullmatch('<p>(.+)</p>', self.conteudo).group(1)
        except:
            description = "Acesse a publicação para ver mais detalhes..."
            
        return description

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name_plural = "Publicações"