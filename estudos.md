Ctrl + Shift + p > pythons select interpreter > selecionar o interpretador do ven

python manage.py runserver - iniciar o servidor

## Instalando dependências do requirements.txt

pip install -r requirements.txt

## Utilizando o banco de dados do Django

1° Criar uma classe OO com os campos para o banco de dado no arquivo models.py dentro da pasta do app. Nas classes criamos as colunas que queremos no banco de dados
    Ex: `
        class Fotografia(models.Model):
            nome = models.CharField(max_length=100, null=False, blank=False)
            legenda = models.CharField(max_length=150, null=False, blank=False)
            descricao = models.TextField(null=False, blank=False)
            foto = models.CharField(max_length=100, null=False, blank=False)

            def __str__(self) -> str:
                return f'Fotografia [nome={self.nome}]'
    `

2° rodar o comando no terminal ` python manage.py makemigrations ` para iniciar as migrações, o python até cria um arquivo 0001_initial.py na pasta migrations no app

3° rodar o comando ` python manage.py migrate ` para rodas toas as migrações  