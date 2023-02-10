from django.contrib import admin
from galeria.models import Fotografia

# Nesse arquivo fazemos todas as configurações da pagina de admin do Django

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada') # os itens que aparecem na pagina do Admistrador
    list_display_links = ('id', 'nome') # Onde podemos clicar para editar os campos dos dados
    search_fields = ('nome',) # Com esse método conseguimos fazer a busca pelo item passado como parâmetro
    list_filter = ("categoria",) # Com esse método criamos uma lista de filtros
    list_editable = ("publicada",)
    list_per_page = 10 # Definimos quantos itens teremos em cada página na area de admin

# Toda vez que criarmos uma classe dentro desse arquivo precisamos listar dentro desse register

admin.site.register(Fotografia, ListandoFotografias)