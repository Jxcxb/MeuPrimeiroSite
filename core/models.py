from django.db import models
from stdimage import StdImageField


class Base(models.Model):
    criado = models.DateTimeField('Criado', auto_now_add=True)
    modificado = models.DateTimeField('Modificado', auto_now_add=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    nome = models.CharField('Nome',max_length=100)
    descricao = models.TextField('Descrição',max_length=500)
    imagem = StdImageField('Imagem', upload_to='servicos',
                           variations={'thumb': {'width': 480, 'height': 250, 'crop': True}})

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self): #Evita que o retorno seja em object
        return self.nome

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    bio = models.TextField('Biografia', max_length=255)
    foto = StdImageField('Foto', upload_to='equipe', variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    facebook = models.CharField('Facebook', max_length=200)
    twitter = models.CharField('Twitter', max_length=200)
    instagram = models.CharField('Instagram', max_length=200)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome