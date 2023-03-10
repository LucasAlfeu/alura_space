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


## Passando uma referência ou uma variável

1° Passar uma variável através do link - ` <a href="{% url 'imagem' fotografia.id %}"> `

2° Arrumar o path no arquivo de urls.py dentro da pasta do app para indicar que vai ser enviado uma variável - ` path('imagem/<int:foto_id>', imagem, name='imagem') `

3°  No arquivo de views na pasta do app importar o metodo get_object_or_404 e indicar que essa variavels vai ser recebida. Na funcção importada vão ser passados dois parametros, a classe dos models e no pk passamos a variável que vais er recebida
```
from django.shortcuts import render, get_object_or_404

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})
```

## Acessar o Django admin

1° Rodar o código ` python manage.py createsuperuser ` para criar um login de administrador

2° Acessar o pagina de admin do djanco com ` /admin `

## Crud no Django Admin

1° importar a classe que faz o link com o banco de dados dento de models no admin.py dentro da pasta do app - ` from galeria.models import Fotografia `

2° registrar o banco de dados com o comando e passar a classe importada - ` admin.site.register(Fotografia) `

3° para facilitar a navegação dentro de admin podemos criar uma classe com os seguintes metodos:

```
class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda') # os itens que aparecem na pagina do Admistrador
    list_display_links = ('id', 'nome') # Onde podemos clicar para editar os campos dos dados
    search_fields = ('nome',) # Com esse método conseguimos fazer a busca pelo item passado como parâmetro. É importante ter a vírgula pois deve enviar uma tupla e não apenas parâmetros
```
lembrar de sempre que fizer alguma classe passar do resgister - ` admin.site.register(Fotografia, ListandoFotografias) `

## Criando categorias no banco de dados 

1° criar uma tupla com oas opções dentro dda classe no models que faz o link com o banco de dados
```
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]
```

2° adicionar na classe que faz o link com op banco de dados um novo CharFild com o atributo de ` chioces `, passando a lista de tupla

```
categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
```

3° Rodar os comandos ` python manage.py makemigrations ` e depois o ` python manage.py migrate `

## Escolhendo quais itens é mostrado na página principal pelo Admin

1°  No arquivo de models na pasta do app criar uma variável com a função BooleanFild com o default sendo falso
        EX: ` publicada = models.BooleanField(default=False) `

2° No arquivo de views trocar o ` objects.all() ` por ` objects.filter() ` passando a variavel criado anteriormente
        EX: ```   
            # fotografias = Fotografia.objects.all()
            fotografias = Fotografia.objects.filter(publicada=True) 
            ```

3° No arquivo admin dentro da classe que criamos para fazer a ponte com o banco de dados, criamos o método de ` list_editable ` e passamos a variável criada no primeiro ponto em str
        EX: ` list_editable = ("publicada",) ` - Não esquecer da virgula pois passamos uma tupla

## Importando um arquivo de imagem

1° no arquivo setting.py da pasta setup criar os comando para criar um diretório para armazenar as imagens e de onde o Django pode encontrar as imagens
    EX:```
        # Media

        MEDIA_ROOT = os.path.join(BASE_DIR, "media")

        MEDIA_URL = "/media/"
    ```
    É uma convenção escrever dessa forma

2° Adicionar os caminho ` + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) ` no arquivo de urls dentro de setup da seguinte maneira
    ```
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('galeria.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```
    OBS: lembrar de importar o settings e o static 
    ```
    from django.conf import settings
    from django.conf.urls.static import static
    ```

3° Adicionar a função ` ImageField ` dentro do arquivo models.py do app com o parametro ` upload_to= nome_da_pasta `    
    EX: ``` foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True) ``` 

4° modificar o html onde as imagens estão sendo renderizadas. Na tag de imagem no SCR colocamos o seguinte trecho de código: ` src="{{ fotografia.foto.url }}" `