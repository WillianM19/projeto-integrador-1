from django.shortcuts import render, redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from functools import reduce 
from django.http import JsonResponse

from jornal_web.models import Publicacao, Tags
from django.db.models import Q
from .foms import PublicacaoForm

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

# Create your views here.

def components(request):
    staticTags = ['Artigos', 'Eventos', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais']
    

    # highlights
    admin = False


    return render(
        request,
        'pages/components.html', {'tags': staticTags, 'admin': admin}
    )


def destaque_button_view(request, post_id):
    post = get_object_or_404(Publicacao, id=post_id)
    destaque_tag, _ = Tags.objects.get_or_create(nome='destaque')

    # Verifique se a tag "destaque" já está associada à publicação
    if destaque_tag in post.tags.all():
        # Se estiver associada, remova a tag
        post.tags.remove(destaque_tag)
        status = 'removido'
    else:
        # Se não estiver associada, adicione a tag
        post.tags.add(destaque_tag)
        status = 'adicionado'

    response_data = {'status': status}
    return JsonResponse(response_data)

def evento_button_view(request, post_id):
    post = get_object_or_404(Publicacao, id=post_id)
    evento_tag, _ = Tags.objects.get_or_create(nome='evento')

    # Verifique se a tag "evento" já está associada à publicação
    if evento_tag in post.tags.all():
        # Se estiver associada, remova a tag
        post.tags.remove(evento_tag)
        status = 'removido'
    else:
        # Se não estiver associada, adicione a tag
        post.tags.add(evento_tag)
        status = 'adicionado'

    response_data = {'status': status}
    return JsonResponse(response_data)

def get_tags_data():
    tags = Tags.objects.all()
    return tags

def home(request):
    staticTags = get_tags_data()
    
    # Destaques
    destaques = Publicacao.objects.filter(tags__nome__in=['destaque']).order_by('-data_de_publicacao')
    
    relevantSliderContent = []
    relevantCouter = 0
    
    ##Quantidade maxima de publicações exibidas
    maxRelevantAmount = 4
    
    for destaque in destaques:
        if (relevantCouter >= maxRelevantAmount): break
        
        destaque_aux = {
            'imagem': destaque.capa,
            'titulo': destaque.titulo,
        }
        
        relevantSliderContent.append(destaque_aux)
        relevantCouter +=1
        
    # Eventos
    eventos = Publicacao.objects.filter(tags__nome__in=['evento'])
    
    event_list = []
    
    for evento in eventos:
        
        post = {
            'title': evento.titulo,
            'event_date': evento.data_de_publicacao,
            'event_datetime': evento.data_de_publicacao,
            'dayWeek': evento.data_de_publicacao.day,
            'week': evento.data_de_publicacao.strftime('%B')[0:3]
        }
        
        event_list.append(post)
    
    # Posts da home
    all_posts = Publicacao.objects.all()

    # Filtra postagens por tags se a query parameter 'tags' estiver presente
    tags_filter = request.GET.getlist('tags')
    if tags_filter:
        # O Q objects para criar uma consulta OR para todas as tags
        tag_queries = [Q(tags__nome__iexact=tag) for tag in tags_filter]
        all_posts = all_posts.filter(reduce(lambda x, y: x | y, tag_queries))
        all_posts = all_posts.distinct()

    # Configurar o paginador
    paginator = Paginator(all_posts.order_by('-data_de_publicacao', '-id'), 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um número inteiro, exibir a primeira página
        posts = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do intervalo, exibir a última página
        posts = paginator.page(paginator.num_pages)
    
    
    # Admin
    admin = request.user.is_authenticated

    return render(
        request,
        'pages/home.html', {
            'tags': staticTags,
            'tags_filter':tags_filter,
            'relevantSliderContent': relevantSliderContent, 
            'event_list': event_list, 
            'posts': posts,
            'admin': admin,
        }
    )
    
def login_postador(request):
    message = None
    
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            message = 'Credenciais inválidas. Por favor, verifique os campos de e-mail e senha.'
            return render(request, 'pages/login.html',{'message':message})

    return render(request, 'pages/login.html', {'message':message})

@login_required
def logout_postador(request):
    logout(request)
    return redirect('home')

@login_required
def newPost(request):
    form = PublicacaoForm()  # Crie uma instância do formulário

    if request.method == 'POST':
        form = PublicacaoForm(request.POST)

        # Chame is_valid() corretamente, com parênteses
        if form.is_valid():
            form.save()
            form = PublicacaoForm()  # Crie um novo formulário em branco após salvar

    # Adicione o formulário ao contexto, mesmo se o método não for POST
    context = {"form": form}

    return render(request, "pages/newPost.html", context)



def search(request):

    staticTags = get_tags_data()
    
    keySearch = request.GET.get('Artigo', 'pesqusiar')
    
    postRow_list = [
        {
            "title": "Avisos de Eventos: O Que Está Acontecendo na Escola",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
            "image": "media/img/Placeholder.png",
            "author": "Autor 1",
            "created_at": " 9 setembro, 2023"
        },
        {
            "title": "Avisos de Eventos: O Que Está Acontecendo na Escola",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
            "image": "media/img/Placeholder.png",
            "author": "Autor 2",
            "created_at": " 9 setembro, 2023"
        },
        {
            "title": "Avisos de Eventos: O Que Está Acontecendo na Escola",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
            "image": "media/img/Placeholder.png",
            "author": "Autor 3",
            "created_at": " 9 setembro, 2023"
        },
        {
            "title": "Avisos de Eventos: O Que Está Acontecendo na Escola",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
            "image": "media/img/Placeholder.png",
            "author": "Autor 3",
            "created_at": " 9 setembro, 2023"
        },
        {
            "title": "Avisos de Eventos: O Que Está Acontecendo na Escola",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
            "image": "media/img/Placeholder.png",
            "author": "Autor 3",
            "created_at": " 9 setembro, 2023"
        }
    ]

    return render(
        request,
        'pages/search.html',
        {'keySearch':keySearch, 'tags':staticTags, 'postRow_list':postRow_list}
    )



def post(request):
    
    return render(
        request,
        'pages/post.html'
    )