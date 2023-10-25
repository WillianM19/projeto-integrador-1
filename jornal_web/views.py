from django.shortcuts import render

# Create your views here.

def components(request):
    staticTags = ['Artigos', 'Eventos', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais']
    

    # highlights
    admin = False

    destaques_data = [
    {
        'imagem': 'media/img/highlights/1.png',
        'titulo': 'Aprendizado Global: Alunos da Escola VWX Participam de Intercâmbio Cultural',
    },
    {
        'imagem': 'media/img/highlights/2.png',
        'titulo': 'Aprendizado Global: Alunos da Escola VWX Participam de Intercâmbio Cultural',
    },
    {
        'imagem': 'media/img/highlights/3.png',
        'titulo': 'Aprendizado Global: Alunos da Escola VWX Participam de Intercâmbio Cultural',
    },
    {
        'imagem': 'media/img/highlights/4.png',
        'titulo': 'Aprendizado Global: Alunos da Escola VWX Participam de Intercâmbio Cultural',
    },
    {
        'imagem': 'media/img/highlights/5.png',
        'titulo': 'Aprendizado Global: Alunos da Escola VWX Participam de Intercâmbio Cultural',
    },]

    event_list = [
        {
            'week': 'set',
            'dayWeek': '12',
            'title': 'Feira de Ciências',
            'event_date': '17 de outubro de 2023 Das 14:00 às 17:00',
            'event_datetime': '2023-10-17T14:00',
        },
        {
            'week': 'set',
            'dayWeek': '12',
            'title': 'Feira de Ciências',
            'event_date': '17 de outubro de 2023 Das 14:00 às 17:00',
            'event_datetime': '2023-10-17T14:00',
        },
                {
            'week': 'set',
            'dayWeek': '12',
            'title': 'Feira de Ciências',
            'event_date': '17 de outubro de 2023 Das 14:00 às 17:00',
            'event_datetime': '2023-10-17T14:00',
        },
        {
            'week': 'set',
            'dayWeek': '12',
            'title': 'Feira de Ciências',
            'event_date': '17 de outubro de 2023 Das 14:00 às 17:00',
            'event_datetime': '2023-10-17T14:00',
        },
        {
            'week': 'set',
            'dayWeek': '12',
            'title': 'Feira de Ciências',
            'event_date': '17 de outubro de 2023 Das 14:00 às 17:00',
            'event_datetime': '2023-10-17T14:00',
        },
        {
            'week': 'set',
            'dayWeek': '12',
            'title': 'Feira de Ciências',
            'event_date': '17 de outubro de 2023 Das 14:00 às 17:00',
            'event_datetime': '2023-10-17T14:00',
        },
        {
            'week': 'set',
            'dayWeek': '12',
            'title': 'Feira de Ciências',
            'event_date': '17 de outubro de 2023 Das 14:00 às 17:00',
            'event_datetime': '2023-10-17T14:00',
        },        {
            'week': 'set',
            'dayWeek': '12',
            'title': 'Feira de Ciências',
            'event_date': '17 de outubro de 2023 Das 14:00 às 17:00',
            'event_datetime': '2023-10-17T14:00',
        },
        {
            'week': 'set',
            'dayWeek': '12',
            'title': 'Feira de Ciências',
            'event_date': '17 de outubro de 2023 Das 14:00 às 17:00',
            'event_datetime': '2023-10-17T14:00',
        },
    ]


    return render(
        request,
        'pages/components.html', {'tags': staticTags, 'admin': admin, 'event_list': event_list}
    )


def home(request):
    staticTags = ['Artigos', 'Eventos', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais']
    
    return render(
        request,
        'pages/home.html', {'tags': staticTags}
    )
    
def login(request):
    
    return render(
        request,
        'pages/login.html'
    )

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