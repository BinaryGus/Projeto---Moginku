from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import BlogPost, Game
from .forms import ContatoForm

def blog_feed(request):
    posts_list = BlogPost.objects.order_by('-criado_em')
    paginator = Paginator(posts_list, 4)  # 4 posts por página

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'core/blog.html', {'posts': posts})

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contato')  # ou uma página de sucesso
    else:
        form = ContatoForm()
    return render(request, 'core/contato.html', {'form': form})


def home(request):
    return render(request, 'core/index.html')


def sobre(request):
    return render(request, 'core/sobre.html')

def games(request):
    all_games = Game.objects.all().order_by('-id')
    paginator = Paginator(all_games, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/games.html', {'games': page_obj})


def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'core/jogo.html', {'game': game})

