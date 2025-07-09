from django.contrib import admin
from .models import BlogPost, ProjetoPortfolio, MensagemContato
from .models import Game
from .models import Game, GameImagem, Loja


admin.site.register(ProjetoPortfolio)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    exclude = ['imagem']
    list_display = ('titulo', 'criado_em')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('criado_em',)
    ordering = ('-criado_em',)

@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'assunto', 'email', 'enviada_em')
    search_fields = ('nome', 'email', 'assunto')
    list_filter = ('enviada_em',)
    ordering = ('-enviada_em',)


class GameImagemInline(admin.TabularInline):
    model = GameImagem
    extra = 1

class LojaInline(admin.TabularInline):
    model = Loja
    extra = 1

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
    inlines = [GameImagemInline, LojaInline]
    list_display = ('nome',)