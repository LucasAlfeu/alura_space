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

4° Para inserir um dado utilizamos os seguintes comandos: 
    `
        from galeria.models import Fotografia
        foto = Fotografia(nome="Nebulosa de Carina", legenda="webbtelescop.org / NASA / James Webb", foto="carina-nebula.png")
        foto.save()
    `
    lembrando que galeria é um app, então trocar galeria pelo nome do app da sua aplicação

## Acessando as informações do banco de dados

1° No arquivo views.py do nosso app importar a classe desejada 

2° Criar uma variável que acesse a nossa classe dessa maneira: ` variavel = classe_importada.objects.all() `
        EX: fotografias = Fotografia.objects.all()

3° Na hora de renderizar a o retorno da função em views, adicionar um dicionário com uma palavra qualquer que tenha o valor da variável
        EX:
         ```
            def index(request):
                fotografias = Fotografia.objects.all()
                return render(request, 'galeria/index.html', {"cards": fotografias})
        ```

4° Criar uma condicional para verificar a existencia dessa palavra no dicionario no arquivo html desejado
    EX:
     ```
        {% if cards %}
    ```

5° Podemos criar um for para acessar as informações  
        EX: {% for fotografia in cards %}

        Obs: lembrar de colocar um endfor no final do bloco