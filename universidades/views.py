from django.shortcuts import render
from django.shortcuts import get_object_or_404


def lista(request):
    universidades = [
        {
            "nome": "Jiangsu University of Science and Technology (JUST)",
            "pais": "China",
            "descricao": "Uma das principais universidades tecnológicas da China, com foco em engenharia, gestão e inovação.",
            "site": "https://www.just.edu.cn/",
            "imagem": "images/just.jpg",
        },
        {
            "nome": "Nanjing University of Posts and Telecommunications (NUPT)",
            "pais": "China",
            "descricao": "Reconhecida internacionalmente na área de telecomunicações e tecnologias da informação.",
            "site": "https://www.njupt.edu.cn/",
            "imagem": "images/nupt.jpg",
        },
        {
            "nome": "Universidade de Ciências e Tecnologia Agrícola de Jilin (吉林农业科技学院)",
            "pais": "China",
            "descricao": "Universidade localizada na província de Jilin, especializada em ciências agrícolas, biotecnologia, engenharia ambiental e tecnologia alimentar. Reconhecida pelo foco em inovação, pesquisa e sustentabilidade.",
            "site": "https://www.jlnku.edu.cn/",
            "imagem": "images/jilin_agricultural.jpg",
        },
    ]

    return render(request, 'universidades/lista.html', {'universidades': universidades})


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
            "imagem": "images/business_admin.jpg",
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
            "imagem": "images/business_admin_jlnku.jpg",
            "duracao": "4 anos",
        },
        {
            "universidade": "JLNKU",
            "nome": "Marketing Management",
            "descricao": "Gestão de marketing e estratégias de mercado.",
            "imagem": "images/marketing_jlnku.jpg",
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
            "imagem": "images/computer_science_jlnku.jpg",
            "duracao": "4 anos",
        },
    ]

    return render(request, 'cursos/lista.html', {'cursos': cursos})
        
  
def detalhe_universidade(request, universidade_id):
    # ⚠️ Este é apenas um placeholder (simulação simples)
    # Como ainda não temos um banco de dados, ele apenas renderiza a página de detalhes.
    return render(request, 'universidades/detalhe.html', {
        'universidade_id': universidade_id
    })

