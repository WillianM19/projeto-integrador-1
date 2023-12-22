import datetime
from django.shortcuts import render
from jornal_web.models import Publicacao
import locale
from .foms import PublicacaoForm
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


def home(request):
    staticTags = ['Artigos', 'Eventos', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais']
    
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
    
    posts = [
        {
            'title': 'Avisos de Eventos: O Que Está Acontecendo na Escola',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
        {
            'title': 'Avisos de Eventos: O Que Está Acontecendo na Escola',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
        {
            'title': 'Avisos de Eventos: O Que Está Acontecendo na Escola',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
        {
            'title': 'Avisos de Eventos: O Que Está Acontecendo na Escola',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
        {
            'title': 'Avisos de Eventos: O Que Está Acontecendo na Escola',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
        {
            'title': 'Avisos de Eventos: O Que Está Acontecendo na Escola',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
                {
            'title': 'Avisos de Eventos: O Que Está Acontecendo na Escola',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
        {
            'title': 'Avisos de Eventos: O Que Está Acontecendo na Escola',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
        {
            'title': 'Avisos de Eventos: O Que Está Acontecendo na Escola',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
    ]
    
    # Admin
    admin = True
    
    return render(
        request,
        'pages/home.html', {
            'tags': staticTags, 
            'relevantSliderContent': relevantSliderContent, 
            'event_list': event_list, 
            'posts': posts,
            'admin': admin,
        }
    )
    
def login(request):
    
    return render(
        request,
        'pages/login.html'
    )
    
from django.shortcuts import render, redirect


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

    staticTags = ['Artigos', 'Eventos', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais']

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