from django.shortcuts import render

# Create your views here.

def components(request):
    staticTags = ['Artigos', 'Eventos', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais']
    

    # highlights
    admin = False


    return render(
        request,
        'pages/components.html', {'tags': staticTags, 'admin': admin, 'event_list': event_list}
    )


def home(request):
    staticTags = ['Artigos', 'Eventos', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais']
    
    relevantSliderContent = [
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
    
    posts = [
        {
            'title': 'Publicação',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
        {
            'title': 'Publicação',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
        {
            'title': 'Publicação',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
        {
            'title': 'Publicação',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
        {
            'title': 'Publicação',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
        {
            'title': 'Publicação',
            'image': 'media/img/Placeholder.png',
            'author': 'Usuário',
            'created_at': '22 de Outubro de 2023',
            'admin': False,
        },
    ]
    
    return render(
        request,
        'pages/home.html', {
            'tags': staticTags, 
            'relevantSliderContent': relevantSliderContent, 
            'event_list': event_list, 
            'posts': posts,
        }
    )
    
def login(request):
    
    return render(
        request,
        'pages/login.html'
    )