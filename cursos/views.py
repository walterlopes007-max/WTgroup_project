from django.shortcuts import render, get_object_or_404
from .models import Curso
from universidades.models import Universidade


def lista_cursos(request):
    cursos = [
        # Cursos de JUST / UJS
        {
            "universidade": "JUST",
            "nome": "Computer Science & Technology",
            "descricao": "Curso de ciência da computação e tecnologia.",
            "imagem": "images/computer_science.jpg",
            "duracao": "4 anos",
        },
        {
            "universidade": "JUST",
            "nome": "Civil Engineering",
            "descricao": "Engenharia civil e construção de infraestruturas.",
            "imagem": "images/civil_engineering.jpg",
            "duracao": "4 anos",
        },
        {
            "universidade": "JUST",
            "nome": "Food Science & Engineering",
            "descricao": "Ciência dos alimentos e engenharia de produção.",
            "imagem": "images/food_science.jpg",
            "duracao": "4 anos",
        },
        {
            "universidade": "JUST",
            "nome": "Business Administration",
            "descricao": "Administração de empresas e gestão.",
            "imagem": "images/Business_Administration.jpg",
            "duracao": "4 anos",
        },
        {
            "universidade": "JUST",
            "nome": "Accounting",
            "descricao": "Contabilidade empresarial e auditoria.",
            "imagem": "images/accounting.jpg",
            "duracao": "4 anos",
        },

        # Cursos de NUPT
        {
            "universidade": "NUPT",
            "nome": "Communication Engineering",
            "descricao": "Engenharia de comunicação e redes.",
            "imagem": "images/communication_engineering.jpg",
            "duracao": "4 anos",
        },
        {
            "universidade": "NUPT",
            "nome": "Electronic Information Engineering",
            "descricao": "Engenharia de informação eletrônica.",
            "imagem": "images/electronic_information.jpg",
            "duracao": "4 anos",
        },
        {
            "universidade": "NUPT",
            "nome": "Network Engineering",
            "descricao": "Engenharia de redes de comunicação.",
            "imagem": "images/network_engineering.jpg",
            "duracao": "4 anos",
        },
        {
            "universidade": "NUPT",
            "nome": "Software Engineering",
            "descricao": "Engenharia de software e desenvolvimento de sistemas.",
            "imagem": "images/software_engineering.jpg",
            "duracao": "4 anos",
        },
        {
            "universidade": "NUPT",
            "nome": "Business Administration",
            "descricao": "Administração de empresas e gestão de negócios.",
            "imagem": "images/business_admin_nupt.jpg",
            "duracao": "4 anos",
        },

        # Cursos de Jilin Agricultural / JLNKU
        {
            "universidade": "JLNKU",
            "nome": "Business Administration",
            "descricao": "Administração e gestão empresarial.",
            "imagem": "images/business_administration.jpg",
            "duracao": "4 anos",
        },
        {
            "universidade": "JLNKU",
            "nome": "Marketing Management",
            "descricao": "Gestão de marketing e estratégias de mercado.",
            "imagem": "images/Marketing Management.jpg",
            "duracao": "4 anos",
        },
        {
            "universidade": "JLNKU",
            "nome": "International Economics & Trade",
            "descricao": "Economia internacional e comércio.",
            "imagem": "images/international_econ.jpg",
            "duracao": "4 anos",
        },
        {
            "universidade": "JLNKU",
            "nome": "Animal / Veterinary Science",
            "descricao": "Ciência animal e medicina veterinária.",
            "imagem": "images/veterinary_science.jpg",
            "duracao": "4 anos",
        },
        {
            "universidade": "JLNKU",
            "nome": "Computer Science & Technology",
            "descricao": "Ciência da computação e tecnologia.",
            "imagem": "images/computer_science.jpg",
            "duracao": "4 anos",
        },
    ]

    return render(request, 'cursos/lista.html', {'cursos': cursos})

def detalhe_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    return render(request, 'cursos/detalhe.html', {'curso': curso})
