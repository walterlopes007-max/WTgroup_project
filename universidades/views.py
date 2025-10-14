from django.shortcuts import render

def lista(request):
    universidades = [
        {
            "nome": "Jiangsu University of Science and Technology (JUST)",
            "pais": "China",
            "descricao": "Uma das principais universidades tecnológicas da China, com foco em engenharia, gestão e inovação.",
            "site": "https://www.just.edu.cn/"
        },
        {
            "nome": "Nanjing University of Posts and Telecommunications (NUPT)",
            "pais": "China",
            "descricao": "Reconhecida internacionalmente na área de telecomunicações e tecnologias da informação.",
            "site": "https://www.njupt.edu.cn/"
        },
        {
            "nome": "Universidade Agostinho Neto (UAN)",
            "pais": "Angola",
            "descricao": "Maior instituição pública de ensino superior de Angola, com destaque em ciências sociais e engenharia.",
            "site": "https://www.uan.ao/"
        },
    ]
    return render(request, 'universidades/lista.html', {'universidades': universidades})


# Função opcional (placeholder para página de detalhes)
def detalhe_universidade(request, universidade_id):
    return render(request, 'universidades/detalhe.html')
