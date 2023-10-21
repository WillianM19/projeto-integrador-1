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
    
    return render(
        request,
        'pages/components.html', {'tags': staticTags, 'admin': admin, 'destaques_data': destaques_data}
    )


def home(request):
    staticTags = ['Artigos', 'Eventos', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais', 'Notícias', 'Tecnologia', 'Ciência e Pesquisa', 'Dicas de Estudo', 'Boas Praticas Escolares', 'Recursos Educationais']
    
    return render(
        request,
        'pages/home.html', {'tags': staticTags}
    )