from django.db import models
from datetime import datetime

# criamos classe de OO e o python vai traduzir as classes para o banco de dados
# nas classes criamos as colunas que queremos no banco de dados
class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    dataFotografia = models.DateField(default=datetime.now, blank=False)

    def __str__(self) -> str:
        return f'Fotografia [nome={self.nome}]'

# o comando " python manage.py makemigrations " para mostrar para o Django que há uma nova tabela do banco de dados que desejamos traduzir para, definitivamente, uma tabela no banco de dados.
# depois é só rodar o comando "python manage.py migrate" para rodar a migração e agora temos o banco de dados SQL lite
# toda vez que alterarmos o model precisamos fazer uma migration. Por isso, rodamos novamente o comando makemigrations no terminal e também o migrate