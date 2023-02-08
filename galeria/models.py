from django.db import models

# criamos classe de OO e o python vai traduzir as classes para o banco de dados
# nas classes criamos as colunas que queremos no banco de dados
class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return f'Fotografia [nome={self.nome}]'

# o comando " python manage.py makemigrations " para mostrar para o Django que há uma nova tabela do banco de dados que desejamos traduzir para, definitivamente, uma tabela no banco de dados.
# depois é só rodar o comando "python manage.py migrate" para rodar a migração e agora temos o banco de dados SQL lite